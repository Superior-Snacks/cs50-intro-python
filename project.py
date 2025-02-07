from random import choice
from re import search, match

def main():

    pig_latin()


def pig_latin():
    # get input, sellect direction
    # translating starts with a consonant or a vowel. If it’s a consonant, 
    # move all the letters that come before the first vowel to the end of the word. 
    # Then, add the suffix “-ay.” 
    # If the word starts with a vowel, just add “-yay,” “-way,” or “-ay” to the end of the word.
    sentance = input(": ")
    direction = input("select in/out: ").lower()
    print(direction)

    if "in" == direction:
        translate_in(sentance)

    elif "out" == direction:
        translate_out(sentance)
    
    else:
        print("incorrect formating")


def translate_in(sentance):
    #translate acording to rules
    print("translate in")


def translate_out(sentance):
    #fix
    print("translate out")


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
    suffix = ["yay","way","ay"]
    # iterate over letters in the word,
    for letter in word:
        if check_vowel(letter):
            return word.append(choice(suffix))
        else:
            first_vowel = search(r'[eaoiu]', word)
            print(word.append(word[:first_vowel]+"ay"))
            return word.append(word[:first_vowel]+"ay")

def check_word_out(word):
    ...


if __name__ == "__main__":
    main()