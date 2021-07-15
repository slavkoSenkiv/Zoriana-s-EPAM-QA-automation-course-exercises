num = 567
result = 0

while num > 0:

    print('current num =', num)
    oneVsZero = num - (num - 1)
    print('oneVsZero =', oneVsZero)
    print('loverNum =', num - oneVsZero)

    if oneVsZero == 1:
        result += oneVsZero
        print('result =', result, '\n')
        num = (num - oneVsZero) / 2

    if oneVsZero == 0:
        num = num / 2

print(result)