#Alec George Battle Simulator

#page for actual battling

#needs small functions
from small_functions import *

#will have some randomness
import random

#function to display profiles with a number
def display_profiles(profiles):
    profile_list = ""
    for i, profile in enumerate(profiles):
        profile_list += f"\n{i+1} - Level {profile["level"]} {profile["name"]}"

    return profile_list
        

#function to select 2 profiles and return their stats
def select_profiles(profiles):
    print(f"\nprofiles:{display_profiles(profiles)}")
    #select 2 profiles
    profile_1 = profiles[is_in_range(is_int(input("type the number of the profile "))-1, 1, len(profiles))-1]
    profile_2 = profiles[is_in_range(is_int(input("type the number of the profile "))-1, 1, len(profiles))-1]


    return profile_1, profile_2



#function for battling, turn based, but automatic with commentary
def main():
    #put profiles in a list
    profiles = list_profiles()
    #only work if there are more than 2 profiles
    if len(profiles) < 2:
        cs()
        print("\nnot enough profiles\n")
        return
    
    #select 2 profiles
    profile_1, profile_2 = select_profiles(profiles)



main()