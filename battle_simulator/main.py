#Alec George Battle simulator

#will allow users to save info and battle each other
#profiles will have stats including level, xp, attack, defense, etc.
#user can create new character or battle other characters

#import functions from other pages to run on main
from guide import main as guide


#main function, runs other functions
def main():
    while True:
        #ask user what to do
        choice = input("""
Welcome to battle simulator!
What would you like to do? Type:
1 to battle someone else
2 to manage/create a profile
3 to learn what you're doing
4 to exit""")
        #do things depending on what the user chose
        if choice == "1":
            pass

        elif choice == "2":
            pass

        elif choice == "3":
            guide()

        elif choice == "4":
            break

        else: #stupid proof
            print("\ninvalid input")