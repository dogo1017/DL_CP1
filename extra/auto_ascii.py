import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import time
import json
import os
from ascii_magic import AsciiArt
from urllib.parse import urljoin
from tqdm import tqdm
import logging

OUTPUT_FILE = "pokemon_database_all.json"
IMAGE_DIR = "pokemon_images_db" 
SMALL_WIDTH = 40
LARGE_WIDTH = 100
REQUEST_DELAY = 0.65 
USE_OFFICIAL_ARTWORK = True
MAX_POKEMON = None  
LOG_LEVEL = logging.INFO

logging.basicConfig(level=LOG_LEVEL, format="%(asctime)s %(levelname)s: %(message)s")

API_BASE = "https://pokeapi.co/api/v2/"
POKEMON_LIST_ENDPOINT = urljoin(API_BASE, "pokemon?limit=100000&offset=0")

if IMAGE_DIR:
    os.makedirs(IMAGE_DIR, exist_ok=True)

session = requests.Session()
retries = Retry(total=5, backoff_factor=1, status_forcelist=(429, 500, 502, 503, 504))
session.mount("https://", HTTPAdapter(max_retries=retries))
session.headers.update({
    "User-Agent": "PokemonDBBuilder/1.0 (+https://example.local) ascii_magic script"
})

def safe_get(url):
    """HTTP GET with error handling. Returns JSON if possible or raw content when requested."""
    try:
        r = session.get(url, timeout=30)
        r.raise_for_status()
        content_type = r.headers.get("Content-Type", "")
        if "application/json" in content_type:
            return r.json()
        return r.content
    except requests.HTTPError as e:
        logging.warning(f"HTTP error for {url}: {e}")
    except requests.RequestException as e:
        logging.warning(f"Request exception for {url}: {e}")
    return None

def fetch_all_pokemon_list():
    """Get list of all pokemon resource entries from the API."""
    logging.info("Fetching list of all Pokémon from PokéAPI...")
    data = safe_get(POKEMON_LIST_ENDPOINT)
    if not data or "results" not in data:
        raise RuntimeError("Could not fetch the master pokemon list.")
    return data["results"]

def download_image(url, name):
    """Downloads an image and returns local path or None."""
    if not url:
        return None
    try:
        r = session.get(url, stream=True, timeout=30)
        r.raise_for_status()
        if not IMAGE_DIR:
            path = f"/tmp/{name}.png"
        else:
            path = os.path.join(IMAGE_DIR, f"{name}.png")
        with open(path, "wb") as fh:
            for chunk in r.iter_content(1024):
                fh.write(chunk)
        return path
    except Exception as e:
        logging.warning(f"Failed downloading image {url}: {e}")
        return None

def convert_image_to_ascii(image_path, width):
    """Return ASCII art string using ascii_magic. Returns empty string on failure."""
    try:
        art = AsciiArt.from_image(image_path)
        return art.to_ascii(columns=width, monochrome=False)
    except Exception as e:
        logging.warning(f"ASCII conversion failed for {image_path}: {e}")
        return ""

def parse_evolution_chain(chain_obj):
    """
    Recursively parse a PokeAPI evolution chain object into a flat list of transitions.
    Format returned: list of dicts like {'from': 'Pichu', 'to': 'Pikachu', 'trigger': 'level-up', 'details': {...}}
    """
    evo_list = []

    def walk(node, from_species=None):
        species_name = node['species']['name'].capitalize()
        if from_species:
            for detail in node.get('evolution_details', []):
                readable = {
                    'trigger': detail.get('trigger', {}).get('name') if isinstance(detail.get('trigger'), dict) else detail.get('trigger'),
                    'item': detail.get('item', {}).get('name') if detail.get('item') else None,
                    'min_level': detail.get('min_level'),
                    'gender': detail.get('gender'),
                    'time_of_day': detail.get('time_of_day'),
                    'known_move': detail.get('known_move', {}).get('name') if detail.get('known_move') else None,
                    'location': detail.get('location', {}).get('name') if detail.get('location') else None,
                    'other': {k: v for k, v in detail.items() if k not in ['trigger', 'item', 'min_level', 'gender', 'time_of_day', 'known_move', 'location']}
                }
                evo_list.append({
                    'from': from_species,
                    'to': species_name,
                    'details': readable
                })
        for child in node.get('evolves_to', []):
            walk(child, species_name)

    walk(chain_obj, from_species=None)
    return evo_list

def get_pokemon_data(pokemon_resource):
    """
    Given a resource element with 'name' and 'url' (from /pokemon list),
    fetches pokemon endpoint, species endpoint, evolution chain, artwork, moves, stats, etc.
    Returns a dict ready to be JSON-serializable.
    """
    name = pokemon_resource['name'] 
    pokemon_url = pokemon_resource['url']  # e.g. https://pokeapi.co/api/v2/pokemon/1/
    poke = safe_get(pokemon_url)
    time.sleep(REQUEST_DELAY)
    if not poke:
        logging.warning(f"Skipping {name}: failed to fetch pokemon endpoint.")
        return None

    species_url = poke.get('species', {}).get('url')
    species = safe_get(species_url) if species_url else None
    time.sleep(REQUEST_DELAY)

    display_name = poke.get('name', name).capitalize()
    pokedex_number = poke.get('id')
    types = [t['type']['name'].capitalize() for t in poke.get('types', [])]

    stat_map = {}
    for s in poke.get('stats', []):
        stat_name = s['stat']['name']
        base = s['base_stat']
        if stat_name == 'hp':
            stat_map['hp'] = base
        elif stat_name == 'attack':
            stat_map['attack'] = base
        elif stat_name == 'defense':
            stat_map['defense'] = base
        elif stat_name == 'special-attack':
            stat_map['special_attack'] = base
        elif stat_name == 'special-defense':
            stat_map['special_defense'] = base
        elif stat_name == 'speed':
            stat_map['speed'] = base

    abilities = []
    for a in poke.get('abilities', []):
        ability_name = a['ability']['name']
        abilities.append({
            'name': ability_name.replace('-', ' ').title(),
            'is_hidden': a.get('is_hidden', False),
            'slot': a.get('slot')
        })

    moves = []
    for m in poke.get('moves', []):
        move_obj = {'move_name': m['move']['name'].replace('-', ' ').title(), 'details': []}
        for det in m.get('version_group_details', []):
            move_learn_method = det.get('move_learn_method', {}).get('name')
            version_group = det.get('version_group', {}).get('name')
            level_learned = det.get('level_learned_at')
            move_obj['details'].append({
                'version_group': version_group,
                'learn_method': move_learn_method,
                'level': level_learned
            })
        moves.append(move_obj)

    description = "N/A"
    if species:
        entries = species.get('flavor_text_entries', [])
        for entry in entries:
            if entry.get('language', {}).get('name') == 'en':
                description = entry.get('flavor_text', '').replace('\n', ' ').replace('\x0c', ' ').strip()
                break

    catch_rate = None
    base_exp = poke.get('base_experience')
    if species:
        catch_rate = species.get('capture_rate')

    evolution_details = []
    if species and species.get('evolution_chain', {}).get('url'):
        evo_url = species['evolution_chain']['url']
        evo_resp = safe_get(evo_url)
        time.sleep(REQUEST_DELAY)
        if evo_resp and 'chain' in evo_resp:
            evo_list = parse_evolution_chain(evo_resp['chain'])
            evolution_details = evo_list

    image_url = None
    if USE_OFFICIAL_ARTWORK:
        image_url = poke.get('sprites', {}).get('other', {}).get('official-artwork', {}).get('front_default')
    if not image_url:
        image_url = poke.get('sprites', {}).get('front_default')

    small_ascii = ""
    large_ascii = ""
    image_path = None
    if image_url:
        image_path = download_image(image_url, f"{display_name}-{pokedex_number}")
        time.sleep(REQUEST_DELAY)
        if image_path:
            small_ascii = convert_image_to_ascii(image_path, SMALL_WIDTH)
            large_ascii = convert_image_to_ascii(image_path, LARGE_WIDTH)
            if not IMAGE_DIR:
                try:
                    os.remove(image_path)
                except:
                    pass

    result = {
        'name': display_name,
        'pokedex_number': pokedex_number,
        'type': types,
        'description': description,
        'base_stats': stat_map,
        'abilities': abilities,
        'catch_rate': catch_rate,
        'base_experience_yield': base_exp,
        'evolution_details': evolution_details,
        'learnable_moves': moves,
        'small_ascii': small_ascii,
        'large_ascii': large_ascii,
        'artwork_url': image_url
    }
    return result

def main():
    all_pokemon = []
    resources = fetch_all_pokemon_list()
    if MAX_POKEMON:
        resources = resources[:MAX_POKEMON]
    logging.info(f"Found {len(resources)} pokemon entries. Beginning processing...")

    for res in tqdm(resources, desc="Pokémon", unit="pkmn"):
        try:
            data = get_pokemon_data(res)
            if data:
                all_pokemon.append(data)
        except Exception as e:
            logging.exception(f"Unexpected error processing {res.get('name')}: {e}")

    logging.info(f"Saving {len(all_pokemon)} Pokémon to {OUTPUT_FILE} ...")
    with open(OUTPUT_FILE, "w", encoding="utf-8") as fh:
        json.dump(all_pokemon, fh, indent=2, ensure_ascii=False)

    logging.info("Done.")

if __name__ == "__main__":
    main()

