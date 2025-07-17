import tkinter as tk
import random

# List of games
games = [
    "Against the Storm", "American Truck Simulator", "Ancestors Legacy", "Assetto Corsa", "Astroneer",
    "Barotrauma", "Bellwright", "Bloons TD 6", "Call of Juarez - Gunslinger", "Cyberpunk 2077",
    "Dome Keeper", "Don't Starve", "DREDGE", "Endless Legend", "Far Cry 3",
    "Frostpunk", "FTL - Faster Than Light", "Graveyard Keeper", "Half-Life", "Kingdom Two Crowns",
    "Lethal Company", "Middle-Earth - Shadow of War", "Mount & Blade II - Bannerlord", "Noita", "Oxygen Not Included",
    "Planet Coaster", "Prison Architect", "Risk of Rain", "Shadow Tactics - Blades of the Shogun", "Sid Meier's Civilization 6",
    "Starbound", "Stardew Valley", "Stronghold Crusader", "Surviving Mars", "Tails of Iron",
    "Terraria", "The Binding of Isaac - Rebirth", "The Long Dark", "theHunter - Call of the Wild", "Valheim",
    "Vampire Survivors"
]

# Function to choose a random game
def choose_random_game():
    selected_game = random.choice(games)
    result_label.config(text=selected_game, font=("Helvetica", 16, "bold"))

# Setting up the main application window
root = tk.Tk()
root.title("Random Game Selector")

# Result label to display the selected game
result_label = tk.Label(root, text="Click the button to select a random game", font=("Helvetica", 14))
result_label.pack(pady=20)

# Button to trigger the game selection
choose_button = tk.Button(root, text="Choose Random Game", command=choose_random_game, font=("Helvetica", 12))
choose_button.pack(pady=10)

# Running the application
root.mainloop()
