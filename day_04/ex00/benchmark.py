#! /usr/bin/python3
import timeit

def loop_and_append():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
    new_emails = []
    for item in emails:
        if item.find('@gmail.com') != -1:
            new_emails.append(item)
# Для поиска подстроки в строке в Python применяется метод find(), который возвращает индекс первого вхождения подстроки в строку. 
# Если подстрока не найдена, возвращается –1.

def list_comprehension():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
    new_emails = [item for item in emails if item.find('@gmail.com') != -1]

# List comprehension — это упрощенный подход к созданию списка, который задействует цикл for, 
# а также инструкции if-else для определения того, что в итоге окажется в финальном списке.

def main():

	ITERATIONS_NUMBER = 9 * 10**7

	time_for_loop = timeit.timeit(loop_and_append, number=ITERATIONS_NUMBER)
	time_list_comprehension = timeit.timeit(list_comprehension, number=ITERATIONS_NUMBER)

	# Функция timeit() возвращает время, необходимое для выполнения основного выражения number количество раз.

	if time_list_comprehension < time_for_loop:
		print('it is better to use a list comprehension')
	else:
		print('it is better to use a loop')

	print(f'{min(time_for_loop, time_list_comprehension)} vs ' + f'{max(time_for_loop, time_list_comprehension)}')


if __name__ == '__main__':
    main()
