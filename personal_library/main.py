#Alec George Personal Library

#will be a list of books, user can add, remove, view, and search for items, and exit the program

#list for books and authors
books = []
authors = []


#function to view the list
def view(book_list, author_list):
    printed_list = "Books:\n"
    for i in range(len(book_list)):
        printed_list += f" {book_list[i]} by {author_list[i]}\n"
        return printed_list


#function to add books
def add(book_list, author_list, new_book, new_author):
    book_list.append(new_book)
    
    

#function to remove books


#function to search for books or authors


#main function
def main():
    view(books, authors)

#while loop to stupid proof and repeat main function
main()