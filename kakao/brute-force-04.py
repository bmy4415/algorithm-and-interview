# https://www.welcomekakao.com/learn/courses/30/lessons/42842?language=python3
'''

'''


# 가능한 (가로, 세로)를 모두 구함
def get_xy_pair(num_blocks):
    if num_blocks == 1:
        return [(1, 1)]

    candidates = []
    for i in range(1, num_blocks):
        if i**2 > num_blocks:
            break

        q, r = divmod(num_blocks, i)
        if r == 0: candidates.append((q, i))

    return candidates


def solution(brown, red):
    red_candidates = get_xy_pair(red)
    total_candidates = get_xy_pair(red + brown)

    for (x, y) in total_candidates:
        for (rx, ry) in red_candidates:
            if (x-rx) > 0 and (x-rx) % 2 == 0 and (y-ry) > 0 and (y-ry) % 2 == 0:
                return [x, y]


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))