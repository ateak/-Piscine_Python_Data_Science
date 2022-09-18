class Research:
	def file_reader():
		with open("data.csv") as text:
			for line in text:
				print(line, end='')


if __name__ == '__main__':
	Research.file_reader()