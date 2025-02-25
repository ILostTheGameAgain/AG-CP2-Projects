#Alec George To do list
#will store items on a text file, will let you view uncompleted items and completed items, will be able to add and remove items and mark items as complete


#function to add items
def add_item(item):
    with open("to_do_list/uncompleted_items.txt","r") as file: #set a variable to the list so it can be checked for repeats
        file_content = file.read().split("\n")
    
    with open("to_do_list/uncompleted_items.txt", "a") as file: #add the value to the list
        if item not in file_content: #don't allow repeat items
            file.write(f"{item}\n")
            return f"\nsuccessfully added {item} to the to do list"
        else:
            return f"\n{item} is already on the to do list"


#function to remove items
def remove_item(item):
    with open("to_do_list/completed_items.txt", "r") as file:
        file_content = file.read().split("\n") #make a list of all the items

    if item in file_content: #can't remove items not in the list
        file_content.remove(item)
    else:
        return f"\n{item} has not been completed"
    
    #turn file_content into a string to easily add it back to the folder
    new_list = ""
    for i in file_content:
        new_list += f"{i}\n"

    #rewrite the file as new_list
    with open("to_do_list/completed_items.txt", "w") as file:
        file.write(new_list)
    return f"\nsucessfully removed {item}"
    


#function to mark an item as complete (move it from incomplete to complete)
def complete_item(item):
    #remove item function, but with uncompleted items and small changes to remove the wanted item
    with open("to_do_list/uncompleted_items.txt", "r") as file:
        file_content = file.read().split("\n") #make a list of all the items

    if item in file_content: #can't remove items not in the list
        file_content.remove(item)
    else:
        return f"\n{item} is not on the to do list"
    
    #turn file_content into a string to easily add it back to the folder
    new_list = ""
    for i in file_content:
        new_list += f"{i}\n"

    #rewrite the file as new_list
    with open("to_do_list/uncompleted_items.txt", "w") as file:
        file.write(new_list)

    #add the completed item to the completed list
    with open("to_do_list/completed_items.txt","a")as file:
        file.write(f"{item}\n")

    return f"\nsuccessfully completed {item}"
        


#function to view the lists
def view():
    output = ""
    with open("to_do_list/uncompleted_items.txt","r") as file:
        output += f"\nuncompleted items:\n{file.read()}"

    with open("to_do_list/completed_items.txt", "r") as file:
        output += f"\n\ncompleted items:\n{file.read()}"

    return output
#main function
def main():
    while True:
        #if statement for user input
        choice = input("""\nwhat would you like to do? type:
 1 to add an uncompleted item
 2 to remove a completed item
 3 to mark an uncompleted item as complete
 4 to view the uncompleted and completed items
 5 to exit
 Your answer here: """)
        if choice == "1":
            print(add_item(input("\nwhat are you adding? ").strip().lower()))
        elif choice == "2":
            print(remove_item(input("\nwhat are you removing? "),))
        elif choice == "3":
            print(complete_item(input("\nwhat are you completing? ")))
        elif choice == "4":
            print(view())
        elif choice =="5":
            print("\nthank you for using this to do list\n")
            break
        else: #stupid proof, make everything else not do anything
            print("\ninvalid input")



main()