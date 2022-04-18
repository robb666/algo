import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from queue import PriorityQueue
import re

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

def scrp(driver):

    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    tags = ['input']  # to uzupełniać..?
    # el_name = ['LOGIN', 'PASSW', 'LOG_BUTTON']

    arr = []
    for tag in tags:
        for element in soup.find_all(tag):
            arr.append({'tag': tag} |
                       {'text': element.text} |
                       element.attrs)

    df = pd.DataFrame.from_records(arr)
    # el_name = pd.DataFrame({'element': el_name})
    # df = pd.concat([el_name, df], axis=1)
    df.insert(0, 'element', df.name)
    df.element.fillna(df['value'], inplace=True)
    df.element.fillna(df['text'], inplace=True)
    # df.text = np.nan  # fillna didn't work

    ########
    df.to_csv('file.csv')
    df = pd.read_csv('file.csv', dtype=object)
    print(df.dtypes)
    return df


def new_locator(driver):
    df = scrp(driver)
    df = df.fillna('None')
    # df = df.drop(['Unnamed: 0'], axis=1)
    print(df)

    to_test = pd.read_csv('Test.csv', dtype=object,
                          header=0, usecols=lambda c: c in df.columns)
    test = to_test.append(df)[df.columns].iloc[:1, :]
    test = test.fillna('None')
    # test = test.drop(['Unnamed: 0'], axis=1)
    print(test)





    ohe = OneHotEncoder(sparse=False, handle_unknown='ignore')
    X_train = ohe.fit_transform(df.astype(str))

    X_test = ohe.transform(test)
    print(X_test[0])

    element_dict = dict(zip(df['element'].unique(), range(df['element'].nunique())))
    print(element_dict)
    y_train = df['element'].replace(element_dict)

    rf = RandomForestClassifier(n_estimators=50, random_state=0)
    rf.fit(X_train, y_train)

    probabilities = rf.predict_proba(X_test)[0]
    print(probabilities)

    new_element = list(element_dict.keys())[np.argmax(probabilities)]
    print(new_element)

    new_locator = f"//*[@name='{new_element}']"

    return new_locator





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






















