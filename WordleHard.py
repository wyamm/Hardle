
import sys, os
import colorama
from colorama import Fore, Back, Style
from random import choice

colorama.init()


def printback(statement, colour):
    print(colour + Style.BRIGHT + f"{statement}" + Style.RESET_ALL, end = "")

green = Back.GREEN
yellow = Back.YELLOW
grey = Back.LIGHTBLACK_EX
fname = "five_letter_words_list.txt"

f = open(fname, 'r')
lines = f.readlines()
f.close()
wordlist = []

for line in lines:
    words = [w.strip() for w in line.split(',') if w not in [' ', ' \n']]
    wordlist += words

# wordlist = list(set(wordlist))
# wordlist.remove('')
word = choice(wordlist)
listword = list(word)

print("Guess a 5 letter word! ")
guess = ""
numGuess = 0
MAX_GUESS = 6

while numGuess < MAX_GUESS:
    while guess not in wordlist:
        guess = input(f"Guess {numGuess + 1}: ")
    listguess = list(guess)
    if guess == word:
        printback(guess, green)
        print()
        print(f"You have won in {numGuess + 1} guesses!")
        break
    word_without_cpl = ""
    for guess_letter, word_letter in zip(listguess, listword):
        if guess_letter == word_letter:
            word_without_cpl += " "
        else:
            word_without_cpl += word_letter

    for guess_letter, word_letter in zip(listguess, listword):
        if guess_letter == word_letter:
            printback(guess_letter, green)
        elif guess_letter in word_without_cpl:
            printback(guess_letter, yellow)
            word_without_cpl = list(word_without_cpl)
            word_without_cpl.remove(guess_letter)
            word_without_cpl = "".join(word_without_cpl)
        else:
            printback(guess_letter,  grey)
    print()
    numGuess += 1
    guess = ""
print(f"The correct word was {word}")