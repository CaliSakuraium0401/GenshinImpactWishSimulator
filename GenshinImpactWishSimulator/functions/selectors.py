import sys
sys.path.append('../GenshinImpactWishSimulator')

from banners.characters import *
from miscellaneous.typography import * 
from functions.wishing import *

def select_character_banner(character_banners):
    selected_banner = -1
    valid = False
    while valid != True:
        try:
            print()
            display_all_character_banners()
            print()
            if selected_banner >= 0 and selected_banner <= len(character_banners):
                valid = True
                return selected_banner
            else:
                print()
                selected_banner = int(input(f"{EMPHASIZE.BOLD}Select a banner using it's key: {EMPHASIZE.END}"))
                print()
        except ValueError:
            print()
            print(f"{COLOR.RED}ERROR: The input is invalid, only integers are accepted.{COLOR.END}")
            print()