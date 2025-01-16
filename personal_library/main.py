#Alec George Personal Library

#will be a list of books, user can add, remove, view, and search for items, and exit the program


#function to view the list
def view(book_list, author_list):
    printed_list = "\nBooks:\n"
    for i in range(len(book_list)):
        printed_list += f" {book_list[i]} by {author_list[i]}\n"
    return printed_list


#function to add books
def add(book_list, author_list, new_book, new_author):
    book_list.append(new_book)
    author_list.append(new_author)
    return (book_list, author_list)
    
    

#function to remove books
def remove(book_list, author_list, removed_item_type, removed_item):
    if removed_item_type == "1": #remove the item with matching title if input is 1
        for i in range(len(book_list)):
            if book_list[i] == removed_item:
                book_list.pop(i)
                author_list.pop(i)

                return book_list, author_list
            
        print(f" there isn't a book with the title, {removed_item}")
    
    elif removed_item_type == "2": #remove the item with the matching author if input is 2
        for i in range(len(author_list)):
            if author_list[i] == removed_item:
                book_list.pop(i)
                author_list.pop(i)

                return book_list, author_list
            
        print(f" there isn't a book with the author, {removed_item}")
    
    else: #stupid proof
        print("\n invalid input")
        return book_list, author_list


#function to search for books or authors
def search(book_list, author_list, searched_item):
    searched_list = f"books with {searched_item} in title or author:"
    for i in range(len(book_list)):
        if searched_item in book_list[i] or searched_item in author_list[i]:
            searched_list += f"\n {book_list[i]} by {author_list[i]}"
    return searched_list



#main function
def main():
    #list for books and authors
    books = ["The Way of Kings", "Words of Radiance", "Oathbringer", "Rhythm of War", "Wind and Truth", "What If", "Math Textbook"]
    authors = ["Brandon Sanderson", "Brandon Sanderson", "Brandon Sanderson", "Brandon Sanderson", "Brandon Sanderson", "Randal Monroe", "whoever wrote the math textbook"]
    #while loop to continuously run other functions
    while True:
        #take user input for what to do, and stupid proof
        try:
            action = int(input("""\nWhat would you like to do? type:
 1 to view the list
 2 to add a book
 3 to remove a book
 4 to search for a book
your answer here: """))
        except ValueError:
            print("\ninvalid input")
            continue
        
        if action == 1: #if action is 1, view the list
            print(view(books,authors))
        
        elif action == 2: #if action is 2, add a book and its author
            books, authors = add(books, authors, input("\nwhat book would you like to add? "), input("what is the book's author? "))

        elif action == 3: #if action is 3, remove a book and its author
            books, authors = remove(books, authors, input("\n to remove an item with a matching title, type 1\n to remove an item with a matching author, type 2\n your answer here: "), input(" what are you removing? "))

        elif action == 4: #if action is 4, search for books and authors
            print(search(books, authors, input("\nwhat are you searching for? ")))

        else: #anything else is an invalid input
            print("\ninvalid input")

#run main function
main()