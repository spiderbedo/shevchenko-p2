for i in range(10, 99, 2):
    a = str(i)
    if (int(a[0]) + int(a[1])) % 2 != 0:
        print(i)
