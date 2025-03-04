#Alec George word counter main page

#will pull things together, project's purpose is to take a document and update it to have a word count and a timestamp to show how long it's been since the last word count
from file_handling import *
from time_handling import *


#function to find the word count of something
def word_count(text):
    return len(text.split())


#main function
def main():

    while True:
        #ask for user input of what to do
        user_input = input("""\nWhat would you like to do? Type:
1 to add a timestamp to the built in document
2 to add a timestamp to a different document (you will need to copy/paste the relative path)
3 to exit the program
Your answer here: """)
        
        #if user input is 1, add the word count to the already existing file with the project
        if user_input == "1":
            file = "word_counter/document.txt"

        #if user input is 2, add the word count to a file they added    
        elif user_input == "2":
            file = input("\nPaste the relative path here:\n")

            #make sure the file exists
            try:
                read_file(file)
            except:
                print("not a file")

        #if user input is 3, exit the program
        elif user_input == "3":
            break

        #exception handling
        else:
            print("\ninvalid input")
            continue

        #set the file's contents to a variable for easier editing
        document = read_file(file)

        #prepare thing that displays the word count and timestamp
        wordcount_display = f"word count: {word_count(document)}\nlast checked:\n{get_timestamp()}"
        
        #ask if user would like to add the word count at the top or bottom of the document
        while True: #while loop to stupid proof
            wordcount_location = input("""\nWhat would you like to do? Type:
1 to add the word count and timestamp at the top of the document
2 to add it to the bottom
Your answer here: """)
            #if word count location is 1, add the word count to the top
            if wordcount_location == "1":
                edit_file(file, f"{wordcount_display}\n\n{document}")
                break

            #if word count location is 2, add the word count at the bottom
            elif wordcount_location == "2":
                edit_file(file, f"{document}\n\n{wordcount_display}")
                break

            #exception handling
            else:
                print("\ninvalid input")

        #confirm to the user that it was updated
        print("\nupdated successfully")
        

main()