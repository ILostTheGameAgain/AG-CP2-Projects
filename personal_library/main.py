#Alec George Personal Library

#will be a list of books, user can add, remove, view, and search for items, and exit the program
import random

#function to view the list
def view_books(book_list):
    printed_list = "\nBooks:"
    for i in book_list:
        printed_list += f"\n {i["cover type"]} {i["title"]} by {i["author"]} with {i["page count"]} pages"
    return printed_list



#function to add books
def add_book(book_list, new_title, new_author, new_pages, new_cover):
    book_list.append({
        "title": new_title,
        "author": new_author,
        "page count": new_pages,
        "cover type": new_cover

    })
    return book_list
    
    

#function to remove books
def remove_book(book_list, removed_item, remove_type):
    #choose what you're seaching for to remove
    if remove_type == "1":
        removed_item_count = 0
        for i in book_list:
            if removed_item.strip().lower() in i["title"].strip().lower():
                print(f"\n removed {i["cover type"]} {i["title"]} by {i["author"]} with {i["page count"]} pages")
                book_list.remove(i)
                removed_item_count += 1

        if removed_item_count == 0:
            print(f"\n there are no items with {removed_item} in the title")

    elif remove_type == "2":
        removed_item_count = 0
        for i in book_list:
            if removed_item.strip().lower() in i["author"].strip().lower():
                print(f"\n removed {i["cover type"]} {i["title"]} by {i["author"]} with {i["page count"]} pages")
                book_list.remove(i)
                removed_item_count += 1

        if removed_item_count == 0:
            print(f"\n there are no items with {removed_item} in the author's name")

    elif remove_type == "3":
        removed_item_count = 0
        for i in book_list:
            if removed_item.strip().lower() in str(i["page count"]).strip().lower():
                print(f"\n removed {i["cover type"]} {i["title"]} by {i["author"]} with {i["page count"]} pages")
                book_list.remove(i)
                removed_item_count += 1

        if removed_item_count == 0:
            print(f"\n there are no items with {removed_item} in the page number")

    elif remove_type == "4":
        removed_item_count = 0
        for i in book_list:
            if removed_item.strip().lower() in str(i["cover type"]).strip().lower():
                print(f"\n removed {i["cover type"]} {i["title"]} by {i["author"]} with {i["page count"]} pages")
                book_list.remove(i)
                removed_item_count += 1

        if removed_item_count == 0:
            print(f"\n there are no items with {removed_item} in the cover type")

    else: #stupid proof
        print("\n invalid input")

    return book_list
        




#function to search for books or authors
def search_book(book_list, searched_item):
    #search titles
    searched_list = f"\nbooks with {searched_item} in title:"
    for i in book_list:
        if searched_item.strip().lower() in i["title"].strip().lower():
            searched_list += f"\n {i["cover type"]} {i["title"]} by {i["author"]} with {i["page count"]} pages"

    #search authors
    searched_list += f"\n\nbooks with {searched_item} in author:"
    for i in book_list:
        if searched_item.strip().lower() in i["author"].strip().lower():
            searched_list += f"\n {i["cover type"]} {i["title"]} by {i["author"]} with {i["page count"]} pages"
    return searched_list



#function to generate random books
def random_books(book_list):
    number = 0
    letters = "qwertyuiopasdfghjklzxcvbnm "
    for i in range(random.randint(1,20)):
        new_title = ""
        for i in range(random.randint(4,10)):
            new_title += letters[random.randint(0,26)]

        new_author = ""
        for i in range(random.randint(4, 10)):
            new_author += letters[random.randint(0,26)]

        new_page_count = random.randint(100,1000)

        if random.randint(1,2) == 1:
            new_cover_type = "paperback"

        else:
            new_cover_type = "hardcover"

        
        book_list.append({
            "title": new_title.strip().lower(),
            "author": new_author.strip().lower(),
            "page count": new_page_count,
            "cover type": new_cover_type
        })
        number += 1

    print(f"\n generated {number} new books")
    return(book_list)




#main function
def main():
    #list for books and authors with some stuff already in it
    books = []
    #while loop to continuously run other functions
    while True:
        #take user input for what to do, and stupid proof
        try:
            action = int(input("""\nWhat would you like to do? type:
 1 to view the list
 2 to add a book
 3 to remove a book
 4 to search for a book
 5 to generate random books
 6 to end the program
your answer here: """))
            
            
            if action == 1: #if action is 1, view the list
                print(view_books(books))
            
            elif action == 2: #if action is 2, add a book and its author
                books = add_book(books, input("\nwhat book would you like to add? ").strip().lower().capitalize(), input("what is the book's author? ").strip().lower().capitalize(), int(input("how many pages does it have? ")), input("Is it hardcover or paperback? ").strip().lower())

            elif action == 3: #if action is 3, remove a book and its author
                books = remove_book(books, input(" what are you removing? "), input(" type:\n  1 to search by title\n  2 to search by author\n  3 to search by page count\n  4 to search by cover type\n your answer here: "))

            elif action == 4: #if action is 4, search for books and authors
                print(search_book(books, input("\nwhat are you searching for? ").strip().lower()))
            
            elif action == 5: #if action is 5, generate random books
                books = random_books(books)

            elif action == 6:
                break

            else: #anything else is an invalid input
                print("\ninvalid input")


        except ValueError:
            print("\ninvalid input")
            continue

#run main function
main()
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nI lost the game\n\n")