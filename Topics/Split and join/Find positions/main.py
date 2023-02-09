numbers = [int(el) for el in input().replace(" ", ',').split(',')]
x = int(input())
cnt = 0
index = []

if x in numbers:
    for num in numbers:
        if num == x:
            index.append(cnt)
        cnt += 1
    print(*index)
else:
    print('not found')
