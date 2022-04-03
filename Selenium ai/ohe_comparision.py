import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from queue import PriorityQueue


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


# reading the required files into python using pandas
df = pd.read_csv('file.csv', dtype=object)
test = pd.read_csv('Test.csv', dtype=object)

print(df)

df = df.fillna('None')

df = df.drop(['Unnamed: 0'], axis=1)

ohe = OneHotEncoder(sparse=False, handle_unknown='ignore')
# print(df)
X_train = ohe.fit_transform(df)
print(X_train[0])

test = test.fillna('None')
test = test.drop(['Unnamed: 0'], axis=1)
print(test)

X_test = ohe.transform(test)
print(X_test[0])


d = {}
n = 0
for idx, i in enumerate(range(len(X_train))):
    for j in range(len(X_train[0])):
        if X_train[i][j] == X_test[0][j]:
            n += 1
            d[idx] = n
    n = 0

print()

print(d)
element_idx = max(d, key=d.get)

new_element = df.iloc[element_idx]['element']

new_locator = f"//*[@name='{new_element}']"

print(new_locator)






















