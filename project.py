from random import choice
import re
import psutil
import time

def main():

    pig_latin()


def pig_latin():
    # get input
    sentance = input(": ")
    translation = translate_in(sentance)
    print(translation)


def translate_in(sentance):
    output = ""
    #translate acording to rules
    print("translate in")
    for word in sentance.split(" "):
        output += " " + check_word_in(word)
    return output


def check_vowel(letter):
    # to check later
    consonants = ['t', 'n', 's', 'r', 'h', 'l', 'd', 'c', 'm', 'f', 'p', 'g', 'w', 'y', 'b', 'v', 'k', 'x', 'j', 'q', 'z']
    # check if letter is a vowel
    vowels = ['e', 'a', 'o', 'i', 'u']
    if letter in vowels:
        return True
    else:
        return False


def check_word_in(word):
    print(word)
    suffix = ["yay","way", "ay"]
    # iterate over letters in the word,
    for letter in word:
        if check_vowel(letter):
            return word + choice(suffix)
        else:
            first_vowel = re.search(r'[eaoiu]', word)
            return word[first_vowel.start():] + word[:first_vowel.start()]+"ay"



#real project measure and print time and log efficiency
class measurement():




if __name__ == "__main__":
    main()