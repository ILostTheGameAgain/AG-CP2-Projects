#alec george financial calculator

#will do certain financial functions, uses math library
import math

#function to calculate how long it will take to save for a goal based on a weekly or montlhly deposit

#function to calculate compound interest, will return the amount of money you'll have after a certain amount of time of compound interest, will recieve variables for starting amount, the growth %, the amount of time, and how often it grows
def compound_interest(start, percent, compound_rate, time):
    if compound_rate == 0:
        sum = round(round(start, 2)*math.e**(percent*time), 2)
    else:
        sum = round(round(start, 2)*(1+(percent/compound_rate))**(compound_rate*time), 2)
    return(f"{sum}")

#function to calculate budget

#function to calculate discounts to prices

#function to calculate tips


#main function
def main():
    while True:
        print(f"${compound_interest(float(input(" start amount:")),float(input(" interest percent")),0,10)}")
main()

