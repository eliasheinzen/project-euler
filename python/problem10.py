# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

from project_euler.problem3 import is_prime

if __name__ == '__main__':
    x = 2
    print(x)
    for i in range(3, 2000000, 2):
        if is_prime(i):
            print(i)
            x = x + i
    print(x)
