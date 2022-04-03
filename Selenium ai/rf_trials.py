import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.compose import ColumnTransformer

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

df = pd.read_csv('file.csv')
df = df.fillna('None')
df = df.drop(['Unnamed: 0', 'disabled'], axis=1)
print(df)

ohe = OneHotEncoder(sparse=False, handle_unknown='ignore')
X_train = ohe.fit_transform(df)
print(X_train)


test = pd.read_csv('Test.csv')
test = test.fillna('None')
test = test.drop(['Unnamed: 0'], axis=1)
print(test)

X_test = ohe.transform(test)
print(X_test)

rf = RandomForestClassifier(n_estimators=100, random_state=0)

d = {}
n = 0
for idx, i in enumerate(range(len(X_train))):
    for j in range(len(X_train[0])):
        if X_train[i][j] == X_test[0][j]:
            n += 1
            d[idx] = n
    n = 0

element_idx = max(d, key=d.get)

print(d, element_idx)



