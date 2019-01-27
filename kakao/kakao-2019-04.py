# https://www.welcomekakao.com/learn/courses/30/lessons/42891?language=python3
'''
정확성 테스트: simulation을 짜면 돌아가는듯 함(시간 제약에 안걸리므로)
효율성 테스트: food_times에 대하여 sort하는 등, simulation을 일정시간 돌아가는듯 함
'''

# def solution(food_times, k):
#     if sum(food_times) <= k:
#         return -1

#     while True:
#         temp = [t for t in food_times if t > 0]
#         minimal = min(temp)
#         num_non_zeros = len(temp)

#         # k초에 먹을 음식의 위치를 찾음
#         if minimal * num_non_zeros > k:
#             rest = k % num_non_zeros
#             count = 0
#             for i in range(len(food_times)):
#                 if food_times[i] != 0 and count == rest:
#                     return i+1

#                 if food_times[i] != 0:
#                     count += 1

#         # food_times의 값을 update
#         else:
#             food_times = [t-minimal if t > 0 else t for t in food_times]
#             k -= minimal * num_non_zeros


def solution(food_times, k):
    # -1인 경우 확인
    if sum(food_times) <= k:
        return -1

    N = len(food_times) # number of foods
    arr = sorted(food_times)
    arr.insert(0, 0) # pad
    for i in range(N):
        if (N-i)*(arr[i+1]-arr[i]) > k:
            rest = k % (N-i)
            count = 0
            for j in range(N):
                if food_times[j] >= arr[i+1] and count == rest:
                    return j+1

                if food_times[j] >= arr[i+1]:
                    count += 1

        else:
            k -= (N-i)*(arr[i+1]-arr[i])



for i in range(17):
    print(solution([1,2,3,4,5], i))

# print(solution([1,2,3,4,5], 6))