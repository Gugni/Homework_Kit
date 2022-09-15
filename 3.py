n=int(input())
for i in range(n, n+1):
    y = 1
    for _ in range(i):
        print(y, end=' ')
        y+=1
    print()
