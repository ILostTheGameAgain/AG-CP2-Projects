#Alec George Battle Simulator

#functions to explain what to do


#function to explain stats
def stat_explain():
    pass


#function to explain combat
def combat_explain():
    pass


#function to explain mechanics/leveling
def leveling_explain():
    pass


#main function to explain most things and call other functions
def main():
    while True:
        #display information and ask the user what to do
        print("""
Welcome to Battle Simulator!
This is a school project made by Alec
What would you like to learn about? Type:
1 to learn about stats and what they do
2 to learn about how combat works
3 to learn about leveling and related mechanics
4 to exit the guide
Your answer here:
""")
        choice = input()
        if choice == "1":
            stat_explain()

        elif choice == "2":
            combat_explain()

        elif choice == "3":
            leveling_explain()

        elif choice == "4":
            break

        else: #stupid proof
            print("\ninvalid input")