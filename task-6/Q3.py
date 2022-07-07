from collections import Counter
import pandas as pd
import re

f1 = open("about.txt","r")                  #loads the file
s = f1.read()                               #readsthe file
sl = re.split("[^a-zA-z0-9]",s)             #converts Paragragh to list


# Using Counter
word_list = list(filter(lambda x : len(x)>=6,sl))       #filter words whose length is >= 6
print(word_list)

c = Counter(word_list)                                  #Creates a Counter that tracks number of occurence of element in list/set/tuple/string

print(c.most_common(1)[0][0])                           #prints the most repeating word with lenght >= 6

# Using Pandas

df   = pd.DataFrame({"words" : sl})

df = df[df.words.str.len() >= 6]                        #filter words whose length is >= 6

df2 = pd.DataFrame(data=df["words"].value_counts())     #counts th number of grouped value of DF i.e. no of occurence of word in single column of DF

print(df2[df2["words"]== df2.words.max()].index[0])     #prints the most repeating word with lenght >= 6




