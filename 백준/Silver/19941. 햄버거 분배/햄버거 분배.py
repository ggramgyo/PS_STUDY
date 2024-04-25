import sys

N, K = map(int, sys.stdin.readline().split())
hams = list(sys.stdin.readline().rstrip())
person = []
for i in range(N):
    if hams[i] == 'P':
        person.append(i)
count = 0
for i in range(len(person)):
    front = False
    for j in range(K, -1 , -1):
        idx = person[i] - j

        if 0 <= idx < N and hams[idx] == 'H':
            hams[idx] = 'E'
            front = True
            count += 1
            break

    if not front:
        for j in range(K+1):
            idx = person[i] + j
            if 0 <= idx < N and hams[idx] == 'H':
                hams[idx] = 'E'
                count += 1
                break

print(count)