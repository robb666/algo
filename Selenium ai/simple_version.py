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

driver.maximize_window()


def no_such_element(e):
    if 'no such element' in str(e) or 'Unable to locate element' in str(e):
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        tags = ['input']  # tu uzupełniać..

        arr = []
        for tag in tags:
            for element in soup.find_all(tag):
                arr.append({'tag': tag} |
                           {'text': element.text} |
                           element.attrs)

        df = pd.DataFrame.from_records(arr)

        df.insert(0, 'element', df.name)
        df.element.fillna(df['value'], inplace=True)
        df.element.fillna(df['text'], inplace=True)
        print(df)

        element = df.iloc[0]['name']
        driver.find_element(By.XPATH, f"//*[@name='{element}']").send_keys(login)


try:
    Element_email = driver.find_element(By.XPATH, f"//input[@name='usernamee']")
    Element_email.send_keys('ubezpieczenia.magro@gmail.com')

except Exception as e:
    no_such_element(e)
    time.sleep(6)
