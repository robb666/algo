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

print(d, d[element_idx]/2)



# d = []
# for item in arr:
#     if item[1] == item[2]:
#         n += 1
#     arr1.append(n)
#
# print(arr1)

# print()
# print(rf.predict_proba(X_test))


# rf.predict([[0., 0., 1., 0., 0., 1., 0., 1., 0., 0., 1., 0., 0., 0., 1., 0., 1., 0., 0., 0., 1., 0., 0., 0., 1., 1.]])








# df = pd.read_csv('file.csv')
# df = df.fillna('None')
# df.drop(['element', 'disabled'], axis=1)
# X = df.iloc[:, :].values
# # print(X)
#
#
# label_encoder_X = LabelEncoder()
# X[:, 1] = label_encoder_X.fit_transform(X[:, 1])
#
# Y = pd.DataFrame(X)
#
#
# print(Y)
#
#
#
# oneh = OneHotEncoder(handle_unknown='ignore')
# X_train = oneh.fit(X)
#
# # print(X_train)
#
#
#
#
#
#
# # X_test = oneh.transform(y_train)
# # print(X_train)
#
#
#
# test = pd.read_csv('Test.csv')
# test = test.fillna('None')
# y_train = test.drop('element', axis=1)
#
# # print(test)
#
#
# rf = RandomForestClassifier(n_estimators=50, random_state=0)
# rf.fit(X_train, y_train)














# print(df)
# print()
#
# dummies = pd.get_dummies(df['element'])
#
# print(dummies)
#
# merged = pd.concat([df, dummies], axis=1)
#
# print(merged)
#
# final = merged.drop(['element', 'password'], axis=1)
#
# print(final)
#
# X = final.drop(['name'], axis='columns')
#
# print(X)
#
# y = final.name
#
# print(y)
#
#
# le = LabelEncoder()
# oneh = OneHotEncoder(handle_unknown='ignore')
#
#
# dfle = df
# # dfle = le.fit_transform(dfle[])
#
# X = oneh.fit_transform(X).toarray()
#
# # X.reshape(1,-1) # reshape to 1 row and -1 columns
#
# # print(X)
#
# twoh = OneHotEncoder(handle_unknown='ignore')
# y = twoh.fit_transform([y]).toarray()
#
# y = y.T
#
#
# rf = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)
#
# print(X)
# rf.fit(X, y)
#
#
# probabilites = list(rf.predict_proba(test)[0])
#
# print(probabilites)
#
#
# # print(oneh.transform(X).toarray())
#
#
#
# # print(dfle)
#
#
#
# model = LinearRegression()
#
# # model.fit(X, y)
#
#
#
#
#
#
#
#
#
#
# """OneHotEncoder"""
# oneh = OneHotEncoder(handle_unknown='ignore')
#
#
#
#
# X_train = df
# # print(oneh.transform(X_train).toarray())
#
#
#
#
#
#
#
# # print()
# #
# #
# # y_train = test
# #
# # oneh.fit_transform(y_train)
# # print(oneh.transform(y_train).toarray())
#
#






















