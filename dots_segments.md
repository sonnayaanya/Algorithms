По данным n отрезкам необходимо найти множество точек минимального размера, для которого каждый из отрезков содержит хотя бы одну из точек.

В первой строке дано число 1 <= n <= 100 отрезков. Каждая из последующих n строк содержит по два числа 0 <= l <= r <= 109, задающих начало и конец отрезка. Выведите оптимальное число m точек и сами m точек. Если таких множеств точек несколько, выведите любое из них.

Sample Input 1:

3

1 3

2 5

3 6

Sample Output 1:

1

3 

Sample Input 2:

4

4 7

1 3

2 5

5 6

Sample Output 2:

2

3 6 

# Solution:
```
def dots_segments(coords):
    dots = []
    coords.sort(key = lambda i: i[1])
    dots.append(coords[0][1])
    for k in range(1, len(coords)):
        if coords[k][0] > dots[-1]:
            dots.append(coords[k][1])
            
    return [dot for dot in dots]

def main():
    length = int(input())
    coords = []
    for i in range(length):
        coords.append([int(x) for x in input().split()])
    result = dots_segments(coords)
    print(len(result))
    print(*result)
    
if __name__ == "__main__":
    main() 
```