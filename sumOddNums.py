"""
For a positive integer n calculate the result value, which is equal to the sum of the odd numbers of n.
Example,
n = 1234 result = 4
n = 246 result = 0
"""
result = 0
num = int(input('enter number:..'))
print('num = ', num)
iteration = 0
divider = 10

while num > 0:

    if num % 2 != 0:

        iteration += 1

        backNum1 = num % 10
        print(f'backNum{iteration} = ', backNum1)

        result += backNum1
        print('result = ', result)

        num = num - backNum1
        print('newNum = ', num, '\n')

    else:

        print('divider =', divider)
        preNextBackNum = num / divider
        divider = divider * 10

        if preNextBackNum % 2 != 0:

            iteration += 1

            backNum1 = preNextBackNum % 10
            print(f'backNum{iteration} = ', backNum1)

            result += backNum1
            print('result = ', result)

            if not num < backNum1 * divider:
                num = num - (backNum1 * 10)
                print('newNum = ', num, '\n')
            else:
                print('the end')
                break

print('result sum =', result)


