import sys
from collections import defaultdict

s, p = map(int, sys.stdin.readline().split())
dna = sys.stdin.readline().rstrip()
tmp = list(map(int, sys.stdin.readline().split()))
chk = ['A', 'C', 'G', 'T']
chk_count = defaultdict(int)
for i in range(4):
    chk_count[chk[i]] = tmp[i]
# init
count = defaultdict(int)
for w in dna[:p]:
    count[w] += 1
start = 0
answer = 0
while start <= len(dna) - p:
    # 체크 후
    if count['A'] >= chk_count['A'] and count['C'] >= chk_count['C'] and count['G'] >= chk_count['G'] and count['T'] >= chk_count['T']:
        answer += 1
    # 이동
    count[dna[start]] -= 1
    if start + p < s:
        count[dna[start+p]] += 1
    start += 1

print(answer)


