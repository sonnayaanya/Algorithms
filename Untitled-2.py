def fibonacci(n):
    a = 1
    b = 1
    if n == 1: 
        return 1
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b

def main():
    n = int(input())
    print(fibonacci(n))

if __name__ == "__main__":
    main()