# Largest palindrome product
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

a, b, largest_palindrome = 0, 0, 0


def is_palindrome(x):
    x1 = str(x)
    y = round(len(x1) / 2)
    for n in range(0, y):
        if x1[n] != x1[len(x1) - 1 - n]:
            return False
    return True


for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        if is_palindrome(i * j) and (i * j) > largest_palindrome:
            a, b, largest_palindrome = i, j, i * j

print(str(a) + ' * ' + str(b) + ' = ' + str(largest_palindrome))
