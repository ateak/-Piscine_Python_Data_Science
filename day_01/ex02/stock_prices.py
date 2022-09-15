import sys # Модуль sys в Python предоставляет простые функции, которые позволяют нам напрямую взаимодействовать с интерпретатором

def	get_price(company):
	COMPANIES = {	'Apple': 'AAPL',
					'Microsoft': 'MSFT',
					'Netflix': 'NFLX',
					'Tesla': 'TSLA',
					'Nokia': 'NOK'  }

	STOCKS = 	{  	'AAPL': 287.73,
					'MSFT': 173.79,
					'NFLX': 416.90,
					'TSLA': 724.88,
					'NOK': 3.37		}
	
	company = company[0].upper() + company.lower()[1:] # [1:] - от 1 символа и до конца строки
	ticker_symbol = COMPANIES.get(company) # метод get() возвращает значение для ключа, если ключ находится в словаре, если ключ отсутствует то вернет значение default. 
									# Если значение default не задано и ключ key не найден, то метод вернет значение None.
	if ticker_symbol is None:
		return "Unknown company"
	price = STOCKS.get(ticker_symbol.upper())
	if price is None:
		return "Unknown company"
	return price

def	main():
	if len(sys.argv) != 2:
		return 0
	print(get_price(sys.argv[1]))

if __name__ == '__main__':
	main()