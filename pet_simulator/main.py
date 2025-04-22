# Alec George pet simulator

#main functoin and stuff

from used_everywhere import *
from pet_menu import main as pet_menu


def main():
    #list of pets
    pets = {}

    #variable for coins
    coins = 0

    while True:
        cs()
        #print directoins
        choice = is_int(input('''What would you like to do? type:
1 to create a pet
2 to access/do things with a pet
3 to view all your pets
4 to view specific pet stats
5 to exit
Type your answer here:
'''))
        cs()
        if choice == 1:
            name = is_long(input("what is the pet's name? "))
            if name not in pets.keys():
                species = is_long(input(f"what is {name}'s species? "))
                pets[name] = pet(name, species, 0, 20, 3, 0, 0, 1)
                print("\ncreated pet")

            else:
                print("\na pet already has that name.\n")
            pause()

        elif choice == 2:
            cs()
            #only interact if more than 1 pet
            if len(pets) > 0:
                selected_pet = input("what is the name of the pet you're interacting with (to go back, type nothing)? ")
                if selected_pet == "":
                    continue


                #make sure it is a pet
                if selected_pet in pets.keys():
                    coins += pet_menu(pets[selected_pet])

                else:
                    print("\nthat pet does not exist.\n")
            else:
                print("\nYou need at least 1 pet before interacting.\n")

            pause()

        elif choice == 3:
            cs()
            print("Current pets:\n")
            for i in pets.values():
                print(i)

            pause()

        elif choice == 4:
            cs()
            #only interact if more than 1 pet
            if len(pets) > 0:
                selected_pet = input("what is the name of the pet you're viewing? (to go back, type nothing)? ")
                if selected_pet == "":
                    continue

                #make sure it is a pet
                if selected_pet in pets.keys():
                    selected_pet = pets[selected_pet]
                    print(selected_pet.specific_stats())

                else:
                    print("\nthat pet does not exist.\n")
            else:
                print("\nYou need at least 1 pet before viewing.\n")

            pause()


        elif choice == 5:
            break

        else:
            print("\ninvalid input\n")
            pause()

        #delete dead pets
        dead_pets = []
        for i in pets:
            if pets[i].is_dead():
                dead_pets.append(i)

        for i in dead_pets:
            pets.pop(i)

main()