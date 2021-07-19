"""In a given array of integers nums swap values of the first and the last array
elements, the second and the penultimate etc., if the two exchanged values
are even.
Example,
(10,5, 3, 4) => (4,5, 3, 10)
{100, 2, 3, 4, 5) => (100, 4, 3, 2,5}
(100, 2, 3, 45, 33, 8, 4.54) => (54, 4, 3, 45, 33, 8, 2, 100)"""
ar = [100, 2, 3, 45, 33, 8, 4, 54]
"""print('\ni in range(len(ar):')
for i in range(len(ar)):
    print(f'ar[{i}] =', ar[i], end=", ")
    
print('\n\ni in range(int(len(ar)/2)):')
for i in range(int(len(ar)/2)):
    print(f'ar[{i}] =', ar[i], end=", ")

print('\n\nfind brothers:')
for i in range(int(len(ar) / 2)):
    print(f'ar[{i}] =', ar[i], 'is brother to', end=' ')
    print(f'ar[{len(ar) - i - 1}] =', ar[len(ar) - i - 1])

print('\nfind even brothers:')
for i in range(int(len(ar) / 2)):
    if ar[i] % 2 == 0 and ar[len(ar) - i - 1] % 2 == 0:
        print(ar[i], 'should be swaped with', ar[len(ar) - i - 1])"""

a = 0
b = 0
print('\nswapping even brothers:')
for i in range(int(len(ar) / 2)):
    if ar[i] % 2 == 0 and ar[len(ar) - i - 1] % 2 == 0:
        a = ar[i]
        b = ar[len(ar) - i - 1]
        ar[i] = b
        ar[len(ar) - i - 1] = a

print(ar)
