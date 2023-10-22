Первая строка входа содержит число операций 1 <= n <= 10^5. Каждая из последующих n строк задают операцию одного из следующих двух типов:

Insert x, где 0 <= x <= 10^9 — целое число;

ExtractMax.


* Sample Input:

6
Insert 200

Insert 10

ExtractMax

Insert 5

Insert 500

ExtractMax


* Sample Output:

200
500

# Solution:
```
import heapq

length = int(input())
l = []
popped = []

for _ in range(length):
    s = input()
    if s.startswith('Insert'):
        _, num = s.split()
        num = int(num)
        heapq.heappush(l, -num)
    elif s == 'ExtractMax':
        popped.append(-heapq.heappop(l))
        
print(*popped)
```
