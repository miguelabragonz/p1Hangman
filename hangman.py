'''
Created on Nov 23, 2019

@author: ITAUser
'''
#import the random library

#define a function called pick_random_word():
    #open and read word dictionary/list(words.txt)
    
    #variable called index = selects random word from words.txt
    #variable called word = strip the randomly selected word 
    #return the variable 'word's
    
#define a function called ask_for_next_letter():
    #variable called letter = input function that asks to select a letter
    #return the letter selected 
    
#define a function called generate_word_string(word, letters _guessed):
    #variable called output = empty list
    #make a four loop that goes through each letter in the variable 'word':
        #if statement that checks if letter is in letters_guessed:
            #append letter to output 
        #else:
            #append("_")
        #return output as a strong
    
#create a main module:
    #variable called WORD = pick_random_word()
    
    #variable called letters_to_guess = set of WORD
    #variable called correct_letters_guessed = empty set 
    #variable called incorecct_letters_guessed = empty set
    #variable called number_of_guesses = number of guesses you want the user to have 
    
    #print statement that welcomes the user to hangman 
    
    #while loop that runs until number_of_guesses less than 1 or letters_to_guess is greater than 0
        #variable called guess = ask_for_next_letter() and turn into lower case
        
        #if statement that checks if guess_letters_guessed or guess is in incorrect_letters_guessed:
            #print statement that says you have already guessed this letter
            
        #if statement checks if guess is in letters_to_guess:
            #remove guess from letters_to_guess
            #add guess to correct_letters_guessed 
        #else:
            #add guess to incorrect_letters_guessed
            #number_of_guesses goes down by 1 
            
        #variable called word_string = generate_word_string(WORD, correct_letters_guessed)
        #print statement that prints word string
        #print statement that print how many guesses you have left 
        
        #if statement to check if numbers is less than one:
            #print congratulations you guessed the word
        #else:
            #print sorry you lost 