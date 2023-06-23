import sys
import os
def print_header(head):
    for item in head:
        print(item.upper(), end=',')
    print()


def print_list(data):
    """ Print a list of data on one line """
    for item in data:
        print(item, end=',')


def print_books(data):
    """ Print a structure of dictionaries in list """
    for item in data:
        res = ",".join(item.values())
        print(res, end=',')


def parse_file(filename, start=1) -> list:
    result = []

    with open(filename) as file_object:
        lines = file_object.readlines()

    for item in lines[start:]:
        s = item.split(',')
        result.append(
            {
                'title': s[1],
                'author': s[2],
                'year': s[3]
            }
        )

    return result


# ---------------------------------------------------


file = 'data/' + sys.argv[1]

if os.path.isfile(file):
    header = ['id', 'title', 'author', 'year', 'weight']
    books = parse_file(file)

    print_header(header)
    print_books(books)
else:
    print("File does not exists")
    exit(0)
