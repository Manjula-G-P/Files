def file(a):
    f=open(a,"r")
    return(f.readline())
print(file("data"))