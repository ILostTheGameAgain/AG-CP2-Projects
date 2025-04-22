# Alec George Pet Simulator
#functoins and classes that will possibly be used everywhere

import random


def cs():
    print('\033c')


def is_int(value):
    try:
        int(value)

    except:
        value = is_int(input("\nthat is not an integer. Try again:\n"))

    return int(value)


class pet:
    def __init__(self, name, species, hunger, happiness, tired, sick, age, alive):
        self.name = name
        self.species = species
        self.hunger = hunger
        self.happiness = happiness
        self.tired = tired
        self.sick = sick
        self.age = age
        self.alive = alive



    #functoin to display information
    def display(self):
        returned_string = ''
        if self.hunger > 0 and self.hunger < 5:
            returned_string += f"\n{self.name} is hungry."
        elif self.hunger >= 5:
            returned_string += f"\n{self.name} is starving."

        if self.tired >= 3:
            returned_string += f"\n{self.name} is tired."

        if self.happiness <= 10:
            returned_string += f"\n{self.name} is depressed."

        if self.sick > 0:
            returned_string += f"\n{self.name} has been sick for {self.sick} days now."

        if self.alive <= 0:
            returned_string += f"\n{self.name} is dead."
        
        return returned_string


    
    def __str__(self):
        returned_string = f"""\n{self.name} is a {self.species}.
{self.name} has a happiness value of {self.happiness}.
{self.name} has been alive for {self.age} days now."""
        returned_string += self.display()

        return returned_string
    

    #check multiple things, making sure the pet is still alive
    def check(self):
        if self.hunger >= 7:
            self.alive = 0
            return f"{self.name} starved.\n{self.name} is now dead."
        
        if self.hunger <= -3:
            self.alive = 0
            return f"{self.name} was overfed.\n{self.name} is now dead."
        
        if self.happiness <= 0:
            self.alive = 0
            return f"{self.name} became too depressed.\n{self.name} is now dead."
        
        if self.tired >= 6:
            self.alive = 0
            return f"{self.name} was overworked.\n{self.name} is now dead."
        
        if self.tired <= 4:
            self.alive = 0
            return f"{self.name} had too much energy.\n{self.name} is now dead."
        
        if self.sick >= 5:
            self.alive = 0
            return f"{self.name} got too sick.\n{self.name} is now dead."
        


    #functoin to update things
    def change(self):
        if self.sick >= 1:
            self.sick += 1

        self.happiness -= self.sick + 2

        self.tired -= 2

        self.hunger += 1

        self.age += 1

    #functoin to play with pet
    def play(self):
        returned_string = f"You played with {self.name}. They are happier now."
        self.happiness += 10
        self.tired += 1

        if self.sick == 0 and random.randint(1,10) == 1:
            self.sick = 1
            returned_string += f"\nWhile playing, {self.name} got sick."

        self.hunger += random.randint(0,1)

        return returned_string
        

    #functoin to feed the pet a meal
    def meal(self):
        returned_string = f"You fed {self.name} a well-rounded meal. They are much less hungry."
        self.hunger -= 5
        self.tired += 2

        happiness_change = random.randint(-3,5)
        self.happiness += happiness_change
        if happiness_change >= 0:
            returned_string += f"\n{self.name} liked the meal. Their happiness increased."

        elif happiness_change < 0:
            returned_string += f"\n{self.name} didn't like the meal. Their happiness decreased."

        if self.sick == 0 and random.randint(1,50) == 1:
            self.sick = 1
            returned_string += f"\nEating the meal made {self.name} sick."

        return returned_string

        
    #functoin to feed the pet a snack
    def snack(self):
        returned_string = f"You fed {self.name} a quick snack. They are less hungry."
        self.hunger -= 3
        self.tired += 1

        happiness_change = random.randint(-2,7)
        self.happiness += happiness_change
        if happiness_change >= 0:
            returned_string += f"\n{self.name} liked the snack. Their happiness increased."

        elif happiness_change < 0:
            returned_string += f"\n{self.name} didn't like the snack. Their happiness decreased."

        if self.sick == 0 and random.randint(1,30) == 1:
            self.sick = 1
            returned_string += f"\nEating the snack made {self.name} sick."

        return returned_string
    

    #functoin to feed the pet a treat
    def treat(self):
        returned_string = f"You fed {self.name} a delicious treat. They are slightly less hungry."
        self.hunger -= 1

        happiness_change = random.randint(-1,10)
        self.happiness += happiness_change
        if happiness_change >= 0:
            returned_string += f"\n{self.name} liked the treat. Their happiness increased."

        elif happiness_change < 0:
            returned_string += f"\n{self.name} didn't like the treat. Their happiness decreased."

        if self.sick == 0 and random.randint(1,15) == 1:
            self.sick = 1
            returned_string += f"\nEating the treat made {self.name} sick."

        return returned_string
    

    #functoin to go explore with the pet
    def explore(self):
        money_amount = random.randint(0,10)
        returned_string = f"You went exploring with {self.name}. Together, you found {money_amount} coins."

        self.hunger += 3
        self.tired += 3
        self.happiness += random.randint(5,15)

        if self.sick == 0 and random.randint(1,5) == 1:
            self.sick = 1
            returned_string += f"\nWhile exploring, {self.name} got sick."

        if random.randint(1,100) == 1:
            self.alive = 0
            returned_string += f"{self.name} took a wrong step and fell off a cliff.\n{self.name} is now dead."

        return returned_string, money_amount
    

    #functoin to let the pet sleep
    def sleep(self):
        #only sleep if the pet is tired enough
        if self.tired <= 2:
            returned_string = f"{self.name} is too energetic to sleep right now."

        else:
            returned_string = f"{self.name} went to sleep."
            self.tired -= 3
            self.hunger += 1
            self.happiness += 1

            if self.sick > 0 and random.randint(1,2) == 1:
                returned_string += f"\n{self.name} recovered from the sickness."
                self.sick = 0


        return returned_string

