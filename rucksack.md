Первая строка содержит количество предметов 1 <= n <= 10^3 и вместимость рюкзака 0 <= W <= 2⋅10^6. Каждая из следующих n строк задаёт стоимость 0 <= ci <= 2⋅10^6 и объём 0 < wi <= 2⋅10^6 (n, W, ci, wi — целые числа). Выведите максимальную стоимость частей предметов (от каждого предмета можно отделить любую часть, стоимость и объём при этом пропорционально уменьшатся), помещающихся в данный рюкзак, с точностью не менее трёх знаков после запятой.

Sample Input:

3 50

60 20

100 50

120 30

Sample Output:

180.000

# Solution:
```
def rucksack(n, w, items):
    price = 0
    items.sort(key = lambda x: x[2], reverse = True)
    while len(items) > 0:
        '''unpacking the values of list of lists. Without it one would need to use items[0][0], items[0][1], and items[0][2] to access the values.'''
        value, volume, ppu = items[0]
        if w > 0:
            if w >= volume:
                price += volume * ppu
                w -= volume
            else:
                price += w * ppu
                break
        items = items[1:]
    return f"{price:.3f}"

def main():
    n, w = map(int, input().split())
    items = []
    for _ in range(n):
        value, volume = map(int, input().split())
        ppu = value / volume
        items.append([value, volume, ppu])
    print(rucksack(n, w, items))
        
if __name__ == "__main__":
    main()
```
