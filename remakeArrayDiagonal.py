"""In a predetermined two-dimensional integer array (square matrix) matrix
insert 0 into elements to the left side of the main diagonal, and I into
elements to the right side of the diagonal.
Example
{{2, 4, 3,3}, {{2, 1, 1, 1},
(5.7, 8,5), {0, 7, 1, 1),
(2, 4, 3, 3), {0,0,3,1),
{5, 7, 8,5)} {0, 0, 0,5}}"""
"""for i in range(len(ar)):
    print(f'ar[{i}] =', ar[i])
    for x in range(len(ar[i])):
        print(ar[i][x])"""

arY = [1, 2, 3, 4]
arX = [[[1.1], [1.2], [1.3]], [[2.1], [2.2], [3.3]]]

a = []
b = [[1, 2, 3, 4], [1, 2, 3, 4]]


ar = [[2, 4, 3, 3],
     [5, 7, 8, 5],
     [2, 4, 3, 3],
     [5, 7, 8, 5]]
print(ar)

print('ar =')
for i in range(len(ar)):
    print(ar[i])

for y in range(len(ar)):
    for x in range(len(ar[y])):

        if y < x:
            ar[y][x] = 0
        if y > x:
            ar[y][x] = 1

print('newAr =')
for i in range(len(ar)):
    print(ar[i])

