import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from queue import PriorityQueue
import re

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


# reading the required files into python using pandas
df = pd.read_csv('file.csv', dtype=object)

to_test = pd.read_csv('Test.csv', dtype=object, header=0, usecols=lambda c: c in df.columns)
test = to_test.append(df)[df.columns].iloc[:1, :]

print(test)

df = df.fillna('None')

df = df.drop(['Unnamed: 0'], axis=1)


ohe = OneHotEncoder(sparse=False, handle_unknown='ignore')
# print(df)
X_train = ohe.fit_transform(df)
# print(X_train)

test = test.fillna('None')
test = test.drop(['Unnamed: 0'], axis=1)
# print(test)

X_test = ohe.transform(test)
print(X_test[0])

element_dict = dict(zip(df['element'].unique(), range(df['element'].nunique())))
print(element_dict)
y_train = df['element'].replace(element_dict)

from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators=50, random_state=0)
rf.fit(X_train, y_train)

probabilities = rf.predict_proba(X_test)[0]
print(probabilities)

idx = np.argmax(probabilities)
new_element = df.iloc[idx]['element']

print(new_element)
new_locator = f"//*[@name='{new_element}']"






# d = {}
# n = 0
# for idx, i in enumerate(range(len(X_train))):
#     for j in range(len(X_train[0])):
#         if X_train[i][j] == X_test[0][j]:
#             n += 1
#             d[idx] = n
#     n = 0
#
# print()
#
# print(d)
# element_idx = max(d, key=d.get)
#
# new_element = df.iloc[element_idx]['element']
#
# new_locator = f"//*[@name='{new_element}']"
#
# print(new_locator)






















