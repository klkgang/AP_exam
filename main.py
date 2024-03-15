#colarama is an open source code project and I'm not the creator 
#official link https://pypi.org/project/colorama/
from colorama import Fore

#os is a library that is part of python and I'm not the creator
#official link https://docs.python.org/3/library/os.html
import os

#random librery is a librery that forms part of python and I'm not the creator 
#official link https://docs.python.org/3/library/random.html
import random

#definition of the list with the words that the game will use 
words = ['python', 'four', 'brave', 'computer', 'science', 'aircraft']

def clear_screen():
    """This function is to clean the screen"""
    os.system('clear')

def welcome_screen_message():
    """This function is to print a welcome message to the user"""
    welcome_message = """
        
     _    _ _____ _     _____ ________  ___ _____ 
    | |  | |  ___| |   /  __ \  _  |  \/  ||  ___|
    | |  | | |__ | |   | /  \/ | | | .  . || |__  
    | |/\| |  __|| |   | |   | | | | |\/| ||  __| 
    \  /\  / |___| |___| \__/\ \_/ / |  | || |___ 
     \/  \/\____/\_____/\____/\___/\_|  |_/\____/ 
                                              
    """

    print(Fore.GREEN + welcome_message)

def congratulation_message_screen():
    """This funtion print the congratulations message"""
    congratulation_message = """

     _____                             _         _       _   _                 
    /  __ \                           | |       | |     | | (_)                
    | /  \/ ___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_ _  ___  _ __  ___ 
    | |    / _ \| '_ \ / _` | '__/ _` | __| | | | |/ _` | __| |/ _ \| '_ \/ __|
    | \__/\ (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | \__ |
     \____/\___/|_| |_|\__, |_|  \__,_|\__|\__,_|_|\__,_|\__|_|\___/|_| |_|___/
                        __/ |                                                  
                       |___/                                                   
    """
    print(Fore.GREEN + congratulation_message)


def sorry_message():
    """This funtion print the sorry message"""
    banner = """
    
     __                       
    / _\ ___  _ __ _ __ _   _ 
    \ \ / _ \| '__| '__| | | |
    _\ \ (_) | |  | |  | |_| |
    \__/\___/|_|  |_|   \__, |
                        |___/ 
    """

    print(Fore.RED + banner)

def start_screen():
    """This fucntion is to print the welcome screen in the console"""
    clear_screen()
    welcome_screen_message()

    print()
    print(Fore.BLUE + "This is my guess a word game called Adivinador")
    print()
    input("Press Enter to continue..")


def select_random_word():
    """This function handle the selection of a random word from the 'words' list,
    and then it will retur that word"""
    random_number = random.randint(0, len(words))
    random_number = random_number - 1
    random_word = words[random_number]

    return random_word


def main_game_logic(guess, word, guessed_word):
    """This function has all the logic of the main game"""
    print()

    for i in range(len(word)):
        if guess == word[i]:
            guessed_word[i] = guess 
        if '*' not in guessed_word:  
            clear_screen()
            congratulation_message_screen()
            print()
            print(Fore.MAGENTA + f"You guessed the word: {''.join(word)}")
            print(Fore.MAGENTA + "Thank you for playing")
            exit()
    return guessed_word


def game(password):
    """This function handle the display of the main game"""
    
    clear_screen()
    word = list(password)
    print(word)
    guessed_word = ['*'] * len(password)
    guesses = 3
    
    while True: 
        print()
        print(Fore.GREEN + f"YOUR WORD: {''.join(guessed_word)}")
        print()
        
        guess = input(Fore.BLUE + "Guess a letter of the word: ")

        guessed_word = main_game_logic(guess, word, guessed_word)

        if not guess in word:
            print()
            print(Fore.RED + f"{guess} is not in your word")
            guesses = guesses - 1

            print()
            print(Fore.YELLOW + f"Guesses that you have left: {guesses}")

        if guesses == 0:
            clear_screen()
            sorry_message()
            print()
            print(Fore.RED + f"You couldn't guess the word: {''.join(word)}")
            print(Fore.RED + "you loose")
            exit()

start_screen()
password = select_random_word()
game(password)