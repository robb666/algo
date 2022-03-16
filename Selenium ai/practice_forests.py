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

attr_li = ['class', 'div', 'id', 'input', 'name', 'type', 'value', 'span']

driver.get(url1)
html = driver.page_source

# data = driver.find_element(By.XPATH, "//body")


# body_attr = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', body)
# print(body_attr)
#
# for attr in attr_li:
#     a = body.get_attribute(attr)
#     print(a)

soup = BeautifulSoup(html, 'lxml')
for tag in soup.find_all():
    print(tag.extract())