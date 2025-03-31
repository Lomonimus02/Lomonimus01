n = int(input())
cords = [0]*n
for i in range(n):
    cords[i] = int(input())
height = [0]*n
for i in range (n):
    height[i] = int(input())
lies = [0]*n
lies[0] = 1
lies [-1] = 1


max_h = height[0]+cords[0]
for i in range(1,n):
    if max_h >= cords[i]:
        lies[i] = 1
        max_h = max(max_h, cords[i] + height[i])
    else:
        break

min_h = height[0]+cords[0]
for i in range(1,n):
    if min_h <= cords[i]:
        lies[i] = 1
        min_h = min(min_h, cords[i] + height[i])
    else:
        break