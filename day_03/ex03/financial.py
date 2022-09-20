#! /usr/bin/python3

from bs4 import BeautifulSoup
import sys
import requests
import time

def parse_html():
    time.sleep(5)
	# Этот код просто отправляет запрос GET на сайт. 
    html_yahoo = requests.get(f"https://finance.yahoo.com/quote/{sys.argv[1]}/financials", headers={'User-Agent' : 'Custom'})
    if html_yahoo.status_code != 200: # 200 - код состояния, означающий успешно
        raise Exception("page is not found")
    soup = BeautifulSoup(html_yahoo.text, "html.parser") # создаем Beautiful Soup объект, который принимает текст с веб-страницы
														 # Модуль html.parser в Python предоставляет нам класс HTMLParser, 
														 # который можно разделить на подклассы для анализа текстовых файлов в формате HTML.
														 
    rows = soup.find_all('div', attrs={'data-test' : 'fin-row'}) # find_all - функция, когда нужно найти несколько одинаковых тегов
																 # находим элементы по HTML атрибутам на странице, берем целую строку fin-row
    for i in rows:
        if i.find("div", attrs={'title' : sys.argv[2]}) is not None: # Метод .find() извлекает только первый найденный HTML-тег.
            cols = i.find_all('div', {'data-test' : 'fin-col'})
            return tuple([sys.argv[2], *[j.text for j in cols]]) # звездочка убирает квадратные скобки
																 # text используется для получения только данных без разметки
    raise Exception("statement name is not found")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise Exception("invalid info")
    data = parse_html()
    if data is None:
        raise Exception("invalid info")
    print(data)