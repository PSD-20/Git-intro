num = int(input())
for _ in range(num):
    n = int(input())

    a = divmod(n - 3, 10)
    s = '0123456789'
    if n == 1:
        print(9)
    elif n == 2:
        print(98)
    elif n == 3:
        print(989)
    else:
        print('989' + (s * a[0]) + s[:a[1]])