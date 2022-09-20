#! /usr/bin/python3
import sys
import subprocess
import os

if __name__ == "__main__":
    if os.getenv("VIRTUAL_ENV") is None: 
        raise Exception("invalid venv")
	# os. getenv() возвращает значение ключа key переменной среды, если оно существует или значение по умолчанию default, если его нет.
    subprocess.call([sys.executable, "-m", "pip", "install", "beautifulsoup4", "PyTest"])
	# subprocess.call выполняет команду, описанную args. Ожидает завершения команды, а затем возвращает код возврата.
	# sys.executable - путь к интерпретатору Python.
    subprocess.run([sys.executable, "-m", "pip", "freeze"], stdout=open("requirements.txt", "w"))
    subprocess.run(["cat", "requirements.txt"])
	# subprocess.run запускает команду/скрипт/программу с аргументами, ждет завершения команды, 
	# а затем возвращает экземпляр CompletedProcess() с результатами работы.
