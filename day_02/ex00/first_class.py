class Must_read:
    with open("data.csv") as text:
        for line in text:
            print(line, end='')


if __name__ == '__main__':
    Must_read()