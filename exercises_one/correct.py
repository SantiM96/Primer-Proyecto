def correct(list):
    new_list = []
    for item in list:
        reset = 0
        new_item = ""
        for letter in item:
            if reset != 0:
                letter = letter.lower()
                new_item += letter
                reset += 1
                if letter == " ":
                    reset = 0
            else:
                new_item += letter
                reset += 1
        new_list.append(new_item)
    return new_list


new_list = []
random_list = ["ALO", "COCA COLA"]
new_list = correct(random_list)
print(new_list)