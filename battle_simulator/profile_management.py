#Alec George Battle Simulator

#profile management, will save/load to csv file
import csv

#import small functions
from small_functions import *








#main function to manage profiles
def main():

    #list of profiles, comes from folder
    profiles = []
    with open("battle_simulator/character_info.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for profile in reader:
            profiles.append({"name": profile[0], "attack": profile[1], "defense": profile[2], "health": profile[3], "speed": profile[4], "level": profile[5], "xp": profile[6]})


    #function to add new profile
    def new_profile():
        #ask for information
        name = input("\nwhat is the name? ")
        attack = is_int(input("\nwhat is the attack? "))
        defense = is_int(input("\nwhat is the defense? "))
        health = is_int(input("\nwhat is the health? "))
        speed = is_int(input("\nwhat is the speed? "))

        #add to the list of profiles
        profiles.append({"name": name, "attack": attack, "defense": defense, "health": health, "speed": speed, "level": 1, "xp": 0})


    #function to edit a profile
    def edit_profile(profile):


    
    #after all stuff, rewrite the file with updates
    with open("battle_simulator/character_info.csv", "w", newline='') as file:
        fieldnames = ["name", "attack", "defense", "health", "speed", "level", "xp"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(profiles)
    

    
main()