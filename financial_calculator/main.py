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
    print(f"${compound_interest(round(float(input(" start amount: ")), 2),float(input(" annual interest amount (typed as a decimal, example: 1 = 100%, 0.1 = 10%): ")),float(input(" compound rate (yearly is 1, monthly is 12, daily is 365, continuous is 0): ")), float(input(" time (years): ")))}")


#while loop to continuously run main function and stupid proof it
while True:
    main()