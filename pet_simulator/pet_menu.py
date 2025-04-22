#Alec George pet simulator

#menu for pet interactoins
from used_everywhere import *

def main(thing):
    cs()
    new_money = 0
    while True:
        choice = is_int(input('''What would you like to do? Type:
1 to play with your pet
2 to feed your pet a meal
3 to feed your pet a snack
4 to feed your pet a treat
5 to explore with your pet
6 to put your pet to sleep
7 to exit
Your answer here:
'''))
        
        if choice == 1:
            cs()
            print(thing.play())

        elif choice == 2:
            cs()
            print(thing.meal())

        elif choice == 3:
            cs()
            print(thing.snack())

        elif choice == 4:
            cs()
            print(thing.treat())

        elif choice == 5:
            cs()
            string, money = thing.explore()
            print(string)
            new_money += money

        elif choice == 6:
            cs()
            print(thing.sleep())

        elif choice == 7:
            break

        else:
            continue

        thing.change()
        print(thing.check())
        print(thing.display())

    return new_money