#Alec George Random Password Generator

#will let the user specify the length, amount of uppercase letters, amount of lowercase letters, number of numbers, number of special characters, and give the user 4 options
#to generate random passwords, will need to import random
import random


#function for adding uppercase letters, takes the password and adds a random uppercase letter
def uppercase_letter(password):
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    password += uppercase_letters[random.randint(0,len(uppercase_letters)-1)]
    return password


#function for adding lowercase letters, takes the password and adds a random lowercase letter
def lowercase_letter(password):
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    password += lowercase_letters[random.randint(0,len(lowercase_letters)-1)]
    return password


#function for adding numbers, takes the password and adds a random number
def number(password):
    numbers = "0123456789"
    password += numbers[random.randint(0,len(numbers)-1)]
    return password


#function for adding special characters, takes the password and adds a random special character
def special_character(password):
    special_characters = "`~!@#$%^&*()-_=+[]}{|:;'<,>.?/\"\\"
    password += special_characters[random.randint(0,len(special_characters)-1)]
    return password


#main function to make the password
def main():
    print("\nfill in the data below to generate a few random passwords:\n")
    while True:
        try: #stupid proof
            uppercase_letters = int(input("minimum number of uppercase letters: "))
            if uppercase_letters < 0: #more stupid proof
                print("\ninvalid input\n")
                continue
            lowercase_letters = int(input("minimum number of lowercase letters: "))
            if lowercase_letters < 0: #more stupid proof
                print("\ninvalid input\n")
                continue
            numbers = int(input("minimum number of uppercase numbers: "))
            if numbers < 0: #more stupid proof
                print("\ninvalid input\n")
                continue
            special_characters = int(input("minimum number of special characters: "))
            if special_characters < 0: #more stupid proof
                print("\ninvalid input\n")
                continue
            length = int(input(f"length of password (must be at least {uppercase_letters+lowercase_letters+numbers+special_characters}):"))
            if length < uppercase_letters+lowercase_letters+numbers+special_characters: #more stupid proof
                print("\ninvalid input\n")
                continue
            passwords = int(input("number of passwords: "))
            if length < 1: #more stupid proof
                print("\ninvalid input\n")
                continue
            break
        except ValueError:
            print("\ninvalid input\n")


    #repeat a specific number of times
    for x in range(passwords):
    #assemble the requirements
        requirements = []
        for i in range(uppercase_letters): #add uppercase letters to the requirements
            requirements.append(0)
        for i in range(lowercase_letters): #add lowercase letters to the requirements
            requirements.append(1)
        for i in range(numbers): #add numbers to requirements
            requirements.append(2)
        for i in range(special_characters): #add special characters to requirements
            requirements.append(3)
        for i in range(length-len(requirements)): #make everything else random
            requirements.append(random.randint(0,3))

        #use requirements to make the password
        full_password = ""
        for i in range(len(requirements)):
            random_number = random.randint(0,len(requirements)-1)
            if requirements[random_number] == 0: #if the value at the random index is 0, add a capital letter
                full_password = uppercase_letter(full_password)
            elif requirements[random_number] == 1: #if the value at the random index is 1, add a lowercase letter
                full_password = lowercase_letter(full_password)
            elif requirements[random_number] == 2: #if the value at the random index is 2, add a number
                full_password = number(full_password)
            elif requirements[random_number] == 3: #if the value at the random index is 3, add a special character
                full_password = special_character(full_password)

            requirements.pop(random_number) #remove the used value

        #print message on the first iteration
        if x == 0:
            print("\npossible passwords:")
        
        print(f"{full_password}\n") #print the finished password
    
    
    

main()