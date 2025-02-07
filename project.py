from random import choice
import re

def main():

    pig_latin()


def pig_latin():
    # get input, sellect direction
    # translating starts with a consonant or a vowel. If it’s a consonant, 
    # move all the letters that come before the first vowel to the end of the word. 
    # Then, add the suffix “-ay.” 
    # If the word starts with a vowel, just add “-yay,” “-way,” to the end of the word.
    # example sentance: ellohay orldway everyoneway utpay ouryay andshay inay ethay airay
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
    suffix = ["yay","way"]
    # iterate over letters in the word,
    for letter in word:
        if check_vowel(letter):
            return word + choice(suffix)
        else:
            first_vowel = re.search(r'[eaoiu]', word)
            return word[first_vowel.start():] + word[:first_vowel.start()]+"ay"


if __name__ == "__main__":
    main()