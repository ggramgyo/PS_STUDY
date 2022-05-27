from collections import defaultdict
def solution(tickets):
    from_to = defaultdict(list)
    for ticket in tickets:
        f, t = ticket
        from_to[f].append(t)
        from_to[f].sort(reverse=True)
    stack = ["ICN"]
    answer = []
    while stack:
        f =  stack[-1]
        if not len(from_to[f]):
            answer.append(stack.pop())
        else:        
            stack.append(from_to[f].pop())

    return answer[::-1]
    
solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])