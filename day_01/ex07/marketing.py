import sys

# set - множество, содержит неповторяющиеся элементы в случайном порядке. Это изменяемый тип данных.
# Результатом разности множеств является множество, содержащее элементы, которые есть в "уменьшаемом", но их нет в "вычитаемом". 
# То есть уникальные для "уменьшаемого".

def	call_center(clients, recipients):
	return list(clients - recipients)

def potential_clients(participants, clients):
	return list(participants - clients)

def	loyalty_program(participants, clients):
	return list(clients - participants)

def	return_sets(clients, participants, recipients):
	return set(clients), set(participants), set(recipients)


def main():
	clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is',
				'bill_gates@live.com', 'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
	participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org', 'jessica@gmail.com', 
		'elon@paypal.com', 'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
	recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

	if len(sys.argv) != 2:
		return 0
	clients, participants, recipients = return_sets(clients, participants, recipients) # преобразовываем список во множество (убираем дубликаты)
	if sys.argv[1] == "call_center":
		print(call_center(clients, recipients))
	elif sys.argv[1] == "potential_clients":
		print(potential_clients(participants, clients))
	elif sys.argv[1] == "loyalty_program":
		print(loyalty_program(participants, clients))
	else:
		raise Exception("Invalid argument") # Для принудительной генерации исключения.

if __name__ == "__main__":
	main()