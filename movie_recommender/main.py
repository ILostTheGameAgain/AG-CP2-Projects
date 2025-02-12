#Alec George movie recommender

#will use a csv file filled with movies, and allow the user to find recommendations based on what's inside
import csv


#function to search items/get recommendations based on genre and rating


#main function
def main():
    #make a variable for the movie list so it isn't just stored in a csv file
    movie_list = []

    #open the file and make it into a lot of dictionaries in the list
    with open("movie_recommender/Movies list.csv") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)

        #go through every item and set it to a dictionary
        for row in csv_reader:
            movie_list.append({
                "title": row[0], #set first item to the title
                "director": row[1], #set second item to the director
                "genre": row[2], #set third item to the genre
                "rating": row[3], #set fourth item to the rating
                "length": row[4], #set fifth item to the length of the movie
                "notable actors": row[5].split(", ") #set the sixth item to a list of notable actors
            })

    

    


    


main()
