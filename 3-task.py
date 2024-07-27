#3. Необходимо спарсить цены на диваны с сайта divan.ru в csv файл, обработать данные, найти среднюю цену и вывести ее,
# а также сделать гистограмму цен на диван

import  csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import matplotlib.pyplot as plt
import numpy as np

def cl_dat(price):
    cleaned_price = price.text
    cleaned_price = cleaned_price.replace(" ", "").strip('от₽')
    #cleaned_price = int(cleaned_price)
    return cleaned_price

browser = webdriver.Chrome()
browser.get('https://www.ru-divan.ru/catalog/divany/')
data = []
headings = ['price']

with open('prices.csv', "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headings)
    prices = browser.find_elements(By.XPATH, "//div[@class='thumbnail-price float-left']")
    for price in prices:
        cleaned_price = cl_dat(price)
        writer.writerow([cleaned_price])
        data.append(int(cleaned_price))
browser.quit()

x = np.mean(data)
print(x)

plt.hist(data, bins = 100)
plt.title("Гистограмма цен на диваны")
plt.xlabel("цена, руб")
plt.ylabel("кол-во диванов")
plt.show()
