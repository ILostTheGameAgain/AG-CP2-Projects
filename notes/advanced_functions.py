#Alec George advanced functoins notes


#Helper functoin
def is_int(user_input):
    try:
        int(user_input)

    except:
        print("Please give me a number")
        user_input = is_int(input("\nHow old are you? ")) #recursoin

    return user_input
    
def age():
    old = is_int(input("\nHow old are you? "))

    print(f"you are {old}")

#age()


def add(a):

    def additoin(b):
        return a+b

    return additoin

#add(3)


import logging

logging.basicConfig(level=logging.INFO)

def logger(func):

    def wrapper(*args, **kwargs):
        logging.info(f"Executing {func.__name__} with {args}, {kwargs}")
        return func(*args, *kwargs)
    return wrapper

#@logger
def adder(a,b):
    return a+b

#adder(3,4)


base = add(10)

print(base(5))