import sys

def all_stocks(lst_of_names):
	COMPANIES = {	'Apple': 'AAPL',
					'Microsoft': 'MSFT',
					'Netflix': 'NFLX',
					'Tesla': 'TSLA',
					'Nokia': 'NOK'  }

	STOCKS = {  	'AAPL': 287.73,
					'MSFT': 173.79,
					'NFLX': 416.90,
					'TSLA': 724.88,
					'NOK': 3.37		}

	for ticker_or_name in lst_of_names:
		used = set() #Множество - это контейнер, который содержит уникальные не повторяющиеся элементы в случайном порядке
		for company_name in COMPANIES.keys(): #Метод dict.keys() возвращает новый список-представление всех ключей
			if ticker_or_name.lower() == company_name.lower():
				price = STOCKS[COMPANIES[company_name]]
				print("{} stock price is {}".format(company_name, price)) # Этот метод позволяет форматировать строку, вставляя в нее на место плейсхолдеров определенные значения. 
																			# В качестве результата метод format() возвращает новую отформатированную строку. 
				used.add(ticker_or_name) # Метод set.add() добавляет заданный элемент в множество. Если элемент уже присутствует, он не добавляет никаких элементов. 
				break
			if COMPANIES.get(company_name) is not None and COMPANIES.get(company_name) == ticker_or_name:
				print("{} is a ticker symbol for {}".format(company_name, COMPANIES[company_name]))
				used.add(ticker_or_name) 
				break
		if ticker_or_name not in used:
			print("{} is an unknown company or an unknown ticker symbol".format(ticker_or_name))

def main():
	if len(sys.argv) != 2:
		print()
		return 0
	lst = [i.strip() for i in sys.argv[1].split(",")] # создаем список из строк, образованных в результате разделения входной строки по запятой, а также избавленных от пробелов методом strip(): 
													# strip() возвращает новую строку после удаления любых начальных и конечных пробелов, включая табуляцию (\ t).
	if "" in lst:
		print()
		return 0
	all_stocks(lst)

if __name__ == "__main__":
	main()