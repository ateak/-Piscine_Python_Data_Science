import sys

def extractor():
    if (len(sys.argv) > 2):
        raise Exception('Argument error')
    fp_write = open('employees.tsv', 'w')
    for i, param in enumerate(sys.argv): # позволяет перебирать коллекцию элементов, отслеживая индекс текущего элемента.
        if (i != 0):
            fp_write.write("Name\tSurname\tE-mail\n") # записываем строку в открытый файл.
            with open(param) as fp_read:
                for line in fp_read:
                    name_surname = line.split('@') # разбивает строку на части, используя разделитель, и возвращает эти части списком. Направление разбиения: слева направо. 
                    name = name_surname[0].split('.')[0] # берем 0-й элемент списка, где имя с фамилией и разбиваем их по точке, записываем имя в переменную
                    surname = name_surname[0].split('.')[1] # делаем все вышеназванное и записываем фамилию в переменную
                    fp_write.write('%s\t%s\t%s' % (name.capitalize(), surname.capitalize(), line)) # capitalize() вернет копию строки с первым символом в верхнем регистре, а остальные символы будут в нижнем регистре. 


if __name__ == '__main__':
    extractor()