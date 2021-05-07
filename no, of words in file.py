def line(a):
    f=open(a,"r")
    c=0
    for line in f:
        words=line.split()
        for word in words:
            c=c+1
    print("No.of words in file",c)

line("story.txt")