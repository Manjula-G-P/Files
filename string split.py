a="my name is kumar"
b1=list(a)
n=input("enter a letter:")
i=0
b=[]
while i<len(b1):
    s=""
    while True:
        if b1[i]==n:
            b.append(s)
            b=b+[b1[i]]
            i=i+1
            break
        else:
            s=s+str(b1[i])
            i=i+1
        if i==len(b1):
            b.append(s)
            break
print(b)
