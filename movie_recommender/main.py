#Alec George movie recommender

#will use a csv file filled with movies, and allow the user to find recommendations based on what's inside
import csv



#function to search items/get recommendations based on genre and rating
def search(movies, genre, rating):
    #variable for the end output, will add movies to it
    output = []

    #make it so the rating will be ignored if it is left blank
    if len(rating) == 0:
        rating = ["G", "PG", "PG-13", "R", "NOT RATED"]

    else:
        rating = [rating]

    #search through the movies list and add any movies with the matching genre and rating to the output
    for i in range(len(movies)):
        if genre in movies[i]["genre"].strip().lower() and movies[i]["rating"].strip().upper() in rating:
            #variable for each item in the list, combining the main stuff with the list of notable actors
            list_item = f"""

Title: {movies[i]["title"]}
director: {movies[i]["director"]}
genre: {movies[i]["genre"]}
rating: {movies[i]["rating"]}
length: {movies[i]["length"]} minutes
notable actors: """
            for actors in movies[i]["actors"]:
                list_item += f"{actors}, "

            output.append(list_item)

    #state that there were no matching movies if no movies matched the search
    if len(output) == 0:
        output.append(f"\n there are no {rating} {genre} movies in the list")

    return output



#main function
def main():
    #make a variable for the movie list so it isn't just stored in a csv file
    movie_list = []

    #open the file and make it into a lot of dictionaries in the list
    with open("movie_recommender/Movies list.csv", "r") as file:
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
                "actors": row[5].split(", ") #set the sixth item to a list of notable actors
            })
    

    searched_list = search(movie_list, input("\n\nWhat genre are you searching for? (leave blank if this does not matter) ").strip().lower(), input("What rating are you searching for? (G, PG, PG-13, or R, leave blank if this does not matter) ").strip().upper())

    for i in searched_list:
        print(i)

    


    

while True:
    main()
