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
from ohe_comparision import healed_locator



pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


driver = webdriver.Chrome()

url = r'https://portal.generali.pl/auth/login?service=https%3A%2F%2Fportal.generali.pl%2Flogin%2Fcas'

driver.get(url)

driver.maximize_window()

try:
    Element_email = driver.find_element(By.XPATH, f"//input[@name='usernameeer']")
    Element_email.send_keys('ubezpieczenia.magro@gmail.com')
except Exception as e:
    healed_locator(driver, e, attr='name', element_row=1, value='ubezpieczenia.magro@gmail.com')

    time.sleep(800)













# driver.execute_script(f"document.getElementById('{new_element}').value='ubezpieczenia.magro@gmail.com'")
# body = driver.find_element(By.XPATH, "//body")
# body_attr = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', body)
# attr_li = ['class', 'div', 'id', 'input', 'name', 'type', 'value', 'span']

