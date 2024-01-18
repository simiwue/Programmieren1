
with open("results.txt", "w+") as file:

    for i in range(100,1000):
        summ = 0

        for digit in str(i):
            summ += int(digit) ** 3

        if summ == i:
            file.write(str(i) + "\n")

with open("results.txt", "r") as f:

    all_lines = f.readlines()
    for line in all_lines:
        num = line[:-1]
        print(num)
