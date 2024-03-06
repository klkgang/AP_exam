#colarama is a open source code and I'm not the creator 
#official link https://pypi.org/project/colorama/
from colorama import Fore

#os is a library that is part of python and I'm not the creator
#official link https://docs.python.org/3/library/os.html
import os

#random librery is a librery that forms part of python and I'm not the creator 
#official link https://docs.python.org/3/library/random.html
import random

#definition of the list with the words that the game will use 
words = ['python', 'AP_exam', '2026_class', 'computer', 'science', 'aircraft']

def clear_screen():
    """This function is to clean the screen"""
    os.system('clear')

def welcome_screen_message():
    """This function will give a welcome message to the user and take them to the actuall game"""
    welcome_message = """"
        
     _    _ _____ _     _____ ________  ___ _____ 
    | |  | |  ___| |   /  __ \  _  |  \/  ||  ___|
    | |  | | |__ | |   | /  \/ | | | .  . || |__  
    | |/\| |  __|| |   | |   | | | | |\/| ||  __| 
    \  /\  / |___| |___| \__/\ \_/ / |  | || |___ 
     \/  \/\____/\_____/\____/\___/\_|  |_/\____/ 
                                              
    """

    print(Fore.GREEN + welcome_message)

def start_screen():
    clear_screen()
    welcome_screen_message()

    print()
    print(Fore.BLUE + "This is my guess word game called Adivinador")
    print()
    input("Press any key to continue..")


def select_random_word():
    random_number = random.randint(0, len(words))
    random_number = random_number - 1
    random_word = words[random_number]

    return random_word

def game(password):
    clear_screen()
    
    word = list(password)
    guessed_word = ['*'] * len(password)
    print(guessed_word)
    
    print(f"Your word is: {password}") 
    
    while True:
        guess = str(input("Your guess: "))

        if guess in word:
            letter_index = word.index(guess)
            print("Letter found at index:", letter_index)
            guessed_word.pop(letter_index)
            guessed_word.insert(letter_index, guess)

            print("Current guessed word:", guessed_word)

        if '*' not in guessed_word:
            break


    



    
    
    

start_screen()
password = select_random_word()
game(password)
