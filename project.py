from random import choice
import re

def main():

    pig_latin()


def pig_latin():
    # get input, sellect direction
    # translating starts with a consonant or a vowel. If it’s a consonant, 
    # move all the letters that come before the first vowel to the end of the word. 
    # Then, add the suffix “-ay.” 
    # If the word starts with a vowel, just add “-yay,” “-way,” or “-ay” to the end of the word.
    # example sentance
    sentance = input(": ")
    direction = input("select in/out: ").lower()
    print(direction)

    if "in" == direction:
        translation = translate_in(sentance)
        print(translation)

    elif "out" == direction:
        translation = translate_out(sentance)
        print(translation)
        
    
    else:
        print("incorrect formating")


def translate_in(sentance):
    output = ""
    #translate acording to rules
    print("translate in")
    for word in sentance.split(" "):
        output += " " + check_word_in(word)
    return output


def translate_out(sentance):
    #fix
    output = ""
    print("translate out")
    for word in sentance.split(" "):
        output += " " + check_word_out(word)
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
    suffix = ["yay","way","ay"]
    # iterate over letters in the word,
    for letter in word:
        if check_vowel(letter):
            return word + choice(suffix)
        else:
            first_vowel = re.search(r'[eaoiu]', word)
            print(first_vowel, word)
            output = word[first_vowel.start():] + word[:first_vowel.start()]+"ay"
            print(output)
            return output

def check_word_out(word):
    print(word)
    suffix = ["yay","way","ay"] 

    for letter in word:
        ...



if __name__ == "__main__":
    main()