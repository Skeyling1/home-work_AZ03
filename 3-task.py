#3. Необходимо спарсить цены на диваны с сайта divan.ru в csv файл, обработать данные, найти среднюю цену и вывести ее,
# а также сделать гистограмму цен на диван

import  csv
from selenium import webdriver
from selenium.webdriver.common.by import By



browser = webdriver.Chrome()
browser.get('https://www.ru-divan.ru/catalog/divany/')

prices = browser.find_elements(By.XPATH, "//div[@class='thumbnail-price float-left']")
for price in prices:
    print(price.text)





browser.quit()