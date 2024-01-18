import random


def create_list(length):
    list = []
    while len(list) < length:
        list.append(random.randint(0,9))

    return list



def digit_count(list):
    counts = [0] * 10

    for num in list:
        counts[num] += 1

    return counts



num_list = create_list(1000)

print(digit_count(num_list))