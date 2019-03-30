
list = ["alo", "como estás", "chau"]
n_list = []
long_word = 0


for word in list:
    for letter in word:
        long_word += 1
    n_list.append(long_word)
    long_word = 0

print(n_list)