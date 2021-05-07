def hash_display():
    f=open("data","r")
    data=f.read()
    for letter in data:
        print(letter,end="*")
hash_display()