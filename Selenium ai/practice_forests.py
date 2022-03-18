import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

# driver = webdriver.Chrome()

url = r'https://portal.generali.pl/auth/login?service=https%3A%2F%2Fportal.generali.pl%2Flogin%2Fcas'

# driver.get(url)
# driver.maximize_window()



# body = driver.find_element(By.XPATH, "//body")

# body_attr = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', body)
# attr_li = ['class', 'div', 'id', 'input', 'name', 'type', 'value', 'span']

# body_attr = body.get_attribute('var')






"""lambdatest"""
driver = webdriver.Chrome()
url1 = 'https://accounts.lambdatest.com/login'

attr_tag = ['input', 'button']
attr_li = ['ELEMENT', 'TAG', 'ID', 'TYPE', 'CLASS', 'NAME', 'ARIA_AUTOCOMPLETE', 'TITLE', 'HREF', 'TEXT', 'VALUE', 'ARIA_LABEL']
elements_arr = ['email', 'password', 'LOGIN', 'checkbox']

# d = dict(attr_li=np.array(attr_li),
#          attr_tag=np.array(attr_tag),
#          elements_arr=np.array(elements_arr),
#          )


driver.get(url1)
html = driver.page_source

soup = BeautifulSoup(html, 'lxml')

# df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in d.items()]))
print(soup.find_all('button'))

# for tag in attr_tag:
for attr in soup.find_all('button'):
    # print(dict)
    # print(attr.attrs)
    # # print(tag)
    print(attr.attrs.get('id'))
    # print(attr.id)
    # print(attr.attrs.get('type'))
    # print(attr.attrs.get('class'))
    # print(attr.attrs.get('name'))
    # print(attr.attrs.get('aria-autocomplete'))
    # print(attr.attrs.get('title'))
    # print(attr.attrs.get('href'))
    # print('text:')
    # print(attr.text)
    # print(attr.value)
    # print(attr.attrs.get('value'))
    # print(attr.attrs.get('aria-label'))
    # print('\n\n')
    # print(attr.text)
    # print(attr.value)
    # print(attr.href)
    # print(attr.contents)


    df = pd.DataFrame({'ELEMENT': elements_arr,
                       # 'TAG': tag,
                       'ID': attr.attrs.get('id'),
                       'TYPE': attr.attrs.get('type'),
                       'CLASS': '2',
                       'NAME': attr.attrs.get('name'),
                       'ARIA_AUTOCOMPLETE': attr.attrs.get('aria-autocomplete'),
                       'TITLE': attr.attrs.get('title'),
                       'HREF': attr.attrs.get('href'),
                       'TEXT': '',
                       'VALUE': attr.attrs.get('value'),
                       # 'ARIA_LABEL': '',
                       'PLACEHOLDER': attr.attrs.get('placeholder'),
                       })


    print(df)


