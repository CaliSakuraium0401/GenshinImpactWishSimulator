import os
import numpy as np
import pandas as pd
import datetime as dt

character_path = "GenshinImpactWishSimulator\data\characters.csv"
character_data = pd.read_csv(character_path)
character_list = character_data.to_dict()

#class bannerInformation:
#    def __init__(self, character_list):
#        self.character_list = character_list
#    def print_characters(self):
#        print(self.character_list)

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
    banner_data = query_standard_pool(character_data)
    banner_data = query_version(banner_data, d_version)
    
    # Note: reminder to add functionality that excludes the promotional character by the date.
    
    # Note: reminder to add functionality that filters by date.
    
    return banner_data

# Example / testing code.
# chanson_of_many_waters = get_banner_data(character_data, 4.2)
# print(chanson_of_many_waters)