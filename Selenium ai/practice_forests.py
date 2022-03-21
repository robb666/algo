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


# d = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
# df = pd.DataFrame(d)
# df.insert(0, 'tag', [1, 5, 9])
# print(df)


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
# c = f'{tag=}'.split('=')[0]
# print(len(c))
# df['tag'] = [tag] * len(arr)

df.insert(0, 'element', df.name)
df.insert(1, f'{tag=}'.split('=')[0], 'input')
print(df)
















# driver.quit()



# body = driver.find_element(By.XPATH, "//body")
# body_attr = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', body)
# attr_li = ['class', 'div', 'id', 'input', 'name', 'type', 'value', 'span']

