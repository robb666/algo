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




"""OneHotEncoder"""
oneh = OneHotEncoder(handle_unknown='ignore')





# X_train = df.drop('element', axis=1)
X_train = df
oneh.fit(X_train)
# oneh.transform(X_train).toarray()
print(oneh.transform(X_train).toarray())

print()



# # returns all the unique Elements stored in the training data
# df['element'].unique()
# # creating a dictionary of elements
# element_dict = dict(zip(df['element'].unique(), range(df['element'].nunique())))
# y_train = df['element'].replace(element_dict)


y_train = test

oneh.fit(y_train)
print(oneh.transform(y_train).toarray())


# print(train.fit_transform(train).toarray())



# oneh.fit(y_train)
# oneh.transform(y_train).toarray()
# print(oneh.transform(y_train).toarray())

