import sys
sys.path.append('../GenshinImpactWishSimulator')
from miscellaneous.typography import *

# alt shift i - get to end of multiple lines
# cntrl shift p --> convert to array 

class CharacterBanner:
	
	character_banners = []
 
	def __init__(self, banner_name, start_date, end_date, promotional_five_star, 
	promotional_four_stars, standard_five_stars, standard_four_stars, four_star_weapons, 
	three_star_weapons):
		self.banner_name = banner_name
		self.start_date = start_date
		self.end_date = end_date
		self.promotional_five_star = promotional_five_star
		self.promotional_four_stars = promotional_four_stars
		self.standard_five_stars = standard_five_stars
		self.standard_four_stars = standard_four_stars
		self.four_star_weapons = four_star_weapons
		self.three_star_weapons = three_star_weapons
  
		self.__class__.character_banners.append(self)
	def display_banner_info(self):
		CharacterBanner.display_banner_name(self)
		print(f"{EMPHASIZE.BOLD}{COLOR.YELLOW}Promotional 5 ★ Character{EMPHASIZE.END}: ", end="")
		print(*self.promotional_five_star, sep=" / ")
		print(f"{EMPHASIZE.BOLD}{COLOR.PURPLE}Promotional 4 ★ Characters{EMPHASIZE.END}: ", end="")
		print(*self.promotional_four_stars, sep=" / ")
		print(f"{EMPHASIZE.BOLD}{COLOR.YELLOW}Standard 5 ★ Characters{EMPHASIZE.END}: ", end="")
		print(*self.standard_five_stars, sep=" / ")
		print(f"{EMPHASIZE.BOLD}{COLOR.PURPLE}Standard 4 ★ Characters{EMPHASIZE.END}: ", end="")
		print(*self.standard_four_stars, sep=" / ")
		print(f"{EMPHASIZE.BOLD}{COLOR.PURPLE}Standard 4 ★ Weapons{EMPHASIZE.END}: ", end="")
		print(*self.four_star_weapons, sep=" / ")
		print(f"{EMPHASIZE.BOLD}{COLOR.CYAN}Standard 3 ★ Weapons{EMPHASIZE.END}: ", end="") 
		print(*self.three_star_weapons, sep=" / ")
	def display_banner_name(self):
		print(f"{EMPHASIZE.BOLD_UNDERLINE}{self.banner_name} ({EMPHASIZE.BOLD_UNDERLINE}{self.start_date} - {self.end_date}{EMPHASIZE.END})")
  
ballad_in_goblets_1 = CharacterBanner(
"Ballad in Goblets",
"09-28-2020",
"10-18-2020",
["Venti"], 
["Barbara","Fischl","Xiangling"],
["Jean","Qiqi","Keqing","Mona","Diluc"],
["Sucrose","Chongyun","Beidou","Razor","Ningguang","Noelle","Xingqiu","Bennett"], 
["Favonius Warbow","Rust","Sacrificial Bow","The Stringless","Eye of Perception","Favonius Codex","Sacrificial Fragments","The Widsith","Favonius Greatsword","Rainslasher","Sacrificial Greatsword","The Bell","Dragon's Bane","Favonius Lance","Favonius Sword","Lion's Roar","Sacrificial Sword","The Flute"], 
["Raven Bow", "Sharp­shooter's Oath", "Slingshot", "Emerald Orb", "Magic Guide", "Thrilling Tales of Dragon Slayer", "Bloodtainted Greatsword", "Debate Club", "Ferrous Shadow", "Black Tassel", "Cool Steel", "Harbinger of Dawn", "Skyrider Sword"])

sparkling_steps_1 = CharacterBanner(
"Sparkling Steps",
"10-20-2020",
"11-10-2020",
["Klee"], 
["Xingqiu","Noelle","Sucrose"],
["Jean","Qiqi","Keqing","Mona","Diluc"],
["Chongyun", "Beidou", "Fischl", "Razor", "Ningguang", "Barbara", "Bennett", "Xiangling"],
["Favonius Warbow", "Rust", "Sacrificial Bow", "The Stringless", "Eye of Perception", "Favonius Codex", "Sacrificial Fragments", "The Widsith", "Favonius Greatsword", "Rainslasher", "Sacrificial Greatsword", "The Bell", "Dragon's Bane", "Favonius Lance", "Favonius Sword", "Lion's Roar", "Sacrificial Sword", "The Flute"],
["Raven Bow", "Sharpshooter's Oath", "Slingshot", "Emerald Orb", "Magic Guide", "Thrilling Tales of Dragon Slayers", "Bloodtainted Greatsword", "Debate Club", "Ferrous Shadow", "Black Tassel", "Cool Steel", "Harbinger of Dawn", "Skyrider Sword"])

farwell_of_snezhnaya_1 = CharacterBanner(
"Farewell of Snezhnaya",
"11-11-2020",
"12-01-2020",
["Tartaglia"],
["Diona", "Beidou", "Ningguang"],
["Jean","Qiqi","Keqing","Mona","Diluc"],
["Sucrose", "Chongyun", "Fischl", "Razor", "Noelle", "Barbara", "Xingqiu", "Bennett", "Xiangling"],
["Favonius Warbow", "Rust", "Sacrificial Bow", "The Stringless", "Eye of Perception", "Favonius Codex", "Sacrificial Fragments", "The Widsith", "Favonius Greatsword", "Rainslasher", "Sacrificial Greatsword", "The Bell", "Dragon's Bane", "Favonius Lance", "Favonius Sword", "Lion's Roar", "Sacrificial Sword", "The Flute"],
["Raven Bow", "Sharpshooter's Oath", "Slingshot", "Emerald Orb", "Magic Guide", "Thrilling Tales of Dragon Slayers", "Bloodtainted Greatsword", "Debate Club", "Ferrous Shadow", "Black Tassel", "Cool Steel", "Harbinger of Dawn", "Skyrider Sword"])

gentry_of_hermitage_1 = CharacterBanner(
"Gentry of Hermitage",
"12-01-2020",
"12-22-2020",
["Zhongli"],
["Xinyan", "Razor", "Chongyun"],
["Jean","Qiqi","Keqing","Mona","Diluc"],
["Sucrose", "Beidou", "Fischl", "Ningguang", "Noelle", "Barbara", "Xingqiu", "Bennett", "Xiangling"],
["Favonius Warbow", "Rust", "Sacrificial Bow", "The Stringless", "Eye of Perception", "Favonius Codex", "Sacrificial Fragments", "The Widsith", "Favonius Greatsword", "Rainslasher", "Sacrificial Greatsword", "The Bell", "Dragon's Bane", "Favonius Lance", "Favonius Sword", "Lion's Roar", "Sacrificial Sword", "The Flute"],
["Raven Bow", "Sharpshooter's Oath", "Slingshot", "Emerald Orb", "Magic Guide", "Thrilling Tales of Dragon Slayers", "Bloodtainted Greatsword", "Debate Club", "Ferrous Shadow", "Black Tassel", "Cool Steel", "Harbinger of Dawn", "Skyrider Sword"])

secretum_secretorum_1 = CharacterBanner(
"Secretum Secretorum",
"12-23-2020",
"01-12-2021",
["Albedo"],
["Fischl", "Sucrose", "Bennett"],
["Jean","Qiqi","Keqing","Mona","Diluc"],
["Chongyun", "Diona", "Beidou", "Razor", "Ningguang", "Noelle", "Barbara", "Xingqiu", "Xiangling", "Xinyan"],
["Favonius Warbow", "Rust", "Sacrificial Bow", "The Stringless", "Eye of Perception", "Favonius Codex", "Sacrificial Fragments", "The Widsith", "Favonius Greatsword", "Rainslasher", "Sacrificial Greatsword", "The Bell", "Dragon's Bane", "Favonius Lance", "Favonius Sword", "Lion's Roar", "Sacrificial Sword", "The Flute"],
["Raven Bow", "Sharpshooter's Oath", "Slingshot", "Emerald Orb", "Magic Guide", "Thrilling Tales of Dragon Slayers", "Bloodtainted Greatsword", "Debate Club", "Ferrous Shadow", "Black Tassel", "Cool Steel", "Harbinger of Dawn", "Skyrider Sword"])

adrift_in_the_harbor_1 = CharacterBanner(
"Adrift in the Harbor",
"01-12-2021",
"02-02-2021",
["Ganyu"],
["Xiangling", "Xingqiu", "Noelle"],
["Jean","Qiqi","Keqing","Mona","Diluc"],
["Sucrose", "Chongyun", "Diona", "Beidou", "Fischl", "Razor", "Ningguang", "Barbara", "Bennett", "Xinyan"],
["Favonius Warbow", "Rust", "Sacrificial Bow", "The Stringless", "Eye of Perception", "Favonius Codex", "Sacrificial Fragments", "The Widsith", "Favonius Greatsword", "Rainslasher", "Sacrificial Greatsword", "The Bell", "Dragon's Bane", "Favonius Lance", "Favonius Sword", "Lion's Roar", "Sacrificial Sword", "The Flute"],
["Raven Bow", "Sharpshooter's Oath", "Slingshot", "Emerald Orb", "Magic Guide", "Thrilling Tales of Dragon Slayers", "Bloodtainted Greatsword", "Debate Club", "Ferrous Shadow", "Black Tassel", "Cool Steel", "Harbinger of Dawn", "Skyrider Sword"])

invitation_to_mundane_life_1 = CharacterBanner(
"Invitation to Mundane Life",
"02-03-2021",
"02-17-2021",
["Xiao"],
["Diona", "Beidou", "Xinyan"],
["Jean","Qiqi","Keqing","Mona","Diluc"],
["Sucrose", "Chongyun", "Fischl", "Razor", "Ningguang", "Noelle", "Barbara", "Xingqiu", "Bennett", "Xiangling"],
["Favonius Warbow", "Rust", "Sacrificial Bow", "The Stringless", "Eye of Perception", "Favonius Codex", "Sacrificial Fragments", "The Widsith", "Favonius Greatsword", "Rainslasher", "Sacrificial Greatsword", "The Bell", "Dragon's Bane", "Favonius Lance", "Favonius Sword", "Lion's Roar", "Sacrificial Sword", "The Flute"],
["Raven Bow", "Sharpshooter's Oath", "Slingshot", "Emerald Orb", "Magic Guide", "Thrilling Tales of Dragon Slayers", "Bloodtainted Greatsword", "Debate Club", "Ferrous Shadow", "Black Tassel", "Cool Steel", "Harbinger of Dawn", "Skyrider Sword"])

dance_of_lanterns_1 = CharacterBanner(
"Dance of Lanterns",
"02-17-2021",
"03-02-2021",
["Keqing"],
["Ningguang", "Bennett", "Barbara"],
["Jean","Qiqi","Mona","Diluc"],
["Sucrose", "Chongyun", "Diona", "Beidou", "Fisch", "Razor", "Noelle", "Xingqiu", "Xiangling", "Xinyan"],
["Favonius Warbow", "Rust", "Sacrificial Bow", "The Stringless", "Eye of Perception", "Favonius Codex", "Sacrificial Fragments", "The Widsith", "Favonius Greatsword", "Rainslasher", "Sacrificial Greatsword", "The Bell", "Dragon's Bane", "Favonius Lance", "Favonius Sword", "Lion's Roar", "Sacrificial Sword", "The Flute"],
["Raven Bow", "Sharpshooter's Oath", "Slingshot", "Emerald Orb", "Magic Guide", "Thrilling Tales of Dragon Slayers", "Bloodtainted Greatsword", "Debate Club", "Ferrous Shadow", "Black Tassel", "Cool Steel", "Harbinger of Dawn", "Skyrider Sword"])

moment_of_bloom_1 = CharacterBanner(
"Moment of Bloom",
"03-02-2021",
"03-16-2021",
["Hu Tao"],
["Xingqiu", "Xiangling", "Chongyun"],
["Jean","Qiqi","Keqing","Mona","Diluc"],
["Sucrose", "Diona", "Beidou", "Fischl", "Razor", "Ningguang", "Noelle", "Barbara", "Bennett", "Xinyan"],
["Favonius Warbow", "Rust", "Sacrificial Bow", "The Stringless", "Eye of Perception", "Favonius Codex", "Sacrificial Fragments", "The Widsith", "Favonius Greatsword", "Rainslasher", "Sacrificial Greatsword", "The Bell", "Dragon's Bane", "Favonius Lance", "Favonius Sword", "Lion's Roar", "Sacrificial Sword", "The Flute"],
["Raven Bow", "Sharpshooter's Oath", "Slingshot", "Emerald Orb", "Magic Guide", "Thrilling Tales of Dragon Slayers", "Bloodtainted Greatsword", "Debate Club", "Ferrous Shadow", "Black Tassel", "Cool Steel", "Harbinger of Dawn", "Skyrider Sword"])

ballad_in_goblets_2 = CharacterBanner(
"Ballad in Goblets",
"03-17-2021",
"04-06-2021",
["Venti"],
["Sucrose", "Razor", "Noelle"],
["Jean","Qiqi","Keqing","Mona","Diluc"],
["Chongyun", "Diona", "Beidou", "Fischl", "Ningguang", "Barbara", "Xingqiu", "Bennett", "Xiangling", "Xinyan"],
["Favonius Warbow", "Rust", "Sacrificial Bow", "The Stringless", "Eye of Perception", "Favonius Codex", "Sacrificial Fragments", "The Widsith", "Favonius Greatsword", "Rainslasher", "Sacrificial Greatsword", "The Bell", "Dragon's Bane", "Favonius Lance", "Favonius Sword", "Lion's Roar", "Sacrificial Sword", "The Flute"],
["Raven Bow", "Sharpshooter's Oath", "Slingshot", "Emerald Orb", "Magic Guide", "Thrilling Tales of Dragon Slayers", "Bloodtainted Greatsword", "Debate Club", "Ferrous Shadow", "Black Tassel", "Cool Steel", "Harbinger of Dawn", "Skyrider Sword"])

farewell_of_snezhnaya_2 = CharacterBanner(
"Farewell of Snezhnaya",
"04-06-2021",
"04-27-2021",
["Tartaglia"],
["Rosaria", "Barbara", "Fischl"],
["Jean","Qiqi","Keqing","Mona","Diluc"],
["Sucrose", "Chongyun", "Diona", "Beidou", "Razor", "Ningguang", "Noelle", "Xingqiu", "Bennett", "Xiangling", "Xinyan"],
["Favonius Warbow", "Rust", "Sacrificial Bow", "The Stringless", "Eye of Perception", "Favonius Codex", "Sacrificial Fragments", "The Widsith", "Favonius Greatsword", "Rainslasher", "Sacrificial Greatsword", "The Bell", "Dragon's Bane", "Favonius Lance", "Favonius Sword", "Lion's Roar", "Sacrificial Sword", "The Flute"],
["Raven Bow", "Sharpshooter's Oath", "Slingshot", "Emerald Orb", "Magic Guide", "Thrilling Tales of Dragon Slayers", "Bloodtainted Greatsword", "Debate Club", "Ferrous Shadow", "Black Tassel", "Cool Steel", "Harbinger of Dawn", "Skyrider Sword"])

gentry_of_hermitage_2 = CharacterBanner(
"Gentry of Hermitage",
"04-28-2021",
"05-18-2021",
["Zhongli"],
["Yanfei","Noelle","Diona"],
["Jean","Qiqi","Keqing","Mona","Diluc"],
["Sucrose", "Chongyun", "Rosaria", "Beidou", "Fischl", "Razor", "Ningguang", "Barbara", "Xingqiu", "Bennett", "Xiangling", "Xinyan"],
["Favonius Warbow", "Rust", "Sacrificial Bow", "The Stringless", "Eye of Perception", "Favonius Codex", "Sacrificial Fragments", "The Widsith", "Favonius Greatsword", "Rainslasher", "Sacrificial Greatsword", "The Bell", "Dragon's Bane", "Favonius Lance", "Favonius Sword", "Lion's Roar", "Sacrificial Sword", "The Flute"],
["Raven Bow", "Sharpshooter's Oath", "Slingshot", "Emerald Orb", "Magic Guide", "Thrilling Tales of Dragon Slayers", "Bloodtainted Greatsword", "Debate Club", "Ferrous Shadow", "Black Tassel", "Cool Steel", "Harbinger of Dawn", "Skyrider Sword"])

born_of_ocean_swell = CharacterBanner(
"Born of Ocean Swell",
"05-18-2021",
"06-08-2021",
["Eula"],
["Xinyan", "Xingqiu", "Beidou"],
["Jean","Qiqi","Keqing","Mona","Diluc"],
["Sucrose", "Chongyun", "Diona", "Rosaria", "Fischl", "Razor", "Ningguang", "Noelle", "Barbara", "Bennett", "Xiangling"],
["Favonius Warbow", "Rust", "Sacrificial Bow", "The Stringless", "Eye of Perception", "Favonius Codex", "Sacrificial Fragments", "The Widsith", "Favonius Greatsword", "Rainslasher", "Sacrificial Greatsword", "The Bell", "Dragon's Bane", "Favonius Lance", "Favonius Sword", "Lion's Roar", "Sacrificial Sword", "The Flute"],
["Raven Bow", "Sharpshooter's Oath", "Slingshot", "Emerald Orb", "Magic Guide", "Thrilling Tales of Dragon Slayers", "Bloodtainted Greatsword", "Debate Club", "Ferrous Shadow", "Black Tassel", "Cool Steel", "Harbinger of Dawn", "Skyrider Sword"])

sparkling_steps_2 = CharacterBanner(
"Sparkling Steps",
"06-09-2021",
"06-29-2021",
["Klee"],
["Barbara", "Sucrose", "Fischl"],
["Jean","Qiqi","Keqing","Mona","Diluc"],
["Chongyun", "Diona", "Rosaria", "Beidou", "Razor", "Ningguang", "Noelle", "Xingqiu", "Bennett", "Xiangling", "Xinyan", "Yanfei"],
["Favonius Warbow", "Rust", "Sacrificial Bow", "The Stringless", "Eye of Perception", "Favonius Codex", "Sacrificial Fragments", "The Widsith", "Favonius Greatsword", "Rainslasher", "Sacrificial Greatsword", "The Bell", "Dragon's Bane", "Favonius Lance", "Favonius Sword", "Lion's Roar", "Sacrificial Sword", "The Flute"],
["Raven Bow", "Sharpshooter's Oath", "Slingshot", "Emerald Orb", "Magic Guide", "Thrilling Tales of Dragon Slayers", "Bloodtainted Greatsword", "Debate Club", "Ferrous Shadow", "Black Tassel", "Cool Steel", "Harbinger of Dawn", "Skyrider Sword"])

leaves_in_the_wind_1 = CharacterBanner(
"Leaves in the Wind",
"06-29-2021",
"07-20-2021",
["Kazuha"],
["Rosaria", "Bennett", "Razor"],
["Jean","Qiqi","Keqing","Mona","Diluc"],
["Sucrose", "Chongyun", "Diona", "Beidou", "Fischl", "Ningguang", "Noelle", "Barbara", "Xingqiu", "Xiangling", "Xinyan", "Yanfei"],
["Favonius Warbow", "Rust", "Sacrificial Bow", "The Stringless", "Eye of Perception", "Favonius Codex", "Sacrificial Fragments", "The Widsith", "Favonius Greatsword", "Rainslasher", "Sacrificial Greatsword", "The Bell", "Dragon's Bane", "Favonius Lance", "Favonius Sword", "Lion's Roar", "Sacrificial Sword", "The Flute"],
["Raven Bow", "Sharpshooter's Oath", "Slingshot", "Emerald Orb", "Magic Guide", "Thrilling Tales of Dragon Slayers", "Bloodtainted Greatsword", "Debate Club", "Ferrous Shadow", "Black Tassel", "Cool Steel", "Harbinger of Dawn", "Skyrider Sword"])

the_herons_court_1 = CharacterBanner(
"The Heron's Court",
"07-21-2021",
"08-10-2021",
["Ayaka"],
["Ningguang", "Chongyun", "Yanfei"],
["Jean","Qiqi","Keqing","Mona","Diluc"],
["Sucrose", "Diona", "Rosaria", "Beidou", "Fischl", "Razor", "Noelle", "Barbara", "Xingqiu", "Bennett", "Xiangling", "Xinyan"],
["Favonius Warbow", "Rust", "Sacrificial Bow", "The Stringless", "Eye of Perception", "Favonius Codex", "Sacrificial Fragments", "The Widsith", "Favonius Greatsword", "Rainslasher", "Sacrificial Greatsword", "The Bell", "Dragon's Bane", "Favonius Lance", "Favonius Sword", "Lion's Roar", "Sacrificial Sword", "The Flute"],
["Raven Bow", "Sharpshooter's Oath", "Slingshot", "Emerald Orb", "Magic Guide", "Thrilling Tales of Dragon Slayers", "Bloodtainted Greatsword", "Debate Club", "Ferrous Shadow", "Black Tassel", "Cool Steel", "Harbinger of Dawn", "Skyrider Sword"])

tapestry_of_golden_flames_1 = CharacterBanner(
"Tapestry of Golden Flames",
"08-10-2021",
"08-31-2021",
["Yoimiya"],
["Sayu", "Diona", "Xinyan" ],
["Jean","Qiqi","Keqing","Mona","Diluc"],
["Sucrose", "Chongyun", "Rosaria", "Beidou", "Fischl", "Razor", "Ningguang", "Noelle", "Barbara", "Xingqiu", "Bennett", "Xiangling", "Yanfei"],
["Favonius Warbow", "Rust", "Sacrificial Bow", "The Stringless", "Eye of Perception", "Favonius Codex", "Sacrificial Fragments", "The Widsith", "Favonius Greatsword", "Rainslasher", "Sacrificial Greatsword", "The Bell", "Dragon's Bane", "Favonius Lance", "Favonius Sword", "Lion's Roar", "Sacrificial Sword", "The Flute"],
["Raven Bow", "Sharpshooter's Oath", "Slingshot", "Emerald Orb", "Magic Guide", "Thrilling Tales of Dragon Slayers", "Bloodtainted Greatsword", "Debate Club", "Ferrous Shadow", "Black Tassel", "Cool Steel", "Harbinger of Dawn", "Skyrider Sword"])

reign_of_serenity_1 = CharacterBanner(
"Reign of Serenity",
"09-01-2021",
"09-21-2021",
["Raiden"],
["Kujou Sara", "Xiangling", "Sucrose"],
["Jean","Qiqi","Keqing","Mona","Diluc"],
["Sayu", "Chongyun", "Diona", "Rosaria", "Beidou", "Fischl", "Razor", "Ningguang", "Noelle", "Barbara", "Xingqiu", "Bennett", "Xinyan", "Yanfei"],
["Favonius Warbow", "Rust", "Sacrificial Bow", "The Stringless", "Eye of Perception", "Favonius Codex", "Sacrificial Fragments", "The Widsith", "Favonius Greatsword", "Rainslasher", "Sacrificial Greatsword", "The Bell", "Dragon's Bane", "Favonius Lance", "Favonius Sword", "Lion's Roar", "Sacrificial Sword", "The Flute"],
["Raven Bow", "Sharpshooter's Oath", "Slingshot", "Emerald Orb", "Magic Guide", "Thrilling Tales of Dragon Slayers", "Bloodtainted Greatsword", "Debate Club", "Ferrous Shadow", "Black Tassel", "Cool Steel", "Harbinger of Dawn", "Skyrider Sword"])

drifting_luminescence_1 = CharacterBanner(
"Drifting Luminescence",
"09-21-2021",
"10-12-2021",
["Kokomi"],
["Rosaria", "Beidou", "Xingqiu"],
["Jean","Qiqi","Keqing","Mona","Diluc"],
["Sayu", "Sucrose", "Chongyun", "Diona", "Fischl", "Razor", "Ningguang", "Noelle", "Barbara", "Bennett", "Xiangling", "Xinyan", "Yanfei"],
["Favonius Warbow", "Rust", "Sacrificial Bow", "The Stringless", "Eye of Perception", "Favonius Codex", "Sacrificial Fragments", "The Widsith", "Favonius Greatsword", "Rainslasher", "Sacrificial Greatsword", "The Bell", "Dragon's Bane", "Favonius Lance", "Favonius Sword", "Lion's Roar", "Sacrificial Sword", "The Flute"],
["Raven Bow", "Sharpshooter's Oath", "Slingshot", "Emerald Orb", "Magic Guide", "Thrilling Tales of Dragon Slayers", "Bloodtainted Greatsword", "Debate Club", "Ferrous Shadow", "Black Tassel", "Cool Steel", "Harbinger of Dawn", "Skyrider Sword"])

farewell_of_snezhnaya_3 = CharacterBanner(
"Farewell of Snezhnaya",
"10-13-2021",
"11-02-2021",
["Tartaglia"],
["Ningguang", "Chongyun", "Yanfei"],
["Jean","Qiqi","Keqing","Mona","Diluc"],
["Sayu", "Sucrose", "Diona", "Rosaria", "Beidou", "Fischl", "Kujou Sara", "Razor", "Noelle", "Barbara", "Xingqiu", "Bennett", "Xiangling", "Xinyan"],
["Favonius Warbow", "Rust", "Sacrificial Bow", "The Stringless", "Eye of Perception", "Favonius Codex", "Sacrificial Fragments", "The Widsith", "Favonius Greatsword", "Rainslasher", "Sacrificial Greatsword", "The Bell", "Dragon's Bane", "Favonius Lance", "Favonius Sword", "Lion's Roar", "Sacrificial Sword", "The Flute"],
["Raven Bow", "Sharpshooter's Oath", "Slingshot", "Emerald Orb", "Magic Guide", "Thrilling Tales of Dragon Slayers", "Bloodtainted Greatsword", "Debate Club", "Ferrous Shadow", "Black Tassel", "Cool Steel", "Harbinger of Dawn", "Skyrider Sword"])

moment_of_bloom_2 = CharacterBanner(
"Moment of Bloom",
"11-02-2021",
"11-23-2021",
["Hu Tao"],
["Thoma", "Diona", "Sayu"],
["Jean","Qiqi","Keqing","Mona","Diluc"],
["Sucrose", "Chongyun", "Rosaria", "Beidou", "Fischl", "Kujou Sara", "Razor", "Ningguang", "Noelle", "Barbara", "Xingqiu", "Bennett", "Xiangling", "Xinyan", "Yanfei"],
["Favonius Warbow", "Rust", "Sacrificial Bow", "The Stringless", "Eye of Perception", "Favonius Codex", "Sacrificial Fragments", "The Widsith", "Favonius Greatsword", "Rainslasher", "Sacrificial Greatsword", "The Bell", "Dragon's Bane", "Favonius Lance", "Favonius Sword", "Lion's Roar", "Sacrificial Sword", "The Flute"],
["Raven Bow", "Sharpshooter's Oath", "Slingshot", "Emerald Orb", "Magic Guide", "Thrilling Tales of Dragon Slayers", "Bloodtainted Greatsword", "Debate Club", "Ferrous Shadow", "Black Tassel", "Cool Steel", "Harbinger of Dawn", "Skyrider Sword"])

def display_all_character_banners():
	for banner in CharacterBanner.character_banners:
		print(f"[{CharacterBanner.character_banners.index(banner)}] -", end=" ")
		banner.display_banner_name()

# display_all_character_banners()
