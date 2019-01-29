# https://www.welcomekakao.com/learn/courses/30/lessons/42629?language=python3

import heapq


import heapq


def solution(stock, dates, supplies, k):
    curr = stock
    supplies_minus = map(lambda x: -x, supplies)
    heap = list(zip(supplies_minus, dates)) # max heap을 이용하기 위해 supply를 음수로 저장
    heapq.heapify(heap)
    count = 0

    while curr < k:
        arr = []
        while True:
            supply, date = heapq.heappop(heap)
            # 해당 date에 사용 가능
            if date <= curr:
                count += 1
                curr += supply * -1
                break

            else:
                arr.append((supply, date))

        for (supply, date) in arr:
            heapq.heappush(heap, (supply, date))

    return count
