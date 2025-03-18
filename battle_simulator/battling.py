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
        

#function to handle combat turns
def combat(p1, p2):
    commentary = "" #commentary string to explain what happens
    #randomly assign who goes first
    if random.randint(1,2) == 1:
        commentary += "\nPlayer 1 starts"
        turn = 1

    else:
        commentary += "\nPlayer 2 starts"
        turn = 2

    #repeat combat until one is defeated
    while p1["health"] > 0 and p2["health"] > 0:
        #if turn is 1, player one goes
        if turn == 1:
            damage = p1["strength"] + random.randint(-p1["strength"]//4,p1["strength"]//4)
            defense = random.randint(p2["defense"]//2,p2["defense"])
            #subtract defense from damage
            damage -= defense
            dodge = random.randint(0,p2["speed"])-p1["speed"]

            #check if damage is less than 0
            if damage < 0:
                damage = 0

            #check if dodge is positive
            if dodge > 0:
                damage = 0
                #add commentary
                commentary += "Player 2 dodged"

            else:
                #add commentary
                commentary += f"\nPlayer 1 did {damage} damage, player 2 blocked {defense} damage."

            #subtract damage from health
            p2["health"] -= damage
            commentary += f" Player 2 is now at {p2["health"]} health."


        #if turn is 2, player two goes
        elif turn == 2:
            damage = p2["strength"] + random.randint(-p2["strength"]//4,p2["strength"]//4)
            defense = random.randint(p1["defense"]//2,p1["defense"])
            #subtract defense from damage
            damage -= defense
            dodge = random.randint(0,p1["speed"])-p2["speed"]

            #check if damage is less than 0
            if damage < 0:
                damage = 0

            #check if dodge is positive
            if dodge > 0:
                damage = 0
                #add commentary
                commentary += "Player 1 dodged"

            else:
                #add commentary
                commentary += f"\nPlayer 2 did {damage} damage, player 1 blocked {defense} damage."

            #subtract damage from health
            p1["health"] -= damage
            commentary += f" Player 1 is now at {p1["health"]} health."

        #switch turns
        turn = (turn+1)%2

    #decide winner
    if p1["health"] < 0:
        return 2, commentary
    
    else:
        return 1, commentary





#function to select 2 profiles and return their stats
def select_profiles(profiles):
    print(f"\nprofiles:{display_profiles(profiles)}")
    #select 2 profiles

    index_1 = is_in_range(is_int(input("type the number of the profile "))-1, 0, len(profiles))-1
    index_2 = is_in_range(is_int(input("type the number of the profile "))-1, 0, len(profiles))-1
    profile_1 = profiles[index_1]
    profile_2 = profiles[index_2]


    return profile_1, profile_2, index_1, index_2



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
    profile_1, profile_2, index_1, index_2 = select_profiles(profiles)
    
    #do combat
    winner, commentary = combat(profile_1, profile_2)
    print(commentary)
    input("\ntype anything to move on")
    cs()
    #winner gets levels
    if winner == 1:
        profiles[index_1]["level"] += 1

    else:
        profiles[index_2]["level"] += 1

    #save profiles
    save_profiles(profiles)
