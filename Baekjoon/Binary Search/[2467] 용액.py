import sys
N = int(sys.stdin.readline())
liquids = list(map(int, sys.stdin.readline().split()))
left = 0
right = N-1
min_value, min_li = float('inf'), []
while left <= right:
    if left == right:
        break
    mix = liquids[left] + liquids[right]
    if abs(mix) <= abs(min_value):
        min_li = [liquids[left], liquids[right]]
        min_value = abs(mix)
    if mix < 0:
        left = left + 1
    else:
        right = right - 1
print(*min_li)