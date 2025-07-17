import os
import json
import re
from pathlib import Path

def get_steam_library_folders(steam_path):
    """
    Get the paths to all Steam library folders.
    
    Args:
    steam_path (str): The root path to the Steam installation.
    
    Returns:
    list: A list of paths to Steam library folders.
    """
    library_folders_file = Path(steam_path) / 'steamapps' / 'libraryfolders.vdf'
    
    if not library_folders_file.exists():
        raise FileNotFoundError(f"{library_folders_file} does not exist.")
    
    library_folders = [Path(steam_path) / 'steamapps']
    
    with open(library_folders_file, 'r', encoding='utf-8') as file:
        content = file.read()
        matches = re.findall(r'"\d+"\s*"\s*(.*?)\s*"', content)
        for match in matches:
            library_folders.append(Path(match) / 'steamapps')
    
    return library_folders

def get_installed_games(library_folders):
    """
    Get the names of installed games from Steam library folders.
    
    Args:
    library_folders (list): A list of paths to Steam library folders.
    
    Returns:
    list: A list of installed game names.
    """
    games = []
    
    for folder in library_folders:
        for appmanifest in folder.glob('appmanifest_*.acf'):
            with open(appmanifest, 'r', encoding='utf-8') as file:
                content = file.read()
                name_match = re.search(r'"name"\s*"(.*?)"', content)
                if name_match:
                    games.append(name_match.group(1))
    
    return games

def choose_random_game(games_list):
    """
    This function takes a list of games and returns a randomly selected game.
    
    Args:
    games_list (list): The list of games to choose from.
    
    Returns:
    str: The randomly selected game.
    """
    return random.choice(games_list)

# Path to the Steam installation directory
steam_path = 'C:/Program Files (x86)/Steam'  # Update this path as needed

# Get the paths to all Steam library folders
library_folders = get_steam_library_folders(steam_path)

# Get the names of installed games
installed_games = get_installed_games(library_folders)

if installed_games:
    # Select a random game
    selected_game = choose_random_game(installed_games)

    # Output the selected game
    print(f"The game chosen for you to play is: {selected_game}")
else:
    print("No installed games found.")
