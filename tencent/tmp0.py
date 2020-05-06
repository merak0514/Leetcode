import math
import sys
line = sys.stdin.readline().strip()
n, m = list(map(int, line.split()))
C = []
W = []
for i in range(n):
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    c, w = values
    if (w/c) > 1/m:
        C.append(c)
        W.append(w)
ans = sum(W) - math.ceil(sum(C) / m)

print(ans)
