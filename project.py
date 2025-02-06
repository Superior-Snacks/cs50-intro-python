def main():
    ...

if __name__ == "__main__":
    main()

def pig_latin():
    # get input, sellect direction
    sentance = input(":")
    direction = input("select: in/out")

    if direction.lower in ["in"]:
        translate_in(sentance)

    elif direction.lower in ["out"]:
        translate_out(sentance)
    
    else:
        print("incorrect formating")

def translate_in():
    #translate acording to rules
    ...

def translate_out():
    #fix
    ...