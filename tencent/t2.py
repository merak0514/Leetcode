import sys
line = sys.stdin.readline().strip()
n = int(line)
line = sys.stdin.readline().strip()
ll = list(map(int, line.split()))
def hm(a, b):
    c = a ^ b
    count = 0
    while(c):
        c &= (c-1)
        count += 1
    return count
ans = 0
for i in range(n):
    for j in range(i+1, n):
        h = hm(ll[i], ll[j])
        if h > ans:
            ans = h
print(ans)


