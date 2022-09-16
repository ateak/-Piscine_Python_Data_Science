import sys # Модуль sys в Python предоставляет простые функции, которые позволяют нам напрямую взаимодействовать с интерпретатором

def get_key(dict, value):
    for k, v in dict.items(): # Метод dict.items() возвращает список кортежей вида (key, value), состоящий из элементов словаря.
        if v == value:
            return k

def	get_company_and_price(ticker_symbol):
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
	
	ticker_symbol = ticker_symbol.upper()

	company = get_key(COMPANIES, ticker_symbol)
	price = STOCKS.get(ticker_symbol) # метод get() возвращает значение для ключа, если ключ находится в словаре, если ключ отсутствует то вернет значение default. 
									# Если значение default не задано и ключ key не найден, то метод вернет значение None.
	if company is None or price is None:
		return None
	return company, price 

def	main():
	if len(sys.argv) != 2:
		return 0
	res = get_company_and_price(sys.argv[1]) # функция возвращает str и float, и они хранятся в res как кортеж 
	if res is None:
		print("Unknown ticker")
	else:
		print("{} {}".format(res[0], res[1]))	# Этот метод позволяет форматировать строку, вставляя в нее на место плейсхолдеров определенные значения. 
												# В качестве результата метод format() возвращает новую отформатированную строку.

if __name__ == '__main__':
	main()