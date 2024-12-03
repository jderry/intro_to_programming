#!/usr/bin/python3

not_primes = [j for i in range(2, 11) for j in range(i*2, 101, i)]
primes = [x for x in range(2, 101) if x not in not_primes]
print(primes)
