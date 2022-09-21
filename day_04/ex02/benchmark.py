#! /usr/bin/python3
import timeit
import sys

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

def filter_func():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
    new_emails = list(filter(lambda item : item.find("@gmail.com") != -1, emails))

# В то время как map() пропускает каждый элемент итерируемого через функцию и возвращает результат всех элементов, прошедших через функцию,
# filter(), прежде всего, требует, чтобы функция возвращала логические значения (true или false), а затем передает каждый элемент 
# итерируемого через функцию, «отфильтровывая» те, которые являются ложными.
	
def main():
	
	if len(sys.argv) != 3:
		raise Exception("invalid args")
	if (sys.argv[1] == 'loop'):
		time_exec = timeit.timeit(loop_and_append, number=int(sys.argv[2]))
	elif (sys.argv[1] == 'list_comprehension'):
		time_exec = timeit.timeit(list_comprehension, number=int(sys.argv[2]))
	elif (sys.argv[1] == 'map'):
		time_exec = timeit.timeit(map_func, number=int(sys.argv[2]))
	elif (sys.argv[1] == 'filter'):
		time_exec = timeit.timeit(filter_func, number=int(sys.argv[2]))
	else:
		raise Exception("unknown argument")

	print(time_exec)

	
if __name__ == '__main__':
	main()
