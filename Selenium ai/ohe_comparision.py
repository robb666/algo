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

# Fill the NaN values with 'None'
df = df.fillna('None')

# df = df.drop(['Unnamed: 0', 'disabled'], axis=1)  # lambda_test
df = df.drop(['Unnamed: 0'], axis=1)


ohe = OneHotEncoder(sparse=False, handle_unknown='ignore')
print(df)
X_train = ohe.fit_transform(df)

# # creating a dictionary of elements
# element_dict = dict(zip(df['element'].unique(), range(df['element'].nunique())))

# {'_token': 0, 'email': 1, 'password': 2, 'LOGIN': 3, 'on': 4}

# # # replacing dictionary values into dataframe as we need to convert this into numbers
# y_train = df['element'].replace(element_dict)

test = test.fillna('None')
test = test.drop(['Unnamed: 0'], axis=1)

X_test = ohe.transform(test)


d = {}
n = 0
for idx, i in enumerate(range(len(X_train))):
    for j in range(len(X_train[0])):
        if X_train[i][j] == X_test[0][j]:
            n += 1
            d[idx] = n
    n = 0

element_idx = max(d, key=d.get)

new_element = df.iloc[element_idx]['element']

new_locator = f"//*[@name='{new_element}']"

print(new_locator)






















