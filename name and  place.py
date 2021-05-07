def n_p():
    f=open("data.txt","r")
    for line in f:
        a=line.split()
        if a[1]=="delhi":
            f=open("delhi.txt","a+")
            f.write(a[0])
            f.write("\n")
        elif a[1]=="shimla":
            f=open("shimla.txt","a+")
            f.write(a[0])
            f.write("\n")
        else:
            f=open("others.txt","a+")
            f.write(a[0])
            f.write("\n")
n_p()