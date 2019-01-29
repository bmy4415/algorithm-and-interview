# https://www.welcomekakao.com/learn/courses/30/lessons/42841?language=python3
'''

'''
from itertools import permutations


# strike, ball을 계산
def cal(src, dest):
    src = str(src)
    dest = str(dest)
    s, b = 0, 0

    for i in range(len(src)):
        if src[i] == dest[i]:
            s += 1

        elif src[i] in dest[:i] + dest[i+1:]:
            b += 1

    return s, b


def solution(baseball):
    candidates = permutations(range(1, 10), 3)
    candidates = [100*x[0] + 10*x[1] + x[2] for x in candidates]

    for question in baseball:
        temp = []
        number, s, b = question
        for c in candidates:
            _s, _b = cal(number, c)
            if (s, b) == (_s, _b):
                temp.append(c)

        candidates = temp

    return len(candidates)



print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]])) # 2