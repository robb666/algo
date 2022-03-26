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

locator = 'username'
try:
    Element_email = driver.find_element(By.XPATH, f"//input[@name='{locator}']")
    Element_email.send_keys('ubezpieczenia.magro@gmail.com')

except Exception as e:
    print(e)

    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    tags = ['input']  # to uzupełniać..?
    el_name = ['LOGIN', 'PASSW', 'LOG_BUTTON']

    arr = []
    tst = []
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

    print(df)

    # df.to_csv('file.csv')

    # Test = df.loc[(df['name'] == 'username')]  # ???
    # Test = df.iloc[0]['name']  # K! działa... Rząd nie po indeksie tylko po zatytułowaniu!
    # Test = df.loc[(df['element'] == 'username')]['name'].values[0]
    Test = df.loc[(df['element'] == 'qwer')]
    # Test = df
    # print(Test)
    Test.to_csv('Test.csv')

    from rand_forests_sel import predict_elements, get_predicted_element
    from queue import PriorityQueue

    scores, element_name, test_df = predict_elements()
    print(scores, element_name)

    queue = PriorityQueue()

    from_heap = get_predicted_element(scores, queue)[1]
    print(from_heap)
    predicted_element = df.loc[(df['element'] == from_heap)]['name'].values[0]


    # pred_dict = df.loc[(df['id'] == predicted_element)]
    # print('predicted_element:', predicted_element)
    # new_element = pred_dict['id']#.values[0]

    # print('NEW ELEMENT:', new_element)
    print('NEW predicted_element:', predicted_element)

    new_locator = f"//*[@name='{predicted_element}']"

    ## locator_parts
    # tag, attr, val = df.loc[(df['tag'] == 'input')]
    # new_locator = f"//*[@name='{Test}']"
    # print(new_locator)


    # driver.execute_script(f"document.getElementById('{new_element}').value='ubezpieczenia.magro@gmail.com'")
    driver.find_element(By.XPATH, new_locator).send_keys(login)
    #
    print('wpisane!!!')
    time.sleep(50)










# driver.quit()



# body = driver.find_element(By.XPATH, "//body")
# body_attr = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', body)
# attr_li = ['class', 'div', 'id', 'input', 'name', 'type', 'value', 'span']

