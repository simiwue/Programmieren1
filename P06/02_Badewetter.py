
temp_list = [29, 30, 40, 24, 32, 36, 31]

def optimal_day(temps):
    highest_temp = 0
    for temp in temps:
        if temp > highest_temp:
            highest_temp = temp
        else:
            pass
    
    return temps.index(highest_temp)

weekdays = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]

print(f"Bester Tag zum Schwimmen ist {weekdays[optimal_day(temp_list)]}")