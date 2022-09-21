#! /usr/bin/python3
import timeit

def loop_and_append():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
    new_emails = []
    for item in emails:
        if item.find('@gmail.com') != -1:
            new_emails.append(item)

def list_comprehension():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
    new_emails = [item for item in emails if item.find('@gmail.com') != -1]

def main():

    ITERATIONS_NUMBER = 9 * 10**7

    time_for_loop = timeit.timeit(setup = loop_and_append, number=ITERATIONS_NUMBER)
    time_list_comprehension = timeit.timeit(setup = list_comprehension, number=ITERATIONS_NUMBER)

    if time_list_comprehension < time_for_loop:
        print('it is better to use a list comprehension')
    else:
        print('it is better to use a loop')

    print(f'{min(time_for_loop, time_list_comprehension)} vs ' + f'{max(time_for_loop, time_list_comprehension)}')
    

if __name__ == '__main__':
    main()
