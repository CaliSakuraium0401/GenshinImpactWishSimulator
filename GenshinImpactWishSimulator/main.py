import sys
import random
sys.path.append('../GenshinImpactWishSimulator')

from miscellaneous.typography import * 
from functions.selectors import *
from banners.characters import *
from functions.wishing import *

inventory = []
already_itterated = set()

def main():
	character_banner = select_character_banner(CharacterBanner.character_banners)
	character_banner = CharacterBanner.character_banners[character_banner]
	character_banner.display_banner_info()
	print()
	wish_event_character(get_wish(), get_pity(), get_guaranteed(), character_banner, inventory)
	print()
	for item in inventory:
		if item not in already_itterated:
			#print(f"[x{inventory.count(item)}] - {item}")
			already_itterated.add(item)

	print(f"{EMPHASIZE.BOLD_UNDERLINE}CHARACTERS{EMPHASIZE.END}")
   
	for item in character_banner.promotional_five_star:
		if item in already_itterated:
			print(f"[C{inventory.count(item)}] {COLOR.YELLOW}5 ★ {item}{COLOR.END}")
	for item in character_banner.standard_five_stars:
		if item in already_itterated:
			print(f"[C{inventory.count(item)}] {COLOR.YELLOW}4 ★ {item}{COLOR.END}")

	for item in character_banner.promotional_four_stars:
		if item in already_itterated:
			print(f"[C{inventory.count(item)}] {COLOR.PURPLE}4 ★ {item}{COLOR.END}")

	for item in character_banner.standard_four_stars:
		if item in already_itterated:
			print(f"[C{inventory.count(item)}] {COLOR.PURPLE}4 ★ {item}{COLOR.END}")
 
	print(f"{EMPHASIZE.BOLD_UNDERLINE}WEAPONS{EMPHASIZE.END}")
 
	for item in character_banner.four_star_weapons:
		if item in already_itterated:
			print(f"[x{inventory.count(item)}] {COLOR.PURPLE}4 ★ {item}{COLOR.END}")
      
	for item in character_banner.three_star_weapons:
		if item in already_itterated:
			print(f"[x{inventory.count(item)}] {COLOR.CYAN}3 ★ {item}{COLOR.END}")

main()