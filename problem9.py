# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a2 + b2 = c2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

if __name__ == '__main__':
    for c in range(3, 995):
        for b in range(2, c):
            for a in range(1, b):
                if a * a + b * b == c * c and a + b + c == 1000:
                    print(str(a) + ' * ' + str(b) + ' * ' + str(c) + ' = ' + str(a * b * c))
                    break
