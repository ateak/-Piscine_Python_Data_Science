import sys

def caesar():
    if (len(sys.argv) != 4):
        raise Exception('Argument error')
    Cyrillic_symbols = ('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    check_Cyrillic_symbols = [x for x in Cyrillic_symbols if x in sys.argv[2].lower()]
    if (len(check_Cyrillic_symbols) != 0):
        raise Exception('The script does not support your language yet')
    
    res = ''
    type = sys.argv[1]
    str = sys.argv[2]
    number = sys.argv[3]
    alpha_small = 'abcdefghijklmnopqrstuvwxyz'
    alpha_big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if (type == 'encode'):
        res = ''
        for c in str:
            if (c in alpha_small):
                res += alpha_small[(alpha_small.index(c) + int(number)) % len(alpha_small)] # str.index возвращает наименьший индекс, 
																							# по которому обнаруживается начало указанной подстроки в исходной.
            elif (c in alpha_big):
                res += alpha_big[(alpha_big.index(c) + int(number)) % len(alpha_big)]
            else:
                res += c
    if (type == 'decode'):
        res = ''
        for c in str:
            if (c in alpha_small):
                res += alpha_small[(alpha_small.index(c) - int(number)) % len(alpha_small)]
            elif (c in alpha_big):
                res += alpha_big[(alpha_big.index(c) - int(number)) % len(alpha_big)]
            else:
                res += c
    print(res)

if __name__ == '__main__':
    caesar()