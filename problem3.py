# Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# Os fatores primos de 13195 são 5, 7, 13 e 29
# Qual o maior fator primo do número 600851475143?


def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x):
            if x % n == 0:
                return False
        return True
        # return len([n for n in range(2, x) if x % n == 0]) == 0


for i in range(3, 10000, 2):
    if is_prime(i) and 600851475143 % i == 0:
        print(i)
