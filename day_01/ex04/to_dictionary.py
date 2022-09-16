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
	dict_with_countries = dict() # Создаем пустой словарь
	for i in list_of_tuples:
		if dict_with_countries.get(i[1]) is not None: # метод get() возвращает значение для ключа, если ключ находится в словаре, если ключ отсутствует то вернет значение default. 
													# Если значение default не задано и ключ key не найден, то метод вернет значение None.
			dict_with_countries[i[1]].append(i[0]) # Метод append() добавляет элемент в конец списка.

		else:
			dict_with_countries[i[1]] = [i[0]]
	for key, values in dict_with_countries.items(): # Метод dict.items() возвращает список кортежей вида (key, value), состоящий из элементов словаря.
		for value in values:
			print(f"'{key}' : '{value}'") # f-строки берут значения переменных, которые есть в текущей области видимости, и подставляют их в строку. 


if __name__ == "__main__":
	main()