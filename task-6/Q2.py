import pandas as pd
import numpy as np

df = pd.read_csv("Q2-Dataset.csv")
df=pd.DataFrame(df)
print(df.head())
df["Alley"] = df["Alley"].fillna("no alley")
df["LotFrontage"] = df["LotFrontage"].fillna(0)
df["BsmtFinType2"] = df["BsmtFinType2"].fillna("No")
df["BsmtFinType1"] = df["BsmtFinType1"].fillna("No")
df["BsmtExposure"] = df["BsmtExposure"].fillna("No")
df["BsmtCond"] = df["BsmtCond"].fillna("No")
df["BsmtQual"] = df["BsmtQual"].fillna("No")
df.to_csv("Q2-new-data.csv",index=False)
print(df)