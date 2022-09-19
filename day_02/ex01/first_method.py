class Research:
	def file_reader():
		with open("data.csv", "r") as text:
			return(text.read()) # чтение всего файла


if __name__ == '__main__':
	print(Research.file_reader())