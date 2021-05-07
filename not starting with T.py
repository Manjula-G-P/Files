def line_count(a):
    f=open(a,"r")
    c=0
    for line in f:
        if line[0]!="T":
            c=c+1
    print("No.of lines not start with T:",c)
(line_count("story.txt"))