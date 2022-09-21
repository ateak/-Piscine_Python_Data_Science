#! /usr/bin/python3
import timeit

def loop_and_append():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
    new_emails = []
    for item in emails:
        if item.find('@gmail.com') != -1:
            new_emails.append(item)

def list_comprehension():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
    new_emails = [item for item in emails if item.find('@gmail.com') != -1]

def map_func():
	emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
	new_emails = list(map(lambda item : None if item.find("@gmail.com") == -1 else item, emails))

#map - идет по итерируемому объекту и применяет какую-то функцию к каждому элементу
	
def main():

	ITERATIONS_NUMBER = 9 * 10**7

	time_for_loop = timeit.timeit(loop_and_append, number=ITERATIONS_NUMBER)
	time_list_comprehension = timeit.timeit(list_comprehension, number=ITERATIONS_NUMBER)
	time_map = timeit.timeit(map_func, number=ITERATIONS_NUMBER)

	min_time = min([time_for_loop, time_list_comprehension, time_map])

	if min_time == time_list_comprehension:
		print('it is better to use a list comprehension')
	elif min_time == time_for_loop:
		print('it is better to use a loop')
	else:
		print('it is better to use a map')

	time_sorted = sorted([time_for_loop, time_list_comprehension, time_map]) 
	# Функция sorted возвращает новый отсортированный список, который получен из итерируемого объекта, который был передан как аргумент.
	print(f'{time_sorted[0]} vs {time_sorted[1]} vs {time_sorted[2]}')
	
	
if __name__ == '__main__':
    main()
