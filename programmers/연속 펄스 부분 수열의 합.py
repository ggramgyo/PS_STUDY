def solution(sequence):
    answer = 0
    l = len(sequence)
    dp = [0] * l
    dp[0] = sequence[0]
    if l == 1:
        return max(dp[0], -dp[0])
    else:
        for i in range(1, l, 2):
            sequence[i] *= -1
        for i in range(1, l):
            dp[i] = max(dp[i-1] + sequence[i], sequence[i]) 
        answer = max(dp)
        
        for i in range(l):
            sequence[i] *= -1
        dp[0] = sequence[0]
        
        for i in range(1, l):
            dp[i] = max(sequence[i], sequence[i] + dp[i-1])
        answer = max(answer, max(dp))
    
    return answer