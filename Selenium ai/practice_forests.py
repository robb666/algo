import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

url = r'https://portal.generali.pl/auth/login?service=https%3A%2F%2Fportal.generali.pl%2Flogin%2Fcas'

# driver.get(url)
# driver.maximize_window()



# body = driver.find_element(By.XPATH, "//body")

# body_attr = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', body)
# attr_li = ['class', 'div', 'id', 'input', 'name', 'type', 'value', 'span']

# body_attr = body.get_attribute('var')






"""lambdatest"""

url1 = 'https://accounts.lambdatest.com/login'

# attr_li = ['id', 'type', 'class', 'name', 'aria-autocomplete', 'title', 'href', 'text', 'value', 'aria-label']

attr_tag = ['input', 'button']


driver.get(url1)
html = driver.page_source
# html = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div').get_attribute('innerHTML')

soup = BeautifulSoup(html, 'lxml')

for tag in attr_tag:
    # time.sleep(1)
    for attr in soup.find_all(tag):
        print(attr.attrs)
        print(tag)
        print(attr.attrs.get('id'))
        print(attr.attrs.get('type'))
        print(attr.attrs.get('class'))
        print(attr.attrs.get('name'))
        print(attr.attrs.get('aria-autocomplete'))
        print(attr.attrs.get('title'))
        print(attr.attrs.get('href'))
        print('text:')
        print(attr.text)
        print(attr.attrs.get('value'))
        print(attr.attrs.get('aria-label'))
        print('\n\n')
        # print(attr.text)
        # print(attr.value)
        # print(attr.href)
        # print(attr.contents)


