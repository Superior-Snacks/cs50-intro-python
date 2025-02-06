def main():

    pig_latin()


def pig_latin():
    # get input, sellect direction
    sentance = input(": ")
    direction = input("select in/out: ").lower()
    print(direction)

    if "in" == direction:
        translate_in(sentance)

    elif direction.lower:
        translate_out(sentance)
    
    else:
        print("incorrect formating")

def translate_in():
    #translate acording to rules
    print("translate in")

def translate_out():
    #fix
    print("translate out")


if __name__ == "__main__":
    main()