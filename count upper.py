def upper_count():
    f=open("notes.txt","r")
    data=f.read()
    c=0
    for letter in data:
        if letter.isupper():
            c=c+1
    print(c)
upper_count()
