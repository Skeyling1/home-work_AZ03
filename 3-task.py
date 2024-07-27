#3. Необходимо спарсить цены на диваны с сайта divan.ru в csv файл, обработать данные, найти среднюю цену и вывести ее,
# а также сделать гистограмму цен на диван

import  csv
from selenium import webdriver
from selenium.webdriver.common.by import By



browser = webdriver.Chrome()
browser.get('https://www.ru-divan.ru/catalog/divany/')

prices = browser.find_elements(By.XPATH, "//div[@class='thumbnail-price float-left']")
for price in prices:
    cleaned_price = price.text
    cleaned_price = cleaned_price.replace(" ", "")
    cleaned_price = int(cleaned_price.strip('от₽'))

    print(cleaned_price)





browser.quit()