def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

counter=0
i=0
while counter<10001: #input prime number you want to find (ex: 10001st prime number)
    i = i+1
    if is_prime(i):
        counter = counter+1
print(i)
print(counter)