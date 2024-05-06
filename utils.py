def find_max(number_list):
    highest = 0

    for number in number_list:
        if number > highest:
            highest = number

    print(highest)
