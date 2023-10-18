По данному числу 1 <= n <= 10^9 найдите максимальное число k, для которого n можно представить как сумму k различных натуральных слагаемых. Выведите в первой строке число k, во второй — k слагаемых.

Sample Input 1:

4

Sample Output 1:

2

1 3 

Sample Input 2:

6

Sample Output 2:

3

1 2 3 

# Solution:
def summands(n):
    answer = []
    last_num = 1
    if n == 1 or n == 2:
        answer.append(n)
    else:
        while n - last_num > last_num:
            answer.append(last_num)
            n -= last_num
            last_num += 1
        answer.append(n)
    return answer

def main():
    n = int(input())
    result = summands(n)
    print(len(result))
    print(*result)

if __name__ == "__main__":
    main()
```
