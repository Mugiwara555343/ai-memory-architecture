story = "" # the empty var is used as a placeholder to create the sentance 
attempts = 0
word_2 = None

while True:
    word = input("Please type in a word: ")
    
    attempts += 1 # or , attempts = attempts + 1 
    
    if word == "end":
        #break is written to end the loop and begin to print story
        break
    
    if word == word_2:
         # Exit the loop when the same word is entered twice
        break
    
    # Concatenate the word and add a space
    story += word + " "

 # Set word_2 to the current word for comparison
    word_2 = word


print(story)
    


 