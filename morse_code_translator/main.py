#Alec George Simple Morse Code Translator

#will give the user the option to either translate a line of morse code to english or english to morse code


#main function
def main():
    #list of english letters and morse code letters with corresponding letters having the same index
    english = ["a", "b", "c", "d", "e" "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
    morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", " / "]

    #user input to decide if they're going from english to morse code or morse code to english, supid proofed
    while True: #stupid proof while loop
        choice = input("\nwhat would you like to do? type:\n 1 to translate English to morse code\n 2 to translate morse code to english\n 3 to exit program\n your answer here (type 1, 2, or 3): ")
        if choice in "123" and len(choice) == 1:
            break
        else:
            print("\ninvalid input")

    #use choice to decide what to do
    if choice == "1"




main()