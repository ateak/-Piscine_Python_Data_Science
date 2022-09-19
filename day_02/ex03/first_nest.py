import sys

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
		def counts(list):
			heads = 0
			tails = 0
			for values in list:
				if values[0]:
					tails += 1
				else:
					heads += 1
			return (heads, tails) # возвращаем кортеж (tuple)

		def fractions(counts_list):
			total = sum(counts_list)
			return tuple(value / total * 100 for value in counts_list)

def parse_file(file):
	with open(file, "r") as text:
		lines = text.readlines() # считывает из файла все строки в список
		if len(lines) < 2 or len(lines[0].split(',')) != 2:
			raise Exception('Incorrect file structure')
		for line in lines[1:-1]: # вырезаем строку без первого символа
			if line != '0,1\n' and line != '1,0\n':
				raise Exception('Incorrect file structure')

if __name__ == '__main__':
	if len(sys.argv) == 2:
		parse_file(sys.argv[1])
		list = Research(sys.argv[1]).file_reader()
		print(list)
		counts_list = Research.Calculations.counts(list)
		print(counts_list[1], counts_list[0])
		fractions_list = Research.Calculations.fractions(counts_list)
		print(fractions_list[1], fractions_list[0])
	else:
		raise Exception('Incorrect arguments')