special_chars = "!@#$%^&*()?/<>.,\\|{}][`~±§"
numbers = "1234567890"

weak = 0
weak_list = []
medium = 0
strong = 0

loop_num = input("Please enter the number of passwords: ")
loop_num = int(loop_num)

while loop_num < 0:
    print("Error: number of passwords cannot be negative.")
    loop_num = input("Please enter the number of passwords: ")
    loop_num = int(loop_num)

i = 0

while i < loop_num:
    count = 0
    flag_1 = False
    flag_2 = False

    user_password = input("Please enter the password: ")

    for ch in user_password:
        count += 1

        if ch in numbers:
            flag_1 = True

        if ch in special_chars:
            flag_2 = True

    if count < 6:
        print("Password is weak")
        weak += 1
        weak_list.append(user_password)

    elif count < 10:
        print("Password is medium")
        medium += 1

    elif flag_1 and flag_2:
        print("Password is strong")
        strong += 1

    else:
        print("Password is medium")
        medium += 1

    i += 1

print("Number of weak passwords is", weak)
print("Number of medium passwords is", medium)
print("Number of strong passwords is", strong)

for password in weak_list:
    print("The weak password is", password)
