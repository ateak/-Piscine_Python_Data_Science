import sys

class Research:
	def __init__(self, file):
		self.file = file

	def file_reader(self):
		with open(self.file, 'r') as text:
			return(text.read()) # чтение всего файла

def parse_file(file):
	with open(file, "r") as text:
		lines = text.readlines()
		if len(lines) < 2 or len(lines[0].split(',')) != 2:
			raise Exception('Incorrect file structure')
		for line in lines[1:-1]:
			if line != '0,1\n' and line != '1,0\n':
				raise Exception('Incorrect file structure')

if __name__ == '__main__':
	if len(sys.argv) == 2:
		parse_file(sys.argv[1])
		print(Research(sys.argv[1]).file_reader())
	else:
		raise Exception('Incorrect arguments')