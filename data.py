def print_header(head):
    for item in head:
        # TODO: remove last coma
        print(item.upper(), end=',')
    print()


def print_data(data):
    for item in data:
        print(item, end=',')


# ---------------------------------------------------

book = [1, 'learn python hard way', 'zed shaw', 2021]

header = ['id', 'title', 'author', 'year', 'weight']

print_header(header)
print_data(book)

# ID,TITLE,AUTHOR,YEAR
# 1,learn python hard way,zed shaw,2021
# 2,,,
