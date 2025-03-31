k = int(input())
n = int(input())
v = [0]*n
v = [int(input()) for i in range (n)]
if sum(v)< k:
    return -1
else:
    v.sort()
    res = 2*k
while k > 0:
    k -= v[-1]
    v.pop()
    if k > 0:
        res += 2*k