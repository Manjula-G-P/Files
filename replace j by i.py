def replace():
    f=open("words.txt","r")
    data=f.read()
    for letter in data:
        if letter=="J":
            print("I",end="")
        else:
            print(letter,end="")
    print(f.read())
    f.close()

replace()