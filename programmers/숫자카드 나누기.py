from math import gcd

def solution(arrayA, arrayB):
    answer = 0
    ga = arrayA[0]
    gb = arrayB[0]
    # Math 모듈 이용해 배열의 최대 공약수를 구함
    # 최대공약수가 조건이 부합하지 않으면 해당 공약수 역시 불가능
    for a, b in zip(arrayA[1:], arrayB[1:]):
        ga, gb = gcd(a, ga), gcd(b, gb)

    for a in arrayA:
        if a % gb == 0:
            break
    else:
        answer = gb
    for b in arrayB:
        if b % ga == 0:
            break
    else:
        answer = max(answer, ga)
    return answer
