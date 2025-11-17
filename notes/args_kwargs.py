#DL 1st, args and kwargs notes


def hello(*names, **kwargs):
    for n in names:
        print(f"Hello {n} {kwargs['last_name']}")

hello("Alex", "Katie", "Andrew", "Vienna", last_name="LaRose", dad = "Eric", num_cats = 5)


def summary(**story):
    sum = ""
    if "name" in story.keys():