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

"""lambdatest"""
driver = webdriver.Chrome()
url1 = 'https://accounts.lambdatest.com/login'
driver.get(url1)

# print(df)



driver.maximize_window()

new_element = ''

try:
    Element_email = driver.find_element(By.XPATH, "//input[@name='email']")
    Element_email.send_keys('ubezpieczenia.magro@gmail.com')

except Exception as e:
    print(e)

    tags = ['input', 'button']
    attr_li = ['element', 'tag', 'id', 'type', 'class', 'name', 'aria_autocomplete', 'title', 'href', 'text', 'value',
               'aria_label']
    ele_arr = ['Email', 'Password', 'LOGIN', 'Checkbox']

    html = driver.page_source

    soup = BeautifulSoup(html, 'lxml')

    arr = []
    n = 0

    for tag in tags:
        for attr in soup.find_all(tag):
            get_class = attr.get('class')[0] if len(attr.get('class')) > 0 else None
            arr.append((ele_arr[n], tag, attr.get('id'), attr.get('type'), get_class, attr.get('name'),
                        attr.get('aria_autocomplete'),
                        attr.get('title'), attr.get('href'), attr.text, attr.get('value'), attr.get('aria_label')))
            n += 1

    df = pd.DataFrame(arr)
    df.columns = attr_li

    df.to_csv('file.csv')
    print(df)
    # Test = df.loc[(df['element'] == 'Email')]
    Test = df.iloc[0]['name']
    # Test.to_csv('Test.csv')
    #
    # from rand_forests_sel import predict_elements, get_predicted_element
    # from queue import PriorityQueue
    #
    # scores, element_name, test_df = predict_elements()
    # print(scores, element_name)
    #
    # queue = PriorityQueue()
    #
    # predicted_element = get_predicted_element(scores, queue)[1]
    #
    # pred_dict = df.loc[(df['element'] == predicted_element)]
    #
    # new_element = pred_dict['id'].values[0]
    #
    # print(new_element)

    # new_locator = f"//*[@name='{new_element}']"
    new_locator = f"//*[@name='{Test}']"
    print(new_locator)

    # driver.execute_script(f"document.getElementById('{new_element}').value='ubezpieczenia.magro@gmail.com'")
    driver.find_element(By.XPATH, new_locator).send_keys(login)

    print('wpisane!!!')
    # time.sleep(50)



def EnterUserName(driver):
    try:
        # Element_email = driver.find_element_by_xpath("//input[@name='email']")
        Element_email = driver.find_element(By.XPATH, "//input[@name='email']")
        Element_email.send_keys(login)
    except Exception as e:pass

        # if str(e) in 'no such element' or 'Unable to locate element':
        #     Element_email = Model.InvokeSelfHealing(e, driver, locators.email)
    # Element_email.send_keys(credentials.Email)
    # Element_email.send_keys('ubezpieczenia.magro@gmail.com')
    print("Enter username Executed")


def EnterPasswors(driver):
    try:
        # Element_passwors = driver.find_element_by_id("password")
        Element_passwors = driver.find_element(By.ID, "password")
        Element_passwors.send_keys(passw)
    except Exception as e:pass
        # if str(e) in 'no such element' or 'Unable to locate element':
        #     Element_email = Model.InvokeSelfHealing(e, driver, locators.email)

    # Element_email.send_keys(credentials.Password)
    # Element_passwors.send_keys('Q75dcJCvMbeaB7x')
    print("Enter password Executed")


def ClickOnSignIn(driver):
    try:
        # Element_click = driver.find_element_by_xpath("//button[contains(text(), 'Login')]")
        Element_click = driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
        Element_click.click()
        print("Enter clickon SignIn Executed")
    except Exception as e:
        print(e)

    #     if str(e) in 'no such element' or 'Unable to locate element':
    #         Element_click = Model.InvokeSelfHealing(e, driver, locators.clickBtn)
    # Element_click.click()
    # print("Enter clickon SignIn Executed")



# GetElements(driver)
# driver.maximize_window()
# EnterUserName(driver)
EnterPasswors(driver)
ClickOnSignIn(driver)
print("Test complete")
time.sleep(9999)
# driver.quit()
