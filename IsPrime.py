import math

def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return n != i

def prime_factor(n):
    list = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            n /= i
            list.append(i)
            i = 2
        else:
            i += 1
    if n != 1:
        list.append(int(n))
    return list

def devisor(n):
    list = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            list.append(i)
            if i != n/i:
                list.append(int(n/i))
        i += 1
    return list

print(devisor(81))