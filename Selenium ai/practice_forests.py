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

driver.maximize_window()

new_element = ''

try:
    Element_email = driver.find_element(By.XPATH, "//input[@name='usernamegh']")
    Element_email.send_keys('ubezpieczenia.magro@gmail.com')

except Exception as e:
    print(e)

    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    tags = ['input']  # to uzupełniać..?

    arr = []
    for tag in tags:
        for element in soup.find_all(tag):
            arr.append({'tag': tag} |
                       {'text': element.text} |
                       element.attrs)

    print(arr)
    """TODO name elements"""
    df = pd.DataFrame.from_records(arr)

    df.insert(0, 'element', df.name)
    # df.element.fillna(df['value'], inplace=True)
    print(df)

    df.to_csv('file.csv')

    # Test = df.loc[(df['name'] == 'username')]  # ???
    Test = df.iloc[0]['name']  # K! działa... Rząd nie po indeksie tylko po zatytułowaniu!
    print(Test)
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
    # # pred_dict = df.loc[(df['id'] == predicted_element)]
    # # print('predicted_element:', predicted_element)
    # # new_element = pred_dict['id']#.values[0]
    #
    # print('NEW ELEMENT:', new_element)
    #
    # new_locator = f"//*[@name='{predicted_element}']"

    ## locator_parts
    # tag, attr, val = df.loc[(df['tag'] == 'input')]
    new_locator = f"//*[@name='{Test}']"
    # print(new_locator)
    #
    # driver.execute_script(f"document.getElementById('{new_element}').value='ubezpieczenia.magro@gmail.com'")
    driver.find_element(By.XPATH, new_locator).send_keys(login)
    #
    # print('wpisane!!!')
    # time.sleep(50)










# driver.quit()



# body = driver.find_element(By.XPATH, "//body")
# body_attr = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', body)
# attr_li = ['class', 'div', 'id', 'input', 'name', 'type', 'value', 'span']

