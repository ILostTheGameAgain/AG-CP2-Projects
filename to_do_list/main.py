#Alec George To do list
#will store items on a text file, will let you view uncompleted items and completed items, will be able to add and remove items and mark items as complete


#function to add items
def add_item(item):
    with open("to_do_list/uncompleted_items.txt","a") as file:
        if item not in file: #don't allow repeat items on the list
            file.write(f"{item}\n")
            return f"\nsuccessfully added {item} to the to do list"
        else:
            return f"\n{item} is already on the to do list"


#function to mark an item as complete
def complete_item(item):
    with open("to_do_list/uncompleted_items.txt", "w+") as file:
        if item not in file: #can't complete items not there
            return f"\n{item} is not on the to do list"

        else:
            list_of_items = file.split("\n")
            print(list_of_items)


#function to remove items
def remove_item():
    pass



#main function
def main():
    while True:
        print(add_item(input("\nwhat are you adding? ")))



main()