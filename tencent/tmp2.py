import sys
K = 100003
def new_pow(a, b):
    if b == 1:
        return a % K
    if b % 2 == 0:
        r = new_pow(a, b / 2)
        return r ** 2 % K
    else:
        r = new_pow(a, (b-1) / 2)
        return (r ** 2 % K) * a % K
    # x = a % K
    # r = x
    # for i in range(1, b):
    #     r = r * x % K
    # return r
line = sys.stdin.readline().strip()
m, n = list(map(int, line.split()))
ans = (new_pow(m, n) - (m*new_pow(m-1, n-1))) % K
print(ans)
