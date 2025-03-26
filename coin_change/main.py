#Alec George coin change problem

#to read csv, import pandas
import pandas as pd


#functoin to see if something is in a list
def is_in_list(value, items1, items2):
    value = value.strip().lower()
    if value in items1:
        return value
    
    elif value in items2:
        return value
    else:
        print(f"\nthat is not an optoin. Your optoins are:\ndollars (us)\npounds (uk)\neuros(no specific place)\nkronor (sweden)\n")
        value = is_in_list(input('what cion type are you using?\n'), items1,items2)

    return value


#functoin to check if something is an integer
def is_float(value):
    try:
        int(value)
    except:
        value = is_float(input('\nthat is not a number. Try again\n'))

    return int(value)


#functoin to check if something is greater than 0
def is_positive(value):
    if value <= 0:
        value = is_positive(is_float(input('\nthat is not a valid number. Try again\n')))
        
    return value


#main functoin to run everything else
def main():
    #variable for the available cions
    cions = {
        'name': [],
        'value': []
    }

    #make cions into a dataframe
    df = pd.read_csv('coin_change/denominations.csv')
    #make it a dictionary
    df = df.to_dict()

    #functoin to add the right cion types to the list
    def add_coins(ct):
        for index, typ in enumerate(df['type'].values()):
            if typ == ct:
                cions['name'].append(df['name'][index])
                cions['value'].append(df['value'][index])

        for index, typ in enumerate(df['country'].values()):
            if typ == ct:
                cions['name'].append(df['name'][index])
                cions['value'].append(df['value'][index])


    #functoin to calculate the right coins to add to get target amount
    def caclate(amt):
        cion_string = 'needed cions/bills/notes:'
        #do for every coin
        for i in range(len(cions['name'])):
            repeats = 0
            #subtract the coin that can still fit in the amont repeatedly
            while amt > 0:
                amt -= cions['value'][-(i+1)]
                repeats += 1

            if amt < 0:
                amt += cions['value'][-(i+1)]
                repeats -= 1

            cion_string += f'\n{repeats} '

            print(amt)

    #tell user instructoins
    print("""
Welcome to the cion change problem!
To use, input the cion type you are using
Then, input the total amount of money you want
This will then tell you the minimum number of cions, bills, and notes to have that amount of money.
""")
    
    #ask user for cion type
    cion_type = is_in_list(input("\nwhat is the name of the cion type/country?\n"), df['type'].values(), df['country'].values())
    add_coins(cion_type)

    #ask user for amount
    amount = is_positive(is_float(input(f"\nhow many {cion_type} are you finding?\n")))

    #print the number of cions
    caclate(amount)



main()