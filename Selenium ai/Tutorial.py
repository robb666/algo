import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder



df = pd.read_csv('tutorial.csv')

print(df)
print()

labelencoder = LabelEncoder()


ddf = pd.get_dummies(df)
print(ddf)
print()

# df.apply(LabelEncoder().fit_transform)
dfle = df.apply(LabelEncoder().fit_transform)
print(dfle)
print()


oneh = OneHotEncoder(handle_unknown='ignore').fit(dfle)

print(oneh.categories_)
print()

oneh_t = oneh.transform(dfle).toarray()

print(oneh_t)
