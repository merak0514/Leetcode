import sys
line = sys.stdin.readline().strip()
n = int(line)
line = sys.stdin.readline().strip()
result = [0] * n
ll = list(map(int, line.split()))
for i in range(n):
    if result[i] == 0:
        for j in range(i+1, n):
            if ll[i] & ll[j] == 0:
                result[i] = 1
                result[j] = 1
        if result[i] == 0:
            result[i] = -1
print(' '.join(str(i) for i in result))
