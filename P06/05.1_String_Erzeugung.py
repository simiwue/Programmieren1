list = range(1,100)

string_list = []
for num in list:
    string_list.append(str(num))
string = ",".join(string_list)

print(string)
