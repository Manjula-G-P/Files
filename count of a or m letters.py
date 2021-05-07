def count():
    f=open("story.txt","r")
    data=f.read()
    c=0
    c1=0
    for letter in data:
        if letter=="a" or letter=="A":
            c=c+1
        elif letter=="m" or letter=="M":
            c1=c1+1
    print("No.of a or A:",c)
    print("No.of m or M:",c1)
count()