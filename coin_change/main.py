#Alec George coin change problem

#to read csv, import pandas
import pandas as pd


#function to see if something is in a list
def is_in_list(value, items):
    value = value.strip().lower()
    if value in items:
        pass
    else:
        print(f"\nthat is not an optoin. Your options are:\ndollars\npounds\neuros\n")
        value = is_in_list(input('what cion type are you using?\n'))

    return value


#main functoin to run everything else
def main():
    #variable for the available cions
    cions = []

    #make cions into a dataframe
    df = pd.read_csv('coin_change/denominations.csv')


    #function to add the right coin types to the list
    def add_coins(ct):
        for index, typ in enumerate(df['type']):
            if typ == ct:
                cions.append{}


    #tell user instructoins
    print("""
Welcome to the cion change problem!
To use, input the cion type you are using
Then, input the total amount of money you want
This will then tell you the minimum number of cions, bills, and notes to have that amount of money.
""")
    
    #ask user for cion type
    cion_type = is_in_list(input("\nwhat cion type are you using?\n"))

