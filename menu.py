menu_list = ["data structures (list, dict, tuple, set)" , "functions" ,"filesystem operations" , "exceptions" , "objects details and abstractions" ,"database" , "web application"]
for i in range(len(menu_list)):
    print(f"[{i+1}]. {menu_list[i]}")
number = input("Enter your choice: ")
try:
    number = float(number)
except :
    print("You should enter a number")
    exit()
if str(number)[str(number).index('.') + 1] != "0" and len(str(number)) != str(number).index('.') + 1:
    print('Number should be integer')
    exit()
if not 8 <= int(number) <=0:
    print("Number should be from 1 to 7")
    exit()
result = menu_list[int(number)- 1]
result = result.capitalize()
print(result)

# Expected input:
# 7
# Expected output:
# Web application
