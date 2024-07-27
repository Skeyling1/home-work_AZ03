#3. Необходимо спарсить цены на диваны с сайта divan.ru в csv файл, обработать данные, найти среднюю цену и вывести ее,
# а также сделать гистограмму цен на диван

import selenium as sl
import selenium.webdriver



url = 'https://www.ru-divan.ru/catalog/divany/'



#prices = sl.find_elements(BY.