"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    count = 2
    while (len(list) != number_of_primes):
        if (isPrime(count)):
            list.append(count)
        count+=1
    return list

def isPrime(number):
    for x in range(int(number/2)+1):
        if (x == 0 or x == 1):
            continue
        if (number % x == 0):
            return False
    return True