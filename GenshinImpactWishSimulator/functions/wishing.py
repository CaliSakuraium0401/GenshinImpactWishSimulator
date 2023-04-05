import random
import math
import random

import sys
sys.path.append('../GenshinImpactWishSimulator')

from miscellaneous.typography import * 
from functions.selectors import *

# Weapon Wish Banner
    # A 5-star character or weapon – 0.7% chance of dropping
    # A 4-star character or weapon – 6% chance of dropping
    # A 3-star weapon – 93.3% chance of dropping.

loop = True

def get_wish():
    while True:
        try:
            wishes = int(input(f"{EMPHASIZE.BOLD}Wishes: {EMPHASIZE.END}"))
            if wishes >= 1:
                return wishes
            print(f"{COLOR.RED}ERROR: The input must be a positive integer.{COLOR.END}")
        except ValueError:
            print(f"{COLOR.RED}ERROR: The input is invalid, only integers are accepted.{COLOR.END}")

def get_pity():
    while True:
        try:
            pity = int(input(f"{EMPHASIZE.BOLD}Pity: {EMPHASIZE.END}"))
            if 0 <= pity < 90:
                return pity
            print(f"{COLOR.RED}ERROR: The input must be between 0 and 89 (inclusive).{COLOR.END}")
        except ValueError:
            print(f"{COLOR.RED}ERROR: The input is invalid, only integers are accepted.{COLOR.END}")

def get_guaranteed():
    while True:
        guaranteed = input(f"{EMPHASIZE.BOLD}Guranteed (Y/N): {EMPHASIZE.END}").upper()
        if guaranteed == "Y":
            return True
        elif guaranteed == "N":
            return False
        print(f"{COLOR.RED}ERROR: The input must be 'Y' or 'N'.{COLOR.END}")


def get_five_star_from_character(guaranteed, character_banner):
    if guaranteed == True:
        guaranteed = False
        return random.choice(character_banner.promotional_five_star), guaranteed
    else:
        if random.choice(["Won", "Lost"]) == "Won":
            guaranteed = False
            return random.choice(character_banner.promotional_five_star), guaranteed
        else:
            guaranteed = True 
            return random.choice(character_banner.standard_five_stars), guaranteed

def get_four_star_from_character(guaranteed, character_banner):
    
    if guaranteed == True:
        guaranteed = False
        return random.choice(character_banner.promotional_four_stars), guaranteed
    else:
        guaranteed = True
        if random.choice(["Character", "Weapon"]) == "Character":
            return random.choice(character_banner.standard_four_stars), guaranteed
        else:
            return random.choice(character_banner.four_star_weapons), guaranteed

def get_three_star_from_character(character_banner):
     return random.choice(character_banner.three_star_weapons)

def wish_event_character(wishes, pity, guaranteed, character_banner, inventory):
    
    for wish in range(wishes):
        
        pity += 1
        
        if pity % 10 == 0:
            
            if pity == 90:
                item, guaranteed = get_five_star_from_character(guaranteed, character_banner)
                print(f"{COLOR.YELLOW}5 ★ | {item}{COLOR.END}")
                pity = 0
            else:
                item, guaranteed = get_four_star_from_character(guaranteed, character_banner)
                print(f"{COLOR.PURPLE}4 ★ | {item}{COLOR.END}")
                
        else:
        
            chance = round(random.uniform(0, 100), 3)

            if (chance >= 0) and (chance <= 0.600): 
                item, guaranteed = get_five_star_from_character(guaranteed, character_banner)
                print(f"{COLOR.YELLOW}5 ★ | {item}{COLOR.END}")
            elif (chance >= 0.600) and (chance <= 5.100):
                item, guaranteed = get_four_star_from_character(guaranteed, character_banner)
                print(f"{COLOR.PURPLE}4 ★ | {item}{COLOR.END}")
            elif (chance >= 5.100) and (chance < 100):
                item = get_three_star_from_character(character_banner)
                print(f"{COLOR.CYAN}3 ★ | {item}{COLOR.END}")
                
        inventory.append(item)

    return inventory