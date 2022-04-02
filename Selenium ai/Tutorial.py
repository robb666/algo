import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder



df1 = pd.DataFrame({'country': ['USA', 'France'], 'language': ['EN', 'FR']})
ohe = OneHotEncoder(sparse=False)
X_train = ohe.fit_transform(df1)
print(X_train)


df2 = pd.DataFrame({'country': ['USA'], 'language': ['EN']})
X_test = ohe.transform(df2)
print(X_test)




rf = RandomForestClassifier(n_estimators=100, random_state=0)

for row in X_train:
    rf.fit([row], X_test)

print()
print(rf.predict(X_test))



# X_train
# array([[0., 1., 1., 0.],
#        [1., 0., 0., 1.]])

# X_test
# array([[0., 1., 1., 0.]])  # same shape as X_train






# df = pd.read_csv('tutorial.csv')
#
# print(df)
# print()
#
# labelencoder = LabelEncoder()
#
#
# ddf = pd.get_dummies(df)
# print(ddf)
# print()
#
# # df.apply(LabelEncoder().fit_transform)
# dfle = df.apply(LabelEncoder().fit_transform)
# print(dfle)
# print()
#
#
# oneh = OneHotEncoder(handle_unknown='ignore').fit(dfle)
#
# print(oneh.categories_)
# print()
#
# oneh_t = oneh.transform(dfle).toarray()
#
# print(oneh_t)
