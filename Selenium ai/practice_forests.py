import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from creds import login, passw

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


driver = webdriver.Chrome()

url = r'https://portal.generali.pl/auth/login?service=https%3A%2F%2Fportal.generali.pl%2Flogin%2Fcas'

driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, 'lxml')
tags = ['input']  # to uzupełniać..?
# el_name = ['LOGIN', 'PASSW', 'LOG_BUTTON']

arr = []
# tst = []
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

# print(df)
Test = df.loc[(df['element'] == 'username')]
print(Test)
Test.to_csv('Test.csv')
# Test.to_sql('Testdb')



# driver.maximize_window()


locator = 'username'
try:
    Element_email = driver.find_element(By.XPATH, f"//input[@name='{locator}']")
    Element_email.send_keys('ubezpieczenia.magro@gmail.com')

except Exception as e:
    el_from_e = eval(re.search('({.+})', e.args[0]).group())
    selector = el_from_e['selector']
    print(selector)

    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    tags = ['input']  # to uzupełniać..?
    # el_name = ['LOGIN', 'PASSW', 'LOG_BUTTON']

    arr = []
    # tst = []
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

    df.to_csv('file.csv')
    print(df)

    # from rand_forests_sel import predict_elements, get_predicted_element
    # from queue import PriorityQueue
    from ohe_comparision import new_locator

    # scores, element_name, test_df = predict_elements()
    # print(scores)
    # print(element_name)
    # print(test_df)
    #
    # queue = PriorityQueue()
    #
    # predicted_element = get_predicted_element(scores, queue)[1]
    # print(predicted_element)
    #
    # # print(scores)
    # # predicted_element = scores[0][0]
    #
    # new_locator = f"//*[@name='{predicted_element}']"


    # driver.execute_script(f"document.getElementById('{new_element}').value='ubezpieczenia.magro@gmail.com'")
    driver.find_element(By.XPATH, new_locator).send_keys(login)
    #
    print('wpisane!!!')
    time.sleep(50)










# driver.quit()



# body = driver.find_element(By.XPATH, "//body")
# body_attr = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', body)
# attr_li = ['class', 'div', 'id', 'input', 'name', 'type', 'value', 'span']

