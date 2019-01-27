# https://www.welcomekakao.com/learn/courses/30/lessons/42890?language=python3
'''
모든 가능한 column 조합을 구하고
각 조합에 대하여 2가지 조건(unique, minimal)을 만족하는지 확인
'''

from itertools import combinations

def solution(relation):
    # columns가 relation을 uniquely identify 하는지 확인
    def is_unique(relation, columns):
        arr = []
        for r in relation:
            arr.append(tuple([r[c] for c in columns]))

        return len(arr) == len(set(arr))

    columns = [i for i in range(len(relation[0]))]
    count = 0
    possible_combs = []

    i = 1
    while True:
        if i > len(columns):
            break

        all_combs = combinations(columns, i)
        # column 조합에 대해 candidate key 조건 만족하는지 확인
        for comb in all_combs:
            # minimal 확인
            already_exist = False
            for p in possible_combs:
                if set(p) & set(comb) == set(p):
                    already_exist = True

            if already_exist:
                continue

            # unique 확인
            if is_unique(relation, comb):
                count += 1
                possible_combs.append(comb)

        i += 1

    return count


relation = [
    [100,"ryan","music",2],
    [200,"apeach","math",2],
    [300,"tube","computer",3],
    [400,"con","computer",4],
    [500,"muzi","music",3],
    [600,"apeach","music",2]
]
print(solution(relation))
