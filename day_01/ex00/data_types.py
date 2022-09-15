def data_types():
    types = (
        1,                          					# int
        'str',              							# str
        1.1,                       			 			# float
        True,                       					# bool
        [1, 20, 4.0, 'word'],       					# list
        {'name': 'School 21', 'location': 'Moscow'},  	# dict
        (1, 'str', True),           					# tuple
        {1, 5, 3, 4, 6}            						# set
    )


    output = '['
    for var in types:
        output += type(var).__name__ + ', '
    output = output[:-2] + ']'
    print(output)

#Функция type воспринимает объект произвольного типа и возвращает его тип.

if __name__ == '__main__':
    data_types()