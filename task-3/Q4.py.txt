import pandas as pd
inp = input().split()
ser = pd.Series(inp)
for i in ser.keys():
    ser[i]=ser[i].capitalize()
print(" ".join(ser))
