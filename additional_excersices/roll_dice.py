import os, random

with open("results.txt", "w+") as results:
    results.truncate(0)

    for i in range(1000):
        num = random.randint(1,6)
        results.write(str(num))

with open("results.txt", "r") as results:
    all_nums = results.readline()
    num_6 = all_nums.count("6")

    print(f'Chances to roll a 6 are: {round(100*num_6/len(all_nums), 3)} %')

