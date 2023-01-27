""" def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
i=0
sum=0
while i<2000000: #input prime number you want to find (ex: 10001st prime number)
    i = i+1
    if is_prime(i):
        sum = sum+i
    print(i)
print('Answer: ')
print(sum) """

def sumPrimes(n):
    sum, sieve = 0, [True] * n
    for p in range(2, n):
        if sieve[p]:
            sum += p
            for i in range(p*p, n, p):
                sieve[i] = False
    return sum

print(sumPrimes(2000000))