# https://www.welcomekakao.com/learn/courses/30/lessons/42626?language=python3


import heapq


def solution(scoville, K):
    heapq.heapify(scoville) # min-heapify
    count = 0
    while True:
        if scoville[0] < K:
            if len(scoville) < 2:
                return -1

            food1 = heapq.heappop(scoville)
            food2 = heapq.heappop(scoville)
            mix_food = food1 + 2*food2
            count += 1
            heapq.heappush(scoville, mix_food)

        else:
            return count
