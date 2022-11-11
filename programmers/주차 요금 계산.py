import math
from collections import defaultdict


def cal(a: str, b: str):
    a = list(map(int, a.split(':')))
    b = list(map(int, b.split(':')))
    c = 0
    if b[1] - a[1] < 0:
        c = (b[0] - a[0] - 1) * 60 + 60 + (b[1] - a[1])
    else:
        c = (b[0] - a[0]) * 60 + b[1] - a[1]
    return c


def fee_cal(li: list, fees: list):
    default_time,  default_fee, unit_time, unit_fee = fees
    answer = []
    for l in li:
        k, v = l
        if sum(v)-default_time > 0:
            answer.append(default_fee + (math.ceil(float(sum(v)-default_time)/unit_time)) * unit_fee)
        else:
            answer.append(default_fee)
    return answer

def solution(fees, records):
    parkings = defaultdict()
    car_fee = defaultdict(list)
    for record in records:
        time, car_number, res = record.split(' ')

        if res == 'IN':
            parkings[car_number] = time
        else:
            car_fee[car_number].append(cal(parkings[car_number], time))
            parkings[car_number] = ''
    for k, v in parkings.items():
        if v != '':
            car_fee[k].append(cal(v, '23:59'))
    answer = fee_cal(sorted(list(car_fee.items()), key=lambda x: int(x[0])), fees)
    return answer
