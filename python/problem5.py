# Smallest multiple
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# A: 232792560
from project_euler.problem3 import is_prime


def decompose_in_prime_factors(x):
    prime_factors_of_x, y, k = [], x, 2
    if x <= 1:
        return
    else:
        while y > 1:
            if is_prime(k) and y % k == 0:
                prime_factors_of_x.append(k)
                y = y / k
            elif y % k != 0:
                k = k + 1
    return prime_factors_of_x


if __name__ == '__main__':
    prime_factors = []
    powers_of_prime_factors = [1, 1, 1, 1, 1, 1, 1, 1]

    print('Decomposição de 1 a 20 em fatores primos:')
    for n in range(1, 21):
        n_prime_factors = decompose_in_prime_factors(n)
        print(n, '->', n_prime_factors)
        if is_prime(n) and n not in prime_factors:
            prime_factors.append(n)
        if n_prime_factors is not None:
            for m in n_prime_factors:
                x = n_prime_factors.count(m)
                powers_of_prime_factors[prime_factors.index(m)] = max(x,
                                                                      powers_of_prime_factors[prime_factors.index(m)])
    print(prime_factors)
    print(powers_of_prime_factors)

    answer = 1
    for n in range(0, len(prime_factors)):
        answer *= prime_factors[n] ** powers_of_prime_factors[n]
    print(answer)
