number = int(input())


def puissance(x, n):
    if n == 0:
        return 1
    else:
        return x * puissance(x, n-1)


print(puissance(2, 5))
