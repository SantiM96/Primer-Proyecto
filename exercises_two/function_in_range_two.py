
def trange(number, one, two):
    condition = False

    if number >= one and number <= two:
        condition = True
    return condition

print("")
test = trange(107, 90, 120)
print(test)
