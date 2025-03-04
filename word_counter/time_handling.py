#Alec George word counter

#will have functions to manage the timestamps, will need datetime module
import datetime


#function for adding a timestamp to the file for last update
def get_timestamp():
    #assign today's date to a variable
    date = datetime.datetime.now()
    #display the date as text formatted as Week, month, day of month
    text = f"{date.strftime("%A")}, {date.strftime("%B")} {date.strftime("%d")}"
    return text


