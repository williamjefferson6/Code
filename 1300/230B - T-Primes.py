def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i*i, limit + 1, i):
                primes[j] = False
    return [num for num, is_prime in enumerate(primes) if is_prime]

def isTPrime(x, primes):
    sqrt_x = int(x**0.5)
    return x > 1 and sqrt_x * sqrt_x == x and sqrt_x in primes

n = int(input())
x = list(map(int, input().split()))

max_value = max(x)
primes = set(sieve_of_eratosthenes(int(max_value**0.5) + 1))

for num in x:
    if isTPrime(num, primes):
        print("YES")
    else:
        print("NO")
