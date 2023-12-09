import random
random.seed(random.randint(0,50))

list = []
for i in range(20):
    list.append(random.uniform(0,100))

#========== nur dieser Code-Abschnitt ist gefragt ==========

def get_druchschnitt(numbers):
    return(sum(numbers)/len(numbers))

def get_nearest_index(nums):
    average = get_druchschnitt(nums)
    dist = 1000
    closest = -1
    for num in nums:
        if abs(num - average) < dist:
            dist = abs(num - average)
            closest = num

    return nums.index(closest)

#========== nur dieser Code-Abschnitt ist gefragt ==========

index = get_nearest_index(list)

print(index, list[index], get_druchschnitt(list))