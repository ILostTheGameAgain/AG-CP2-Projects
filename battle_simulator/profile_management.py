#Alec George Battle Simulator

#profile management, will save/load to csv file
import csv

#import small functions
from small_functions import *

#function to create a profile, takes a name and gives them basic stats
def add_profile(name, attack, defense):
    with open("battle_simulator/character_info.csv","a") as file:
        fieldnames = ["name", "attack", "defense"]
        csv_writer = csv.writer(file)
        csv_writer.write(name, attack, defense)


add_profile("e", 100, 10)