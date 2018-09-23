# Smallest multiple
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def is_divisible_by_integers_until_20(x):
    return x % 2 == 0 and x % 3 == 0 and x % 4 == 0 and x % 5 == 0 and x % 7 == 0 and x % 8 == 0 \
           and x % 9 == 0 and x % 11 == 0 and x % 12 == 0 and x % 13 == 0 and x % 14 == 0 and x % 16 == 0 \
           and x % 17 == 0 and x % 18 == 0 and x % 19 == 0


for i in range(20, 232792561, 20):
    if is_divisible_by_integers_until_20(i):
        print(i)
