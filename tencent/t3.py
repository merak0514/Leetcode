import sys
line = sys.stdin.readline().strip()
n, m = list(map(int, line.split()))
bad = []
scores = [[0] * n for _ in range(m)]
for i in range(m):
    line = sys.stdin.readline().strip()
    a, b = list(map(int, line.split()))
    if a == 1:
        bad.append(b)
    elif a == 2:
        flag = 0
        for j in range(b, n+1):
            if place[j] == 1:
                print(j)
                flag = 1
                break
        if not flag:
            print(-1)