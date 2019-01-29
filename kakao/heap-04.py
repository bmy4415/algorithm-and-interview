# https://www.welcomekakao.com/learn/courses/30/lessons/42628?language=python3
'''
min heap과 max heap을 둘 다 이용하되
한쪽 heap에서 지워진 것을 다른쪽 heap에서 알 수 있도록 array를 이용하여 삭제 여부를 저장
heap에 중복된 숫자가 들어올 수 있으므로 숫자를 key로 갖고 삭제 여부를 value로 갖는 dictionary는 사용 불가능함

Insert: min heap, max heap, arr에 모두 insert
max heap pop: max heap에서 pop 하고 arr에 표시
min heap pop: min heap에서 pop 하고 arr에 표시
'''


import heapq


def solution(operations):
    min_heap = []
    max_heap = []
    arr = [] # 존재 여부를 확인하기 위한 list

    for command in operations:
        # min heap, max heap, arr에 추가
        if command[0] == 'I':
            num = int(command.split(' ')[1])
            index = len(arr)
            heapq.heappush(max_heap, (-num, index))
            heapq.heappush(min_heap, (num, index))
            arr.append(True)

        # max heap에서 제거, arr에서 제거 표시
        elif command == 'D 1':
            while len(max_heap) != 0:
                num, index = heapq.heappop(max_heap)
                if arr[index]:
                    arr[index] = False
                    break

        # min heap에서 제거, arr에서 제거 표시
        elif command == 'D -1':
            while len(min_heap) != 0:
                num, index = heapq.heappop(min_heap)
                if arr[index]:
                    arr[index] = False
                    break

    max_val = 0
    min_val = 0

    while len(max_heap) != 0:
        num, index = heapq.heappop(max_heap)
        if arr[index]:
            max_val = -num
            break

    while len(min_heap) != 0:
        num, index = heapq.heappop(min_heap)
        if arr[index]:
            min_val = num
            break

    return [max_val, min_val]


operations1 = ['I 16','D 1'] # [0, 0]
operations2 = ['I 7','I 5','I -5','D -1'] # [7, 5]

print(solution(operations1))
print(solution(operations2))