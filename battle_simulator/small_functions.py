#Alec George Battle Simulator

#page with some small quality of life functions

#needs csv things
import csv

#for graphing, needs matplotlib
import matplotlib.pyplot as plt
import numpy as np

#function to clear screen
def cs():
    print("\033c")


#function for exception handling (integers)
def is_int(value):
    try:
        int(value)

    except:
        value = is_int(input("\nPlease input an integer.\n"))
    return int(value)


#function to check if a number is in a range
def is_in_range(value, min, max):
    value = is_int(value)

    if value < min or value > max:
        value = is_in_range("\ninvalid input, try again.\n", min, max)
    return value


#function to check if something is unique in a list
def is_unique(list, value):

    #check every value in the list
    for item in list:
        if item == value:
            value = is_unique(list, input("\nThat item already exists. Choose something else.\n"))
            
    return value



#function to check if something is in a list
def is_in_list(list, value):
    for index in range(len(list)):
        if list[index] == value:
            return index+1 #add one so it isn't considered false
        
    return False


#function to put all profiles in a list
def list_profiles():
    #list of profiles, comes from folder
    profiles = []
    with open("battle_simulator/character_info.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for profile in reader:
            profiles.append({"name": profile[0], "strength": int(profile[1]), "defense": int(profile[2]), "health": int(profile[3]), "speed": int(profile[4]), "level": int(profile[5])})

    return profiles


#function to put profiles list into csv
def save_profiles(profiles):
    with open("battle_simulator/character_info.csv", "w", newline='') as file:
        fieldnames = ["name", "strength", "defense", "health", "speed", "level"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(profiles)


#function to display a bar graph of values
def graph(values, titles):
    plt.bar(titles, values)

    plt.show()