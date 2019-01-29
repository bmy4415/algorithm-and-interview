# https://www.welcomekakao.com/learn/courses/30/lessons/42576?language=python3


def solution(participant, completion):
    dic = dict()

    # key: name, value: name을 가진 사람의 숫자
    for p in participant:
        if p in dic:
            dic[p] += 1

        else:
            dic[p] = 1

    # 완주한 참가자는 count를 빼줌
    for c in completion:
        dic[c] -= 1

    # 완주하지 못한 한명을 찾음
    for people in dic:
        if dic[people] > 0:
            return people

print(solution(['leo', 'kiki', 'eden'], ['eden', 'kiki']))
print(solution(['marina', 'josipa', 'nikola', 'vinko', 'filipa'], ['josipa', 'filipa', 'marina', 'nikola']))
print(solution(['mislav', 'stanko', 'mislav', 'ana'], ['stanko', 'ana', 'mislav']))