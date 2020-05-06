import math
import sys
T = int(sys.stdin.readline().strip())
data = []
for i in range(T):
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    A, B, C = values
    data.append(values)

    a = 1/(2*A)
    b = 1 / B
    c = -C/B
    delta = math.pow(b, 2) + 4*a*c
    if delta <= 0:
        print(0)
    else:
        x1 = (b - math.sqrt(delta)) / (2 * a)
        x2 = (b + math.sqrt(delta)) / (2 * a)
        ans = (-1/3*a*pow(x2, 3)+c*x2+0.5*b*math.pow(x2, 2)) - (-1/3*a*pow(x1, 3)+c*x1+0.5*b*math.pow(x1, 2))
        print(ans)
