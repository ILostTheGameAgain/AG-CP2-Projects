# Alec George Classes notes

class clasz:
    def __init__(self, content, peroid, teacher, room):
        self.content = content
        self.peroid = peroid
        self.teacher = teacher
        self.room = room

    def __str__(self):
        return f"Name: {self.content}\nPeroid: {self.peroid}\nTeacher: {self.teacher}\nRoom: {self.room}"


first = clasz("CS PRINCIPLES", 1, "LaRose", 200)
second = clasz("CP2", 2, "LaRose", 200)

print(first)


class pokemon:
    def __init__(self, name, species, hp, dmg):
        self.name = name
        self.species = species
        self.hp = hp
        self.dmg = dmg

    def __str__(self):
        return f"{self.name} is a {self.tipe} and they have {self.hp} HP and do {self.dmg} amount of damage in battle."
    
    def battle(self, opponent):
        while self.hp > 0 and opponent.hp > 0:
            opponent.hp -= self.dmg
            print(f"{self.name} attacked {opponent.name} for {self.dmg}. {opponent.name} now has {opponent.hp} HP")

            if opponent.hp <= 0:
                print(f"{opponent.name} is DEAD. {self.name} wins")
            else:
                self.hp -= opponent.dmg
            print(f"{opponent.name} attacked {self.name} for {opponent.dmg}. {self.name} now has {opponent.hp} HP")

            if self.hp <= 0:
                print(f"{self.name} is DEAD. {opponent.name} wins")

fluffy = pokemon("Fluffy", "Arcanine", 280, 110)
slimy = pokemon("Slimy", "Ditto", 100, 70)
spiky = pokemon("Spiky", "Jolteon", 150, 100)
goat = pokemon("GOAT", "GOAT", 9999999999999,999999999999)

fluffy.battle(goat)


#What is a class in python?
    #A class is a blueprint for an object. It can contain methods, variables, etc.

#What is an object in python?
    #An object is a specific instance of a class

#How do python classes relate to python objects?
    #python classes are what decides the variables and methods of an object

#How do you create a python class?
    #Basic requirements
class name:
    def __init__(self):
        pass


#What are methods?
    #a function that exists for a specific class

#How do you create a python object?
var_name = name()

#How to you call a method for an object?
    #make a functoin in the class

#Why do we use python classes?
    #they allow you to make multiple objects with similar properties but different values