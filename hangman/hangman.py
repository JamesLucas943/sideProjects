#-----Imports-----

import pandas as pd
import random

#-----Data-Entry-----
dictionary = pd.read_csv('words.csv')

dic = []

for i in dictionary.values:
    dic.append(str(i[0]))

#-----Functions-----

def HangMan(word):
    #--variables--
    
    #holds all guessed characters
    letters = []
    
    showWord = ""
    guesses = 6

    #used for input verification
    alphabet = "qwertyuiopasdfghjklzxcvbnm"

    #used to print a HangMan picture
    hangers = [" ____ \n |  |\n |\n |\n |\n | \n-----",
               " ____ \n |  |\n |  O\n |\n |\n | \n-----",
               " ____ \n |  |\n |  O\n |  !\n |  !\n | \n-----",
               " ____ \n |  |\n |  O\n | /!\n |  !\n | \n-----",
               " ____ \n |  |\n |  O\n | /!\ \n |  !\n | \n-----",
               " ____ \n |  |\n |  O\n | /!\ \n |  !\n | / \n-----",
               " ____ \n |  |\n |  0\n | /!\ \n |  !\n | / \ \n-----"]
    
    #makes the shown word
    for i in word:
        showWord += "_"

    #used to check if first time in loop
    loopValue = 0

    #loops until the word is guessed or ran out of guesses
    while '_' in showWord:
        #guessing a letter
        if guesses > 0:
            temp = ""
            showTemp = ""
            
            #makes the letters guessed already
            for i in letters:
                temp += " " + i

            #makes a more readable output for the user
            for i in showWord:
                #more letters
                if showTemp:
                    showTemp += ' ' + i
                    
                #first letter
                else:
                    showTemp = i
                    
            if loopValue != 0:
                print("\n\n\n")
            else:
                loopValue += 1
            print(hangers[6-guesses])
            print(showTemp, "\n\nGuessed Letters:", temp)
            print("\nYou have", guesses, "more errors left")

            #used to make sure that the user inputs valid characters
            valid = False
            while not valid:
                #gets the user's input
                guess = input("Letter you would like to guess: ").lower()

                #valid character
                if len(guess) == 1 and guess in alphabet and guess not in letters:
                    valid = True

                elif len(guess) == 1 and guess in alphabet:
                    print("You already guessed that letter!")

                #invalid character
                else:
                    print("Not a valid character. Please try again.")

            #saves the current character guessed
            letters.append(guess)

            #loop to see how many characters are found
            count = 0
            i = 0
            for i in range(len(word)):
                if guess == word[i]:
                    count += 1
                    showWord = showWord[:i] + guess + showWord[i+1:]	

            #found some characters (at least one)
            if count > 0:
                sent = "You found {} letter(s)!"
                sent = sent.format(count)
                print(sent)

            #character was not found
            else:
                print("Too bad, no hits...")
                guesses -= 1
            
            

        #out of guesses
        else:
            print("\n\n\n")
            print(hangers[6])
            print("YOU LOSE! \nThe word was", word)
            return
        
    #out of loop, win
    print("\n\n\nYOU WIN! \nThe word was", word)
    
#-----Main-Code-----
    
#used to pick a random word from the dic
randNum = random.randint(0,5946)
word = dic[randNum]

#-----Calls------

HangMan(word.lower())


