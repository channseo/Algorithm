n = int(input())

for i in range(n):
    a, b, c = map(int, input().split())

    floor = c % a
    num = (c//a)+1

    if floor == 0:
        floor = a
        num -= 1

    print(floor * 100 + num)