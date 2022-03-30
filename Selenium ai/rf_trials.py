import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


df = pd.read_csv('file.csv')

test = pd.read_csv('Test.csv')

df = df.fillna('None')

print(df)
print()

dummies = pd.get_dummies(df['element'])

print(dummies)

merged = pd.concat([df, dummies], axis=1)

print(merged)

final = merged.drop(['element', 'password'], axis=1)

print(final)

X = final.drop(['name'], axis='columns')

print(X)

y = final.name

print(y)

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
oneh = OneHotEncoder(handle_unknown='ignore')


dfle = df
# dfle = le.fit_transform(dfle[])

X = oneh.fit_transform(X).toarray()



# print(X)

twoh = OneHotEncoder(handle_unknown='ignore')
twoh.fit_transform(y).toarray()




# print(oneh.transform(X).toarray())



# print(dfle)



model = LinearRegression()

# model.fit(X, y)










"""OneHotEncoder"""
oneh = OneHotEncoder(handle_unknown='ignore')




X_train = df
# print(oneh.transform(X_train).toarray())







# print()
#
#
# y_train = test
#
# oneh.fit_transform(y_train)
# print(oneh.transform(y_train).toarray())
























