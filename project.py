from random import choice
import re
import psutil
import time

def main():
    manage = measurement()
    pig_latin()
    manage.start_pc_check()
    manage.report()


def pig_latin():
    # get input
    #sentance = input(": ")
    sentance = "hello world everyone wants these hands but noone will integrate over areas of interest"
    translation = translate_in(sentance)
    print(translation)


def translate_in(sentance):
    output = ""
    #translate acording to rules
    for word in sentance.split(" "):
        output += " " + check_word_in(word)
    output[0].replace("")
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
    suffix = ["yay","way", "ay"]
    # iterate over letters in the word,
    for letter in word:
        if check_vowel(letter):
            return word + choice(suffix)
        else:
            first_vowel = re.search(r'[eaoiu]', word)
            if first_vowel:
                return word[first_vowel.start():] + word[:first_vowel.start()]+"ay"
            else:
                return word + "ay"


#real project measure and print time and log efficiency
class measurement():

    def __init__(self):
        self.start_time = time.time()

    def start_pc_check(self):
        ...
        memory = psutil.virtual_memory()
        used = memory.used
        print(f'memory used {used}')

    def report(self):
        total_time = time.time() - self.start_time
        print(f'time elapsed : {total_time}')

    def print_table(self):
        ...

if __name__ == "__main__":
    main()