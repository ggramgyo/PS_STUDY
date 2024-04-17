from sys import stdin
cnt = int(input())
for x in range(cnt):
    num1, num2 = map(int, stdin.readline().split())
    print(num1 + num2)