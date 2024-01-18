# ===========================================================
# What is the largest primefactor of the number 600851475143?
# ===========================================================


num = 600851475143
factor = 2

primes = []

while num > 1:
    if num % factor == 0:
      primes.append(factor)
      num = num / factor

    else:
      factor += 1

print(f'largest prime number is: {primes[len(primes)-1]}')