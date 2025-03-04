#Alec George Word counter

#will have functions to manage files, to select which files to open, edit them, etc


#function to open a document/file and set it to a string for editing
def read_file(path):
    with open(path,"r") as file:
        return file.read()
    

#function to edit a file/change it after things are added/removed
def edit_file(path, new_text):
    with open(path,"w") as file:
        file.write(new_text)