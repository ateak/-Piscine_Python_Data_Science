#! /usr/bin/python3
import timeit
import sys
from functools import reduce

def sum_of_squares_loop(number):
	res = 0
	for i in range(1, number + 1):
		res += i ** 2
	return res

def sum_of_squares_reduce(number):
    return reduce(lambda x, y: x + y ** 2, [range(1, number + 1)]) 
	# reduce применяет указанную функцию к элементам последовательности, сводя её к единственному значению.
	# Левый аргумент x - это накопленное значение, а правый аргумент y - это следующий элемент iterable.
	
def main():
	
	if len(sys.argv) != 4:
		raise Exception("invalid args")
	if (sys.argv[1] == 'loop'):
		time_exec = timeit.timeit(lambda: sum_of_squares_loop(int(sys.argv[3])), number=int(sys.argv[2]))
	elif (sys.argv[1] == 'reduce'):
		time_exec = timeit.timeit(lambda: sum_of_squares_reduce(int(sys.argv[3])), number=int(sys.argv[2]))
	else:
		raise Exception("unknown argument")

	print(time_exec)

	
if __name__ == '__main__':
	main()
