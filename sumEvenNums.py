"""
For a positive integer n calculate the result value, which is equal to the sum of the odd numbers of n.
Example,
n = 1234 result = 4
n = 246 result = 0
"""

result = 0
num = int(input('enter number:..'))
print('start num = ', num)

while num > 0:

    if num % 2 == 1:

        backNum1 = num % 10
        print('backNum1 = ', backNum1)

        result += backNum1
        print('result = ', result)

        num -= backNum1
        print('num = ', num, '\n')

    else:
        print('last num is odd')

print('result sum =', result)
