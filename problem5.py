# Smallest multiple
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# A: 232792560

# Brute Force Solution ~> 5-6 secs
# def is_divisible_by_integers_from_1_to_20(x):
#     return x % 3 == 0 and x % 5 == 0 and x % 7 == 0 and x % 8 == 0 and x % 9 == 0 and x % 11 == 0 \
#            and x % 12 == 0 and x % 13 == 0 and x % 14 == 0 and x % 15 == 0 and x % 16 == 0 and x % 17 == 0 \
#            and x % 18 == 0 and x % 19 == 0
#
#
# for i in range(20, 232792561, 20):
#     if is_divisible_by_integers_from_1_to_20(i):
#         print(i)

primes, powers, a = [2, 3, 5, 7, 11, 13, 17, 19], [4, 2, 1, 1, 1, 1, 1, 1], [0 for i in range(8)]
answer = 1
print(primes, powers, a)

for i in range(len(primes)):
    a[i] = pow(primes[i], powers[i])
    answer = answer * a[i]
    print(primes[i], '^', powers[i], '=', a[i])

print('Resultado:', answer)
