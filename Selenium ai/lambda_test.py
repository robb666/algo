import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from creds import login, passw
import re

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

"""lambdatest"""
driver = webdriver.Chrome()
url1 = 'https://accounts.lambdatest.com/login'
driver.get(url1)



html = driver.page_source
soup = BeautifulSoup(html, 'lxml')
tags = ['input', 'button']

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
Test = df.loc[(df['element'] == 'email')]
print(Test)
Test.to_csv('Test.csv')

driver.maximize_window()

try:
    Element_email = driver.find_element(By.XPATH, "//input[@name='email']")
    Element_email.send_keys('ubezpieczenia.magro@gmail.com')

except Exception as e:

    el_from_e = eval(re.search('({.+})', e.args[0]).group())
    selector = el_from_e['selector']
    print(selector)


    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    tags = ['input', 'button']

    arr = []
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
    df.element.fillna(df['type'], inplace=True)

    df.to_csv('file.csv') ### Add name_email to the model!!!
    print(df)

    # from rand_forests_sel import predict_elements, get_predicted_element
    from ohe_comparision import new_locator
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
    #
    # new_locator = f"//*[@name='{new_element}']"
    # # new_locator = f"//*[@name='{Test}']"
    # print(new_locator)

    # driver.execute_script(f"document.getElementById('{new_element}').value='ubezpieczenia.magro@gmail.com'")
    driver.find_element(By.XPATH, new_locator).send_keys(login)

    print('wpisane!!!')
    # time.sleep(50)

#
#
#
# def EnterUserName(driver):
#     try:
#         # Element_email = driver.find_element_by_xpath("//input[@name='email']")
#         Element_email = driver.find_element(By.XPATH, "//input[@name='email']")
#         Element_email.send_keys(login)
#     except Exception as e:pass
#
#         # if str(e) in 'no such element' or 'Unable to locate element':
#         #     Element_email = Model.InvokeSelfHealing(e, driver, locators.email)
#     # Element_email.send_keys(credentials.Email)
#     # Element_email.send_keys('ubezpieczenia.magro@gmail.com')
#     print("Enter username Executed")
#
#
# def EnterPasswors(driver):
#     try:
#         # Element_passwors = driver.find_element_by_id("password")
#         Element_passwors = driver.find_element(By.ID, "password")
#         Element_passwors.send_keys(passw)
#     except Exception as e:pass
#         # if str(e) in 'no such element' or 'Unable to locate element':
#         #     Element_email = Model.InvokeSelfHealing(e, driver, locators.email)
#
#     # Element_email.send_keys(credentials.Password)
#     # Element_passwors.send_keys('Q75dcJCvMbeaB7x')
#     print("Enter password Executed")
#
#
# def ClickOnSignIn(driver):
#     try:
#         # Element_click = driver.find_element_by_xpath("//button[contains(text(), 'Login')]")
#         Element_click = driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
#         Element_click.click()
#         print("Enter clickon SignIn Executed")
#     except Exception as e:
#         print(e)
#
#     #     if str(e) in 'no such element' or 'Unable to locate element':
#     #         Element_click = Model.InvokeSelfHealing(e, driver, locators.clickBtn)
#     # Element_click.click()
#     # print("Enter clickon SignIn Executed")
#
#
#
# # GetElements(driver)
# # driver.maximize_window()
# # EnterUserName(driver)
# EnterPasswors(driver)
# ClickOnSignIn(driver)
# print("Test complete")
# time.sleep(9999)
# # driver.quit()
