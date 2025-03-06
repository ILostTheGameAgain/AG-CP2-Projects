#Alec George Battle Simulator

#profile management, will save/load to csv file
import csv

#import small functions
from small_functions import *

#function to create a profile, takes a name and gives them basic stats
def add_profile(name, attack, defense, health):
    with open("battle_simulator/character_info.csv","a") as file:
        file.write(f"{name}, {attack}, {defense}, {health}\n")





#function to add new profile
def new_profile():
    name = input("\nwhat is the name? ")
    attack = is_int(input("\nwhat is the attack? "))
    defense = is_int(input("\nwhat is the defense? "))
    health = is_int(input("\nwhat is the health? "))
    add_profile(name,attack,defense,health)


new_profile()