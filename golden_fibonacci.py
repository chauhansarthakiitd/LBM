# calculate the fibonacci number using Binet's formula formula

def fib_golden(n):
    phi = (1 + 5 ** 0.5) / 2.0
    return int(round((phi ** n - (1 - phi) ** n) / 5 ** 0.5))


if __name__ == '__main__':
    print(fib_golden(10))
