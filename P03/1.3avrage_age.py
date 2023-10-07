user_input = ""
age_list = []

#add inputs to age_list until user writes "done"
while user_input != "done":
    user_input = input('Enter age.\nIf done, write "done"')
    
    #check if user_input is an int
    try:
        age_list.append(int(user_input))

    # if user_input is "done", leave the while-loop, otherwise ignore input and ask again   
    except ValueError:
        if user_input == "done":
            break
        else:
            print("That's not an int!")

age_average = sum(age_list) / len(age_list)
print("Average age is: " + str(age_average))
