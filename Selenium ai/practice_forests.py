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

html = driver.page_source
soup = BeautifulSoup(html, 'lxml')


arr = []
tag = 'input'
# print(f'{tag=}'.split('=')[0])
for tag in soup.find_all(tag):
    # print(tag)
    # for attr in tag.attrs:
    #     # print(attr)
    #     if isinstance(tag[attr], list):
    #         arr.append((attr, tag[attr][0]))
    arr.append(tag.attrs)

print(arr)

df = pd.DataFrame.from_records(arr)


df.insert(0, f'{tag=}'.split('=')[0], 'input')  # tag !!!???
df.insert(0, 'element', df.name)
df.element.fillna(df['value'], inplace=True)
print(df)

df.to_csv('file.csv')

Test = df.loc[(df['element'] == 'password')]
Test.to_csv('Test.csv')














# driver.quit()



# body = driver.find_element(By.XPATH, "//body")
# body_attr = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', body)
# attr_li = ['class', 'div', 'id', 'input', 'name', 'type', 'value', 'span']

