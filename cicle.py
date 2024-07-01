my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
length = len(my_list)
index = 0
while length >= index:
    number = my_list[index]
    if number > 0:
        print(number)
        index = index + 1
        continue
    elif number == 0:
        index = index + 1
    else:
        break
