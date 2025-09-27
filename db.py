from functools import lru_cache
import json


@lru_cache(maxsize=1)
def music_db():
    """Reads songs.json file and returns a list of dictionaries"""
    with open('songs.json', 'r') as file:
        return json.load(file)
