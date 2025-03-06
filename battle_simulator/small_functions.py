#Alec George Battle Simulator

#page with some small quality of life functions

#function to clear screen
def cs():
    print("\033c")


#function for exception handling (integers)
def is_int(value):
    try:
        int(value)

    except:
        value = is_int(input("\nPlease input an integer.\n"))
    return int(value)


