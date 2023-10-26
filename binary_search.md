В первой строке даны целое число 1 <= n <= 10^5 и массив A[1…n] из n различных натуральных чисел, не превышающих 10^9, в порядке возрастания, во второй — целое число 1 <= k <= 10^5 и k натуральных чисел b1, …, bk, не превышающих 10^9. Для каждого i от 1 до k необходимо вывести индекс 1 <= j <= n, для которого A[j] = bi, или −1.

Sample Input:

5 1 5 8 12 13

5 8 1 23 1 11

Sample Output:

3 1 -1 1 -1

## Solution:
```
def binary_search(lst, target_num):
    left, right = 1, len(lst) - 1
    while left <= right:
        middle = (left + right) // 2
        if lst[middle] == target_num:
            return middle
        elif lst[middle] < target_num:
            left = middle + 1
        else:
            right = middle - 1
    return -1

def main():
    # To obtain 1-based indexes:
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    n = a[0]
    k = b[0]
    result = []

    for i in range(1, k + 1):
        index = binary_search(a, b[i])
        result.append(index)
    print(*result)

if __name__ == '__main__':
    main()
```