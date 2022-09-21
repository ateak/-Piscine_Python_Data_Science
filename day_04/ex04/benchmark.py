#! /usr/bin/python3
import timeit
from random import randint
from collections import Counter

def lst_to_dict(lst):
	dict = {}
	for item in lst:
		if item not in dict:
			dict[item] = 1
		else:
			dict[item] += 1
	return dict

def top_dict(lst):
	# Создадим словарь из списка
	my_dict = lst_to_dict(lst)
	# Отсортируем, получим список
	sorted_list = sorted(my_dict.items(), key=lambda item: -int(item[1])) # С помощью параметра key можно указывать, как именно выполнять сортировку. 
																	      # Параметр key ожидает функцию, с помощью которой должно быть выполнено сравнение.
	# Возьмем срез первых десяти
	top_list = sorted_list[:10]
	# Создадим из списка словарь (нужно по заданию)
	my_top_dict = dict((x, y) for x, y in top_list)
	return my_top_dict

def counter_dict(lst):
	return dict(Counter(lst))

def counter_top_10(lst):
	return Counter(lst).most_common(10) # most_common() возвращает список из n наиболее распространенных элементов 
										# и их количество от наиболее распространенных до наименее.

# Counter является подклассом Dictionary и используется для отслеживания элементов и их количества. 
# Counter – это неупорядоченная коллекция, в которой элементы хранятся, как ключи Dict, а их количество – как значение dict. 
# Количество элементов счетчика может быть положительным, нулевым или отрицательным целым числом.
# Отдавая на вход список слов (который list), получаем объект класса Counter, очень похожий на словарь (который dictionary).

def my_time(func_name, lst):
	times = timeit.timeit(lambda: func_name(lst), number = 1)
	return times

def main():
	
	lst = [randint(0, 100) for i in range(1000000)]

	try:
		print('my function:', my_time(lst_to_dict, lst))
		print('Counter:', my_time(counter_dict, lst))
		print('my top:', my_time(top_dict, lst))
		print('Counter\'s top:', my_time(counter_top_10, lst))
	except:
		print('ERROR')
# Для обработки исключений используется конструкция try - except. В блоке try мы выполняем инструкцию, которая может породить исключение, 
# а в блоке except мы перехватываем их. При этом перехватываются как само исключение, так и его потомки.

if __name__ == '__main__':
	main()
