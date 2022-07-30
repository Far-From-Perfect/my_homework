def fib(n):
    fib1, fib2 = 0, 1
    num = 0
    if n <= 1:
        return 1
    else:
        for i in range(n - 1):
            num = fib1 + fib2
            fib1 = fib2
            fib2 = num
        return num


def fib_m(n):
    """Последняя цифра числа Фибоначчи"""
    fib1, fib2 = 0, 1
    num = 0
    if n <= 1:
        return 1
    else:
        for i in range(n-1):
            num = (fib1 + fib2) % 10
            fib1 = fib2
            fib2 = num
        return num


def fib_mod(n, m):
    """Поиск остатка от деления n-числа Фибоначчи на m через период Пизано"""
    if n <= 1:
        return 1
    else:
        k, x = 1, [1, 1]
        lst = [0]
        while x != [0, 1]:
            k += 1
            lst.append(x[0])
            x = [x[1], (x[0]+x[1]) % m]
        return lst[n % k]


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()