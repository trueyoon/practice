import math

a, b, v = map(int, input().split())
ans = (v-a)/(a-b) + 1

print(math.ceil(ans))
