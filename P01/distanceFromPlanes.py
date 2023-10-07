import math


#get all info from user
x1 = float(input('x from plane1'))
y1 = float(input('y from plane1'))
x2 = float(input('x from plane2'))
y2 = float(input('y from plane2'))

#calculate distance and round it
d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
d = round(d, 2)

print('Distance between planes: ' + str(d))

