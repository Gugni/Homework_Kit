n=int(input())
for _ in range(n, n+1):
    for __ in range(-1, n-_):
        print(_, end=' ')
    print()