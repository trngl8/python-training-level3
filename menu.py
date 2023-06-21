print("[1]. data structures (list, dict, tuple, set)\n\
[2]. functions\n\
[3]. filesystem operations\n\
[4]. exceptions\n\
[5]. objects details and abstractions\n\
[6]. database\n\
[7]. web application")
number = input("Enter your choice: ")
menu_list = ["data structures (list, dict, tuple, set)" , "functions" ,"filesystem operations" , "exceptions" , "objects details and abstractions" ,"database" , "web application"]
result = menu_list[int(number)- 1]
result = result.capitalize()
print(result)

# Expected input:
# 7
# Expected output:
# Web application
