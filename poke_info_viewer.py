"""
Description:
  Graphical user interface that displays select information about a
  user-specified Pokemon fetched from the PokeAPI

Usage:
  python poke_info_viewer.py
"""
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.messagebox import showerror
import requests

# Function to get Pokemon info from PokeAPI
def get_pokemon_info(poke_name):
    website = f"https://pokeapi.co/api/v2/pokemon/ditto"
    response = requests.get(website)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def show_error(message):
    showerror("Error".message)
# Create the main window
root = Tk()
root.title("Pokemon Information")

# Create the frames
input = ttk.Frame(root)
input.grid(row=0, column=0, columnspan=2)

info = ttk.LabelFrame(root, text="Info")
info.grid(row=1, column=0, sticky="N", padx=(10, 5), pady=(5, 10))

stats = ttk.LabelFrame(root, text="Stats")
stats.grid(row=1, column=1, sticky="N", padx=(5, 10), pady=(5, 10))

# Populate the user input frame with widgets
input_lbl = ttk.Label(input, text="Pokemon Name:")
input_lbl.grid(row=0, column=0, padx=(10, 5), pady=10)

input_ent = ttk.Entry(input)
input_ent.grid(row=0, column=1, padx=5, pady=10)


def get_info():
    poke_name = input_ent.get().strip()
    if not poke_name:
        return
    height_val["text"] = ""
    weight_val["text"] = ""
    type_val["text"] = ""
    hp_bar["value"] = 0
    att_bar["value"] = 0
    def_bar["value"] = 0
    special_attack_bar["value"] = 0
    special_defense_bar["value"] = 0
    speed_bar["value"] = 0

    poke_info = get_pokemon_info(poke_name)
    if poke_info:
        height_val["text"] = poke_info["height"]
        weight_val["text"] = poke_info["weight"]
        types = [t['type']['name'] for t in poke_info['types']]
        type_val["text"] = ', '.join(types)

        hp_bar["value"] = poke_info["stats"][0]["base_stat"]
        att_bar["value"] = poke_info["stats"][1]["base_stat"]
        def_bar["value"] = poke_info["stats"][2]["base_stat"]
        special_attack_bar["value"] = poke_info["stats"][3]["base_stat"] # Special Attack
        special_defense_bar["value"] = poke_info["stats"][4]["base_stat"] # Special Defense
        speed_bar["value"] = poke_info["stats"][5]["base_stat"] # Speed
    else:
        messagebox.showerror("Error", "Invalid Pokemon Name")

    return


input_btn = ttk.Button(input, text="Get Info", command=get_info)
input_btn.grid(row=0, column=2, padx=(5, 10), pady=10)

# Populate the info frame
height_lbl = ttk.Label(info, text="Height:")
weight_lbl = ttk.Label(info, text="Weight:")
type_lbl = ttk.Label(info, text="Type:")
height_val = ttk.Label(info, width=20)
weight_val = ttk.Label(info, width=20)
type_val = ttk.Label(info, width=20)

height_val["text"] = ""
weight_val["text"] = ""
type_val["text"] = ""

height_lbl.grid(row=0, column=0, sticky="E", padx=(10, 5), pady=(10, 5))
weight_lbl.grid(row=1, column=0, sticky="E", padx=(10, 5), pady=5)
type_lbl.grid(row=2, column=0, sticky="E", padx=(10, 5), pady=(5, 10))
height_val.grid(row=0, column=1, sticky="W", padx=(5, 10), pady=(10, 5))
weight_val.grid(row=1, column=1, sticky="W", padx=(5, 10), pady=5)
type_val.grid(row=2, column=1, sticky="W", padx=(5, 10), pady=(5, 10))

# Populate the stats frame
hp_lbl = ttk.Label(stats, text="HP:")
att_lbl = ttk.Label(stats, text="Attack:")
def_lbl = ttk.Label(stats, text="Defense:")
special_attack_lbl = ttk.Label(stats, text="Special Attack:")
special_defense_lbl = ttk.Label(stats, text="Special Defense:")
speed_lbl = ttk.Label(stats, text="Speed:")

hp_lbl.grid(row=0, column=0, sticky="E", padx=(10, 5), pady=(10, 5))
att_lbl.grid(row=1, column=0, sticky="E", padx=(10, 5), pady=5)
def_lbl.grid(row=2, column=0, sticky="E", padx=(10, 5), pady=5)
special_attack_lbl.grid(row=3, column=0, sticky="E", padx=(10, 5), pady=5)
special_defense_lbl.grid(row=4, column=0, sticky="E", padx=(10, 5), pady=5)
speed_lbl.grid(row=5, column=0, sticky="E", padx=(10, 5), pady=(5, 10))

MAX_STAT = 255
BAR_LENGTH = 200
hp_bar = ttk.Progressbar(stats, maximum=MAX_STAT, length=BAR_LENGTH)
att_bar = ttk.Progressbar(stats, maximum=MAX_STAT, length=BAR_LENGTH)
def_bar = ttk.Progressbar(stats, maximum=MAX_STAT, length=BAR_LENGTH)
special_attack_bar = ttk.Progressbar(stats, maximum=MAX_STAT, length=BAR_LENGTH)
special_defense_bar = ttk.Progressbar(stats, maximum=MAX_STAT, length=BAR_LENGTH)
speed_bar = ttk.Progressbar(stats, maximum=MAX_STAT, length=BAR_LENGTH)

hp_bar.grid(row=0, column=1, padx=(5, 10), pady=(10, 5))
att_bar.grid(row=1, column=1, padx=(5, 10), pady=5)
def_bar.grid(row=2, column=1, padx=(5, 10), pady=5)
special_attack_bar.grid(row=3, column=1, padx=(5, 10), pady=5)
special_defense_bar.grid(row=4, column=1, padx=(5, 10), pady=5)
speed_bar.grid(row=5, column=1, padx=(5, 10), pady=(5, 10))

# Create window
root.mainloop()
