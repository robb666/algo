import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

df = pd.read_csv('file.csv')
test = pd.read_csv('Test.csv')










"""OneHotEncoder"""
oneh = OneHotEncoder(handle_unknown='ignore')

print(df)
print()
print(test)
print()

X_train_std = df
oneh.fit(X_train_std)


print(oneh.categories_)
print()


y_train_std = test
oneh.fit(y_train_std)
print(oneh.categories_)
print(oneh.transform(y_train_std).toarray())   # toarray() - zamiana na macierz

