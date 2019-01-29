# https://www.welcomekakao.com/learn/courses/30/lessons/42840?language=python3
'''

'''


def solution(answers):
    N = len(answers)
    count = [0, 0, 0]
    for i in range(N):
        answer = answers[i]
        a1 = [1, 2, 3, 4, 5][i % 5]
        a2 = [2, 1, 2, 3, 2, 4, 2, 5][i % 8]
        a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5][i % 10]

        if a1 == answer:
            count[0] += 1

        if a2 == answer:
            count[1] += 1

        if a3 == answer:
            count[2] += 1

    max_val = max(count)
    result = []
    for i in range(3):
        if count[i] == max_val:
            result.append(i+1)

    return result
