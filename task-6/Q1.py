f = open("onelinefile.txt","r")
f2=open("Filename2.csv","a")
inp = f.read()
z=0
i=0
k=1
s=""
while i < len(inp):
    while not inp[i].isalpha():
        i+=1
    else:
        s += inp[z:i]+","
        z=i
    while i< len(inp) and inp[i].isalpha():
        i+=1
    else:
        k+=1
        if k%2==0:
            s += inp[z:i]+","
        else:
           s += inp[z:i]+"\n" 
        z=i
f2.write(s)   
    