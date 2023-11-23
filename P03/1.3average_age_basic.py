

age_list = []

num_people = int(input("How many people?"))

while len(age_list) < num_people:
    age = float(input("How old?"))

    age_list.append(age)

average_age = sum(age_list) / len(age_list)

print(average_age)