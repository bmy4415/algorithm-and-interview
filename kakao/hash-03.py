# https://www.welcomekakao.com/learn/courses/30/lessons/42578?language=python3


def solution(clothes):
    dic = dict()
    for cloth in clothes:
        name, case = cloth
        if case in dic:
            dic[case].append(name)
        else:
            dic[case] = [name]

    all_cases = 1
    # 모든 조합(종류 별로 하나도 안입거나 1개만 입는 경우의 곱)에서 모든 종류에 대해서 하나도 안입는 경우를 빼면 됨
    for case in dic:
        all_cases *= len(dic[case]) + 1

    return all_cases - 1
