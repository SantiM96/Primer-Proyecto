
def pair(list):
    pair_list = []
    for number in list:
        if number % 2 == 0:
            pair_list.append(number)
    return pair_list

list_one = [8, 4, 6, 8, 7, 2, 3, 4, 6, 8, 7, 31 ,38, 20, 57, 58, 32]

print(pair(list_one))