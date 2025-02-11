from random import choice
import re
import psutil
import time

def main():
    manage = measurement(pig_latin)
    manage.run_and_mointor()


def pig_latin():
    # get input
    #sentance = input(": ")
    x = 1
    for x in range(10000):
        x += 99999999 ** 999
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

    def __init__(self, project):
        self.cpu_bin = []
        self.memory_bin = []
        self.time_bin = []
        self.project = project

    def run_and_mointor(self):
        cpu_count = psutil.cpu_count(logical=True)
        process = psutil.Process()

        for x in range(5):
            self.start_time = time.time()

            cpu_before = process.cpu_times().user + process.cpu_times().system
            memory_before = process.memory_info().rss / (1024 ** 2)

            # Start program
            self.project()

            total_time = time.time() - self.start_time

            memory_after = process.memory_info().rss / (1024 ** 2)
            cpu_after = process.cpu_times().user + process.cpu_times().system

            cpu = max(0, cpu_after - cpu_before)
            memory = memory_after - memory_before
            self.memory_bin.append(memory)
            self.cpu_bin.append(cpu)
            self.time_bin.append(total_time)

        self.report()


    def report(self):
        average_time = sum(self.time_bin) / len(self.time_bin) if self.time_bin else 0
        average_cpu = sum(self.cpu_bin) / len(self.cpu_bin) / average_time * 100 if self.cpu_bin else 0
        average_memory = sum(self.memory_bin) / len(self.memory_bin) if self.memory_bin else 0
        print(f'average time elapsed : {average_time:.2f}')
        print(f'average cpu usage: {average_cpu:.2f}%') # fix this is prolly worng
        print(f'average memory usage: {average_memory:.2f}')

    def print_table(self):
        ...

if __name__ == "__main__":
    main()
