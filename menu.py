menu_list = [
    "data structures (list, dict, tuple, set)", "functions", "filesystem operations", "exceptions",
    "objects details and abstractions", "database", "web application", 'sdfgsdfg'
]
for i, item in enumerate(menu_list):
    print(f"[{i+1}]. {item}")

# TODO: maybe more clean?
choice = 0
while choice == 0:
    try:
        choice = int(input("Enter your choice: "))
    except TypeError:
        print("You should enter a number")

if len(menu_list) < choice:
    print(f"Number should be from 1 to {len(menu_list)}")
    exit()

result = menu_list[choice- 1]
result = result.capitalize()
print(result)
