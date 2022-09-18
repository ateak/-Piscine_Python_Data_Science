def main():
	list_of_tuples = [
		('Russia', '25'),
		('France', '132'),
		('Germany', '132'),
		('Spain', '178'),
		('Italy', '162'),
		('Portugal', '17'),
		('Finland', '3'),
		('Hungary', '2'),
		('The Netherlands', '28'),
		('The USA', '610'),
		('The United Kingdom', '95'),
		('China', '83'),
		('Iran', '76'),
		('Turkey', '65'),
		('Belgium', '34'),
		('Canada', '28'),
		('Switzerland', '26'),
		('Brazil', '25'),
		('Austria', '14'),
		('Israel', '12') ]

	dict_of_countries = dict(list_of_tuples) 
	sorted_dict = dict(sorted(dict_of_countries.items(), key=lambda country_number : (-1 * int(country_number[1]), country_number[0]))) 
	# Функция sorted возвращает новый отсортированный список, который получен из итерируемого объекта, который был передан как аргумент. 
	# С помощью параметра key можно указывать, как именно выполнять сортировку. Параметр key ожидает функцию, с помощью которой должно быть выполнено сравнение.
	# lambda - функция без объявления. Работает так: lambda перечисляются аргументы через запятую : что то с ними делается)(передаем аргументы))
	# -1 для сортировки по убыванию
	# int(country_number[1]) - приводим строку к инту, чтобы сортировка шла по интам

	for key in sorted_dict.keys(): #метод keys() возвращает список всех доступных ключей в словаре.
		print(key)


if __name__ == "__main__":
	main()