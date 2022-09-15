def read_and_write():
	f_csv = open("ds.csv", "r") #r - открывает файл только для чтения
	csv_text = f_csv.read() # читаем весь файл в одну строку

	f_csv.close()
	quote_number = 0
	comma = ","
	quote = '\"'
	tsv_text = ""

	for i in range(len(csv_text)):
		if csv_text[i] == quote:
			quote_number += 1
		if csv_text[i] == comma and quote_number % 2 == 0:
			tsv_text += "\t"
		else:
			tsv_text += csv_text[i]

	f_tsv = open("ds.tsv", "w") #w - открыт для записи (перед записью файл будет очищен)
	f_tsv.write(tsv_text) # записываем строку в открытый файл

if __name__ == "__main__":
	read_and_write()
