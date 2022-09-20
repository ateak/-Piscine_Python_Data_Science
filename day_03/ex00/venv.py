#! /usr/bin/python3

import os

if __name__ == "__main__":
    print(f"Your current virtual env is {os.getenv('VIRTUAL_ENV')}")
	
# Функция os. getenv() возвращает значение ключа key переменной среды, если оно существует 
# или значение по умолчанию default , если его нет. 