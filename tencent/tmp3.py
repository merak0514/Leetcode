import sys
matrix = []
line = sys.stdin.readline().strip()
n, k = list(map(int, line.split()))
add = 0
weight = []
for i in range(n):
    # 读取每一行
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    values = list(map(int, line.split()))
    if values in matrix:
        ind = matrix.index(values)
        weight[ind] += 1
    else:
        matrix.append(values)
        weight.append(1)
nn = len(matrix)
print(matrix)
ans = 0
for i in range(nn):
    a = matrix[i]
    for j in range(i+1, nn):
        b = matrix[j]
        l_sum = a[0] + b[0]
        flag = 1
        for l in range(1, k):
            if (a[l] + b[l]) != l_sum:
                flag = 0
                break
        if flag == 1:
            ans += weight[i] * weight[j]
print(ans)
print(weight)
for i in weight:
    if i > 1:
        ans += i * (i-1) / 2
print(int(ans))

