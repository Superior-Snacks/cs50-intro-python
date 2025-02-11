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
    return output[1:]


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
        self.cpu_bin = []
        self.memory_bin = []

    def start_pc_check(self):
        memory = psutil.virtual_memory().used
        cpu = psutil.cpu_percent(interval=1)
        self.memory_bin.append(memory)
        self.cpu_bin.append(cpu)


    def report(self):
        total_time = time.time() - self.start_time
        print(f'time elapsed : {total_time}')

    def print_table(self):
        ...

if __name__ == "__main__":
    main()