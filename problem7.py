# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

from project_euler.problem3 import is_prime

if __name__ == '__main__':
    i, j = 1, 3
    print("1 2")
    while True:
        if is_prime(j):
            i += 1
            print(i, j)
        if i == 10001:
            break
        j += 2
    print(i, j)
