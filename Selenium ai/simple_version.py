import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from creds import login, passw

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


driver = webdriver.Chrome()

url = r'https://portal.generali.pl/auth/login?service=https%3A%2F%2Fportal.generali.pl%2Flogin%2Fcas'

driver.get(url)


def no_such_element(*, e, row, attr, value):
    """Useful when attribute changes name but not order within tags.
       This function can send_keys or click to an element.
       The 'attr' is column of the DataFrame so simply specify
       row by index and column by name of the element.
       If value=False then function will send a click."""

    if 'no such element' in str(e) or 'Unable to locate element' in str(e):
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        tags = ['input']  # Fill in tags.

        arr = []
        for tag in tags:
            for element in soup.find_all(tag):
                arr.append({'tag': tag} | {'text': element.text} | element.attrs)

        df = pd.DataFrame.from_records(arr)
        df.insert(0, 'element', df.name)
        df.element.fillna(df['value'], inplace=True)
        df.element.fillna(df['text'], inplace=True)
        # print(df)
        el_attr = df.iloc[row][attr]
        selector = driver.find_element(By.XPATH, f"//*[@{attr}='{el_attr}']")
        if value:
            selector.send_keys(value)
        else:  # click
            selector.click()


try:
    Element_email = driver.find_element(By.XPATH, f"//input[@name='usernamee']")
    Element_email.send_keys('ubezpieczenia.magro@gmail.com')

except Exception as e:
    no_such_element(e=e, row=0, attr='name', value='ubezpieczenia.magro@gmail.com')
