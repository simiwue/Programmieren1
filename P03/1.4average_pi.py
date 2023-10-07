import math

#first part of the formula
const_factor = (2*math.sqrt(2))/9801

n = 0
sum = 0
term = 1

#building the sum with n=0 -> whatever until the term added to the sum is too small
while term > 1e-15:
    term = (math.factorial(n) / math.factorial(4*n)**4) * ((1103 + 26390*n) / 396**(4*n))
    sum += term
    n += 1 

pi = 1/(const_factor * sum)

print(pi)