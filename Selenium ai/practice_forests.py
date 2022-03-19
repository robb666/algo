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

tags = ['input', 'button']
attr_li = ['element', 'tag', 'id', 'type', 'class', 'name', 'aria_autocomplete', 'title', 'href', 'text', 'value', 'aria_label']
ele_arr = ['Email', 'Password', 'LOGIN', 'Checkbox']


driver.get(url1)
html = driver.page_source

soup = BeautifulSoup(html, 'lxml')

arr = []
n = 0
for tag in tags:
    for attr in soup.find_all(tag):

        get_class = attr.get('class')[0] if len(attr.get('class')) > 0 else None
        arr.append((ele_arr[n], tag, attr.get('id'), attr.get('type'), get_class, attr.get('name'), attr.get('aria_autocomplete'),
                    attr.get('title'), attr.get('href'), attr.text, attr.get('value'), attr.get('aria_label')))
        n += 1

df = pd.DataFrame(arr)
df.columns = attr_li

print(df)
df.to_csv('file.csv')

Test = df.loc[(df['element'] == 'Password')]
Test.to_csv('Test.csv')


driver.quit()








        # df = pd.DataFrame({'ELEMENT': elements_arr,
        #                    'TAG': tag,
        #                    'ID': attr.get('id'),
        #                    'TYPE': attr.get('type'),
        #                    'CLASS': get_class,
        #                    'NAME': attr.get('name'),
        #                    'ARIA_AUTOCOMPLETE': attr.get('aria-autocomplete'),
        #                    'TITLE': attr.get('title'),
        #                    'HREF': attr.get('href'),
        #                    'TEXT': attr.get('text'),
        #                    'VALUE': attr.get('value'),
        #                    'ARIA_LABEL': '',
        #                    'PLACEHOLDER': attr.get('placeholder'),
        #                    })












    # print(df)

        # id_ = elements[0].attrs
        # print(id_)

        # for tag in attr_tag:
        # for attr in soup.find_all('button'):
        # print(dict)
        # print(attr.attrs)
        # # print(tag)
        # print(attr.attrs.get('id'))
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

