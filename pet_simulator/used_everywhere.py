# Alec George Pet Simulator
#functoins and classes that will possibly be used everywhere

import random


class pet:
    def __init__(self, name, species, hunger, happiness, tired, sick, alive):
        self.name = name
        self.species = species
        self.hunger = hunger
        self.happiness = happiness
        self.tired = tired
        self.sick = sick
        self.alive = alive


    def __str__(self):
        returned_string = f"""\n{self.name} is a {self.species}.
{self.name} has a happiness value of {self.happiness}."""
        
        #add additional things to the string
        
        if self.hunger > 0 and self.hunger < 5:
            returned_string += f"\n{self.name} is hungry."
        elif self.hunger >= 5:
            returned_string += f"\n{self.name} is starving."

        if self.tired >= 3:
            returned_string += f"\n{self.name} is tired."

        if self.happiness <= 10:
            returned_string += f"\n{self.name} is depressed."

        if self.sick > 0:
            returned_string += f"\n{self.name} has been sick for {self.sick} units of time now."

        if self.alive == 0:
            returned_string += f"\n{self.name} is DEAD."

        return returned_string
    

    #check multiple things, making sure the pet is still alive
    def check(self):
        if self.hunger >= 7:
            self.alive = 0
            return f"{self.name} starved.\n{self.name} is now DEAD."
        
        if self.hunger <= -3:
            self.alive = 0
            return f"{self.name} was overfed.\n{self.name} is now DEAD."
        
        if self.happiness <= 0:
            self.alive = 0
            return f"{self.name} became too depressed.\n{self.name} is now DEAD."
        
        if self.tired >= 6:
            self.alive = 0
            return f"{self.name} was overworked.\n{self.name} is now DEAD."
        
        if self.tired <= 4:
            self.alive = 0
            return f"{self.name} had too much energy.\n{self.name} is now DEAD."
        
        if self.sick >= 5:
            self.alive = 0
            return f"{self.name} got too sick.\n{self.name} is now DEAD."
        

    

    #functoin to play with pet, makes them happy, but also tired and hungry and have a chance to get sick
    def play(self):
        self.happiness += 10
        self.tired += 1
        if self.sick == 0 and random.randint(1,10) == 1:
            self.sick = 1

        self.hunger += random.randint(0,1)
        

