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


def parse_file(filename):
    result = []
    lines = open(filename)
    for item in lines:
        s = item.split(',')
        result.append(
            {
                'title': s[1],
                'author': s[2],
                'year': s[3]
            }
        )
    lines.close()
    return result


def check_file_exists(filename):
    if os.path.isfile(filename):
        return True
    else:
        return False

# ---------------------------------------------------

file = 'data/' + sys.argv[1]

header = ['id', 'title', 'author', 'year', 'weight']
books = parse_file(file)

print_header(header)
print_books(books)

# ID,TITLE,AUTHOR,YEAR
# 1,learn python hard way,zed shaw,2021
# 2,,,
