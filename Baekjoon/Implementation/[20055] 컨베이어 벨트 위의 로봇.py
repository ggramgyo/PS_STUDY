import sys
from collections import deque


# 조건 1번
def moving():
    move.appendleft(move.pop())
    # 같이 이동이라 내구성 감소 x
    for i in range(len(robot)-1, -1, -1):
        robot[i] += 1
        # 내리는 위치 도달 시 제거
        if robot[i] == N-1:
            robot.pop()

# 조건 2번
def moving_adding_robot():
    global DurabilityZeroCount
    # 한칸씩 전진
    for i in range(len(robot)-1, -1, -1):
        # 이동 가능성 조사
        if move[robot[i]+1] > 0:
            try:
                if robot[i+1] == robot[i]+1:
                    continue
            except:
                pass
            robot[i] += 1
            move[robot[i]] -= 1
            # 내리는 위치 도달 시 제거
            if robot[i] == N-1:
                robot.pop()

    # 전진 후 올리는 위치 체크 후 추가 // 조건 3번
    if move[0] != 0:
        if (robot and robot[0] != 0) or not robot:
            robot.appendleft(0)
            move[0] -= 1

# 조건 4번
def checkCount():
    cnt = 0
    for x in range(2*N):
        if not move[x]:
            cnt += 1
            if cnt >= K:
                return True
    return False



N, K = map(int, sys.stdin.readline().split())
move = deque(map(int, sys.stdin.readline().split()))
time = 0
DurabilityZeroCount = 0
robot = deque()
while True:
    moving()
    moving_adding_robot()

    if checkCount():
        print(time+1)
        break
    time += 1