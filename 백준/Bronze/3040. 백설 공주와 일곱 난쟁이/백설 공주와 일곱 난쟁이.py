from itertools import combinations

# 아홉 개의 정수 입력받기
numbers = [int(input()) for _ in range(9)]

# 합이 100인 조합 찾기
for comb in list(combinations(numbers, 7)):
    if sum(comb) == 100:
        result = comb
        break

# 결과 출력
for num in result:
    print(num)
