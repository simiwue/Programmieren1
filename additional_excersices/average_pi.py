import math

pi = math.pi

averages = [3+1/8, (16/9)**2, math.sqrt(10), 3+1/7]

kleinste_abweichung = 10

for num in averages:
    abweichung = abs(pi - num)
    if abweichung < kleinste_abweichung:
        kleinste_abweichung = abweichung
        best_num = num

best_average = str(averages[averages.index(best_num)])

print(f"The best average is {best_average} with abweichung of {kleinste_abweichung}.")