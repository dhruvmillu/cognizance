f = int(input("First Number: "))
l = int(input("Last Number: "))
inp=[]
for i in range(f,l):
    
    for _ in range(5):
        inp.insert(5*(i-f)+(i-f),0)
    inp.insert(5*(i-f)+(i-f),i)
inp.insert(5*(l-f)+(l-f),l)
print(inp)
