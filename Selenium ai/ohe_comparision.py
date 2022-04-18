import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier


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
    # df = pd.concat([el_name, df], axis=0)
    df.insert(0, 'element', df.name)
    df.element.fillna(df['value'], inplace=True)
    df.element.fillna(df['text'], inplace=True)
    # df.text = np.nan  # fillna didn't work
    ########
    df.to_csv('gen.csv')
    df = pd.read_csv('gen.csv', dtype=object)

    return df


def new_locator(driver, e, *, attr, element_row, value):
    if 'no such element' in str(e) or 'Unable to locate element' in str(e):
        df = scrp(driver)
        df = df.fillna('None')
        df = df.drop(['Unnamed: 0'], axis=1)

        to_test = pd.read_csv('Test.csv', dtype=object,
                              header=0, usecols=lambda c: c in df.columns)
        test = to_test.append(df)[df.columns].iloc[[element_row]]
        test = test.fillna('None')

        ohe = OneHotEncoder(sparse=False, handle_unknown='ignore')
        X_train = ohe.fit_transform(df.astype(str))
        X_test = ohe.transform(test)

        element_dict = dict(zip(df['element'].unique(), range(df['element'].nunique())))
        y_train = df['element'].replace(element_dict)

        rf = RandomForestClassifier(n_estimators=50, random_state=0)
        rf.fit(X_train, y_train)

        probabilities = rf.predict_proba(X_test)[0]
        el_attr = list(element_dict.keys())[np.argmax(probabilities)]

        selector = driver.find_element(By.XPATH, f"//*[@{attr}='{el_attr}']")
        if value:
            selector.send_keys(value)
        else:  # click
            selector.click()
