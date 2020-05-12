import sys
line = sys.stdin.readline().strip()
n, m = list(map(int, line.split()))
scores = [[0] * n for _ in range(m)]
for i in range(n):
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    for j in range(m):
        scores[j][i] = values[j]
a = set()
for line in scores:
    oo = max(line)
    al = [i for i, j in enumerate(line) if j == oo]
    for k in al:
        a.add(k)
print(len(a))


