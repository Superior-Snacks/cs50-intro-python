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


def check_vowels(letter):
    vowels = ['e', 'a', 'o', 'i', 'u']
    ...


def check_word(word):
    ...


if __name__ == "__main__":
    main()