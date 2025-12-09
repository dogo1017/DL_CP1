import requests
from bs4 import BeautifulSoup
from ascii_magic import AsciiArt
import ascii_magic
import os
import time
from urllib.parse import urljoin
import json


POKEMON_DB_URL = "https://pokemondb.net/pokedex/all"
BASE_URL = "https://pokemondb.net"
TARGET_WIDTH = 120
IMAGE_DIR = 'pokemon_images_db'
OUTPUT_FILE = 'pokemon_database_db.json'


os.makedirs(IMAGE_DIR, exist_ok=True)
all_pokemon_data = {}


headers = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}


def download_image(url, name):
   img_path = f"{IMAGE_DIR}/{name}.png"
   try:
       response = requests.get(url, stream=True, headers=headers)
       if response.status_code == 200:
           with open(img_path, 'wb') as f:
               for chunk in response.iter_content(1024):
                   f.write(chunk)
           return img_path
   except requests.exceptions.RequestException as e:
       print(f"Error downloading image from {url}: {e}")
   return None


def convert_image_to_ascii(image_path, width):
   try:
       my_art = AsciiArt.from_image(
           image_path
       )
       my_art.to_terminal(columns=width)
       return my_art.art
   except Exception as e:
       print(f"Error converting image {image_path} to ASCII: {e}")
       return ""




print(f"Attempting to fetch data from {POKEMON_DB_URL}...")
try:
   page_response = requests.get(POKEMON_DB_URL, headers=headers)
   page_response.raise_for_status()
   soup = BeautifulSoup(page_response.content, 'html.parser')
   pokedex_table = soup.find('table', {'id': 'pokedex'})
   if not pokedex_table:
       print("Could not find the Pokédex table.")
       exit()
  
   rows = pokedex_table.find('tbody').find_all('tr')
  
   for row in rows:
       cols = row.find_all('td')
       if len(cols) > 1:
           name_anchor = cols[1].find('a', class_='ent-name')
           if not name_anchor:
               continue
            

           pokemon_name = name_anchor.text.strip()
           img_tag = cols[0].find('img')
          
           img_url = img_tag.get('data-src') or img_tag.get('src')
           if img_url and 'http' not in img_url:
                img_url = urljoin(BASE_URL, img_url)


           stats = {
               'hp': int(cols[4].text.strip()),
               'attack': int(cols[5].text.strip()),
               'defense': int(cols[6].text.strip()),
               'sp_atk': int(cols[7].text.strip()),
               'sp_def': int(cols[8].text.strip()),
               'speed': int(cols[9].text.strip())
           }


           image_path = download_image(img_url, pokemon_name)
           if image_path:
               ascii_art = convert_image_to_ascii(image_path, TARGET_WIDTH)
               all_pokemon_data[pokemon_name] = {
                   'stats': stats,
                   'ascii_art': ascii_art
               }
               os.remove(image_path)
               print(f"Processed {pokemon_name}")
          
           time.sleep(0.5)


except requests.exceptions.RequestException as e:
   print(f"Failed to fetch the main Pokédex page: {e}")
   exit()


with open(OUTPUT_FILE, 'w') as f:
   json.dump(all_pokemon_data, f, indent=4)


print(f"\nSuccessfully scraped {len(all_pokemon_data)} Pokémon. Data saved to {OUTPUT_FILE}")


# >>>>> Add this line to see the raw string for ONE pokemon <<<<<
# We use repr() to see the literal ANSI codes (e.g. \x1b[38;2;...m)
print("\nRAW ASCII ART STRING EXAMPLE (Copy this for your Python code):\n")
if 'Bulbasaur' in all_pokemon_data:
   print(repr(all_pokemon_data['Bulbasaur']['ascii_art']))