import sys

N = int(sys.stdin.readline())
distances = list(map(int, sys.stdin.readline().split()))
gas = list(map(int, sys.stdin.readline().split()))
price = gas[0]
total = price * distances[0]
for i in range(1, N-1):
    if gas[i] < price:
        price = gas[i]
    total += price * distances[i]
print(total)