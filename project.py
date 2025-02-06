def main():

    pig_latin()


def pig_latin():
    # get input, sellect direction
    sentance = input(":")
    direction = input("select: in/out")

    if "in" in direction.lower:
        translate_in(sentance)

    elif "out" in direction.lower:
        translate_out(sentance)
    
    else:
        print("incorrect formating")

def translate_in():
    #translate acording to rules
    ...

def translate_out():
    #fix
    ...



if __name__ == "__main__":
    main()