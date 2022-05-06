def open_file(file):
    try:
        with open(file,'r') as read_file:
            for line in read_file:
                print(line.rstrip('\n'))
    except:
        raise

    finally:
        print('Operation executed')


def append_to_file(file,item):
    try:
        with open(file, 'a') as read_file:
            read_file.write(item + '\n')
    except:
        raise

    finally:
        print()
        print('Operation executed')

open_file('orders.txt')
append_to_file('orders.txt', 'nuggets')
open_file('orders.txt')