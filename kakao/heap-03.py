# https://www.welcomekakao.com/learn/courses/30/lessons/42627?language=python3


import heapq


def solution(jobs):
    jobs.sort(key=lambda x: (x[0], x[1])) # (요청시간, job 길이)로 sort
    start, length = jobs[0]
    curr = start + length # 첫번째 작업 선택 후 현재시간
    total = length # sum of latency
    heap = [(x[1], x[0]) for x in jobs[1:]] # 첫 작업을 제외한 나머지 작업에 대해 (job 길이, 요청시간)으로 min heap 만듬
    heapq.heapify(heap)

    while True:
        if len(heap) == 0:
            break

        arr = [] # 선택되지 못한 job들의 모임
        while True:
            # 현재 진행중인 job과 겹치는 것이 하나도 안남은 경우 => arr에 있는 job중 가장 짧은 job을 실행
            if len(heap) == 0:
                heapq.heapify(arr)
                heap = arr
                length, start = heapq.heappop(heap)
                curr = length + start
                total += length
                break

            length, start = heapq.heappop(heap)
            # 기다리는 job이 있을 수 있으므로 skip
            if start > curr:
                arr.append((length, start))

            # 대기중인 job 중 최소 길이이므로 다음에 실행
            else:
                curr += length
                total += curr - start

                # skip된 job 다시 넣어줌
                for item in arr:
                    heapq.heappush(heap, item)
                break

    return int(total / len(jobs))


jobs = [[0, 3], [1, 9], [4, 6]]
# jobs = [[0,4], [0,3], [0,2]]
# jobs = [[0, 9], [0, 4], [0, 5], [0, 7], [0, 3]]
print(solution(jobs))
