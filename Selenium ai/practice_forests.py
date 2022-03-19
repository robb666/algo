import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from rand_forests_sel import predict_elements


# driver = webdriver.Chrome()

# url = r'https://portal.generali.pl/auth/login?service=https%3A%2F%2Fportal.generali.pl%2Flogin%2Fcas'

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



def EnterUserName(driver):
    try:
        Element_email = driver.find_element_by_xpath("//input[@name='email']")
        Element_email.send_keys('')
    except Exception as e:pass

        # if str(e) in 'no such element' or 'Unable to locate element':
        #     Element_email = Model.InvokeSelfHealing(e, driver, locators.email)
    # Element_email.send_keys(credentials.Email)
    # Element_email.send_keys('ubezpieczenia.magro@gmail.com')
    print("Enter username Executed")


def EnterPasswors(driver):
    try:
        Element_passwors = driver.find_element_by_id("password")
        Element_passwors.send_keys('')
    except Exception as e:pass
        # if str(e) in 'no such element' or 'Unable to locate element':
        #     Element_email = Model.InvokeSelfHealing(e, driver, locators.email)

    # Element_email.send_keys(credentials.Password)
    # Element_passwors.send_keys('Q75dcJCvMbeaB7x')
    print("Enter password Executed")


def ClickOnSignIn(driver):
    try:
        Element_click = driver.find_element_by_xpath("//button[contains(text(), 'Login')]")
        Element_click.click()
    except Exception as e:
        print(e)

    #     if str(e) in 'no such element' or 'Unable to locate element':
    #         Element_click = Model.InvokeSelfHealing(e, driver, locators.clickBtn)
    # Element_click.click()
    print("Enter clickon SignIn Executed")




# GetElements(driver)
driver.maximize_window()
EnterUserName(driver)
EnterPasswors(driver)
ClickOnSignIn(driver)
time.sleep(1)
print("Test complete")

# driver.quit()

