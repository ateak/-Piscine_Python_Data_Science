import sys
from random import randint

class Research:
	def __init__(self, file):
		self.file = file

	def file_reader(self, has_header = True):
		with open(self.file, 'r') as text:
			lines = text.readlines() # считывает из файла все строки в список
			if lines[0] == '0,1\n' or lines[0] == '1,0\n': # проверяем, есть ли заголовок
				self.has_header = False # если нет, то ставим False
			start = 0
			if has_header == True:
				start = 1
			list = []	
			for i in range(start, len(lines)):
				first_num = int(lines[i][0])
				second_num = int(lines[i][2])
				list.append([first_num,second_num])
			return (list)

	class Calculations:
		def __init__(self, data):
			self.data = data
			self.count = self.counts()
			self.fractions = self.fractions
		
		def counts(self):
			x = [x[0] for x in self.data]
			y = [y[1] for y in self.data]
			return [sum(x), sum(y)]

		def fractions(self):
			total = sum(self.count)
			return tuple(value / total * 100 for value in self.count)
	
	class Analytics(Calculations):
		def __init__(self, num_steps):
			self.num_steps = num_steps
			self.predict = self.predict_random()
			self.predict_last = self.predict_last()
		
		def predict_random(self):
			predict_dict = {0: [0, 1], 1: [1, 0]}
			return [predict_dict[randint(0, 1)] for x in range(self.num_steps)]
		
		def predict_last(self):
			return self.predict[-1]


def parse_file(file):
	with open(file, "r") as text:
		lines = text.readlines() # считывает из файла все строки в список
		if len(lines) < 2 or len(lines[0].split(',')) != 2:
			raise Exception('Incorrect file structure')
		for line in lines[1:-1]:
			if line != '0,1\n' and line != '1,0\n':
				raise Exception('Incorrect file structure')

if __name__ == '__main__':
	if len(sys.argv) == 2:
		parse_file(sys.argv[1])
		list = Research(sys.argv[1]).file_reader()
		element = Research.Calculations(list)
		predict = Research.Analytics(3)
		print(element.data)
		print(element.count[0], element.count[1])
		print(predict.predict)
		print(predict.predict_last)
	else:
		raise Exception('Incorrect arguments')