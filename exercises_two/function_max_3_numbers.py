
def max_three(one, two, three):
    n_max = one
    if n_max < two:
        n_max = two
    if n_max < three:
        n_max = three
    return n_max

big = max_three(2, 8, 3)
print(big)
