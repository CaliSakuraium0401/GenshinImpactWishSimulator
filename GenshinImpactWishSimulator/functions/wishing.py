import os
import random
import numpy as np
import pandas as pd
import datetime as dt
import time
import pygame

character_path = "GenshinImpactWishSimulator\data\characters.csv"
character_data = pd.read_csv(character_path)
# character_list = character_data.to_dict()

class COLOR:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   END = '\033[0m'

class EMPHASIZE:
   ITALIC = "\x1B[3m"
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   BOLD_UNDERLINE = '\033[1;4m'
   END = '\033[0m'

def query_standard_pool(character_data, filter=True):
    # Filters (queries) the data so that non-standard five star characters 
    # won't be in the wishing pool. This also includes the starter characters,
    # the traveler, and other outlanders such as Aloy.
    return character_data.query(f'`Standard Pool` == {filter}')

def query_version(character_data, d_version):
    #Filters (queries) the data so that only characters released on and below
    # the d(esired) version are available.
    return character_data.query('Version <= @d_version')

def get_banner_data(character_data, d_version, date=None):
    # Filters (queries) the character data to exclude five stars and non standard four star
    # characters. Also filters (queries) to exclude characters from future versions 
    # (if applicable).
    standard_four_star_character_banner_data = character_data.query("Rarity == 4")
    standard_four_star_character_banner_data = query_standard_pool(standard_four_star_character_banner_data)
    standard_four_star_character_banner_data = standard_four_star_character_banner_data.query(f"Version <= {d_version}")
    
    # Creates a seperate filter (queries) for the promotional five star.
    promotional_five_star_character_banner_data = character_data.query(f"Version == {d_version}")
    promotional_five_star_character_banner_data = promotional_five_star_character_banner_data.query("Rarity == 5")
    
    # Combines both filtered (queryed) dataframes so that includes the promotional five star
    # character and the four stars in the wishing pull.
    character_banner_data = pd.concat([promotional_five_star_character_banner_data, standard_four_star_character_banner_data])
    
    return character_banner_data

def get_standard_five_stars(character_data, d_version):
    standard_5_star_character_data = query_standard_pool(character_data)
    standard_5_star_character_data = standard_5_star_character_data.query(f'`Rarity` == 5')
    return standard_5_star_character_data

# Example / testing code.


def roll(pity,five_star_probability = 0.006, four_star_probability = 0.051, three_star_probability = 0.943):
            
 
    if pity % 10 == 0:
        four_star_probability = 1
    if pity >= 74:
        five_star_probability = abs(0.061* (((90-pity)) - 17))
    if pity == 90 and pity % 5 == 10:
        five_star_probability = 1
        four_star_probability = 0
        three_star_probability = 0
    #print(f"#Pull {pulls} | Five Star Chance : {five_star_probability*100:.1f}%")
    
    rarity = [5, 4, 3]
    probabilities = [five_star_probability, four_star_probability, three_star_probability]

    return random.choices(rarity, probabilities)[0]


chanson_of_many_waters_data = get_banner_data(character_data, 4.2)

chanson_of_many_waters_four_star_data = chanson_of_many_waters_data.query(f'`Rarity` == 4')
chanson_of_many_waters_five_star_data = chanson_of_many_waters_data.query(f'`Rarity` == 5')

chanson_of_many_waters_four_stars = chanson_of_many_waters_four_star_data["Name"].to_numpy()
chanson_of_many_waters_five_stars = chanson_of_many_waters_five_star_data["Name"].to_numpy()
chanson_of_many_waters_standard_five_stars = get_standard_five_stars(character_data, 4.2)["Name"].to_numpy()



def open_program():
    pulled = 0
    pity = 0
    pulls = 0
    window_width = 1344
    window_height = 756
    guranteed = False
    
    wish_count = int(input("Wishes: "))
    pity = int(input("Pity: "))

    pygame.init()
    game_display = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption('Genshin Impact Wish Simulator')
    bg_image = pygame.image.load('GenshinImpactWishSimulator/images/background.png')

    pulled_characters = []

    for wish in range(wish_count):
        pity += 1
        pulled = roll(pity)
        pulls += 1
        if pulled == 5:
            if guranteed == False:
                if random.choice(["Win", "Lose"]) == "Win":
                    pulled_character = random.choice(chanson_of_many_waters_five_stars)
                    pity = 0
                    guranteed = False
                else:
                    pulled_character = random.choice(chanson_of_many_waters_standard_five_stars)
                    guranteed = True
            else:
                pulled_character = random.choice(chanson_of_many_waters_five_stars)
                guranteed = False
        elif pulled == 4:
            pulled_character = random.choice(chanson_of_many_waters_four_stars)
        elif pulled == 3:
            pulled_character = random.choice(chanson_of_many_waters_four_stars)

        pulled_characters.append(pulled_character)

    for character in pulled_characters:
        char_image = pygame.image.load(f'GenshinImpactWishSimulator/images/characters/{character}.png')
        char_image = pygame.transform.scale(char_image, (window_width, 672))
        
        # Display the background and character image
        game_display.blit(bg_image, (0, 0))
        game_display.blit(char_image, (window_width / 2 - window_width / 2, window_height / 2 - 672 / 2))
        pygame.display.update()
        
        time.sleep(1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
    pygame.quit()

open_program()



# for wish in range(wish_count):
#     pity += 1
#     pulled = roll(pity)
#     pulls += 1
#     if pulled == 5:
#         time.sleep(1)
#         if guranteed == False:
#             if random.choice(["Win","Lose"]) == "Win":
#                 pulled_five_star = random.choice(chanson_of_many_waters_five_stars)
#                 guranteed = False
#             else: 
#                 pulled_five_star = random.choice(chanson_of_many_waters_standard_five_stars)
#                 guranteed = True
#         else:
#             pulled_five_star = random.choice(chanson_of_many_waters_five_stars)
#             guranteed = False   
#         five_stars.append(pulled_five_star)
#         pity = 0
#         print(f"{COLOR.YELLOW}5★ | {pulled_five_star}{COLOR.END}")
#     elif pulled == 4:
#         print(f"{COLOR.PURPLE}4★ | {random.choice(chanson_of_many_waters_four_stars)}{COLOR.END}")
#     elif pulled == 3:
#         print(F"{COLOR.DARKCYAN}3★ | {random.choice(["Harbinger of Dawn", "Black Tassel", "Thrilling Tales of Dragon Slayers", "Slingshot"])}{COLOR.END}")
# print(f"Pulled {five_stars} in {pulls} pulls.")


