import sys
def isOdd(t):
    cnt = 0
    for i in t:
        if i in '13579':
            cnt += 1
    return cnt

def dfs(t, d):
    global minValue, maxValue
    if len(t) == 1:
        minValue = min(isOdd(t) + d, minValue)
        maxValue = max(isOdd(t)+d, maxValue)
        return
    elif len(t) == 2:
        dfs(str(int(t[0]) + int(t[1])), d + isOdd(t))
    else:
        cnt = isOdd(t)
        for x in range(1, len(t)-1):
            for y in range(x+1, len(t)):
                dfs(str(int(t[:x]) + int(t[x:y]) + int(t[y:])), d + cnt)
                
                
N = sys.stdin.readline().rstrip()
minValue = 987654321
maxValue = 0
dfs(N, 0)
print(minValue, maxValue)


