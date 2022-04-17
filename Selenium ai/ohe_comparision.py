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
print(df.columns)

# test = pd.read_csv('Test.csv', dtype=object, header=0, usecols=df.columns, engine='python')

test = pd.DataFrame(columns=df.columns)
print(test)



# usecols=lambda c: c in df.columns

df = df.fillna('None')

df = df.drop(['Unnamed: 0'], axis=1)


ohe = OneHotEncoder(sparse=False, handle_unknown='ignore')
# print(df)
X_train = ohe.fit_transform(df)
# print(X_train)

test = test.fillna('None')
test = test.drop(['Unnamed: 0'], axis=1)
# print(test)




# try:
#     X_test = ohe.transform(test)
#     print(X_test[0])
# except Exception as e:
#     print(e)
#     if 'names unseen at fit' in str(e):
#         unseen_feature = re.search('Feature names unseen at fit time:\n- (\w+)', e.args[0]).group(1)
#         print('unseen_feature')
#         print(unseen_feature)
#         test = test.drop([unseen_feature], axis=1)
#         X_test = ohe.transform(test)
#
#     elif 'names seen at fit' in str(e):
#         missing_feature = re.search('Feature names seen at fit time, yet now missing:\n- (\w+)', e.args[0]).group(1)
#         print('missing_feature')
#         print(missing_feature)
#         missing_feature = pd.Series(missing_feature)
#         test = pd.concat([test, missing_feature], axis=1)
#         print(test)
#         # test = test.drop([missing_feature], axis=1)
#         X_test = ohe.transform(test)
#
#
#
#
# element_dict = dict(zip(df['element'].unique(), range(df['element'].nunique())))
# print(element_dict)
# y_train = df['element'].replace(element_dict)
#
# from sklearn.ensemble import RandomForestClassifier
#
# rf = RandomForestClassifier(n_estimators=50, random_state=0)
# rf.fit(X_train, y_train)
#
# probabilities = rf.predict_proba(X_test)[0]
# print(probabilities)
#
# idx = np.argmax(probabilities)
# new_element = df.iloc[idx]['element']
#
# print(new_element)
# new_locator = f"//*[@name='{new_element}']"






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






















