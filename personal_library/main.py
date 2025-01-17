#Alec George Personal Library

#will be a list of books, user can add, remove, view, and search for items, and exit the program


#function to view the list
def view(book_list):
    printed_list = "\nBooks:\n"
    for i in book_list:
        printed_list += f" {i}\n"
    return printed_list



#function to add books
def add(book_list, new_book, new_author):
    book_list.add(f"{new_book} by {new_author}")
    return book_list
    
    

#function to remove books
def remove(book_list, removed_item):
    for i in book_list:
        if removed_item.strip().lower() in i.strip().lower():
            book_list.remove(i)
            return book_list
        
    print(f"\n there are no books with {removed_item} in the title or author")



#function to search for books or authors
def search(book_list, searched_item):
    searched_list = f"\nbooks with {searched_item} in title or author:"
    for i in book_list:
        if searched_item in i.strip().lower():
            searched_list += f"\n {i}"
    return searched_list




#main function
def main():
    #list for books and authors with some stuff already in it
    books = {"The Way of Kings by Brandon Sanderson", "Words of Radiance by Brandon Sanderson", "Oathbringer by Brandon Sanderson", "Rhythm of War by Brandon Sanderson", "Wind and Truth by Brandon Sanderson", "What If by Randal Monroe", "Math Textbook by someone... i don't know who"}
    #while loop to continuously run other functions
    while True:
        #take user input for what to do, and stupid proof
        try:
            action = int(input("""\nWhat would you like to do? type:
 1 to view the list
 2 to add a book
 3 to remove a book
 4 to search for a book
 5 to end the program
your answer here: """))
        except ValueError:
            print("\ninvalid input")
            continue
        
        if action == 1: #if action is 1, view the list
            print(view(books))
        
        elif action == 2: #if action is 2, add a book and its author
            books = add(books, input("\nwhat book would you like to add? ").strip().lower().capitalize(), input("what is the book's author? ").strip().lower().capitalize())

        elif action == 3: #if action is 3, remove a book and its author
            books = remove(books, input(" what are you removing? "))

        elif action == 4: #if action is 4, search for books and authors
            print(search(books, input("\nwhat are you searching for? ").strip().lower()))
        
        elif action == 5:
            break

        else: #anything else is an invalid input
            print("\ninvalid input")

#run main function
main()
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nI lost the game\n\n")