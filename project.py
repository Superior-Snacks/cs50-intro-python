def main():

    pig_latin()


def pig_latin():
    # get input, sellect direction
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
    ...


def check_word(word):
    ...


if __name__ == "__main__":
    main()