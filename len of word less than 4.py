def display(a):
    f=open(a,"r")
    for line in f:
        words=line.split()
        for word in words:
            if len(word)<4:
                print(word)
                
display("story.txt")