# https://www.welcomekakao.com/learn/courses/30/lessons/42889?language=python3
'''
stages를 돌면서 dictionary에 [stage, 도달하였으나 풀지 못한 player 수, 도달한 player 수]를 저장 후
dictionary를 이용해서 answer 구함
'''


def solution(N, stages):
    answer = []
    stage_dict = dict() # key: stage, value: [도달하였으나 풀지 못한 player 수, 도달한 player 수]
    # initialize
    for i in range(1, N+1):
        stage_dict[i] = [0, 0]

    for s in stages:
        # 모든 문제를 다 푼 경우 => 도달한 player 수 update
        if s == N+1:
            for i in range(1, s):
                stage_dict[i][1] += 1

        # 1~(s-1)번 까지 풀고, s번은 도전하였으나, s번은 못 푼 경우
        else:
            stage_dict[s][0] += 1
            for i in range(1, s+1):
                stage_dict[i][1] += 1

    # 확률 계산
    for k in stage_dict:
        if stage_dict[k][1] == 0:
            prob = 0
        else:
            prob = stage_dict[k][0] / stage_dict[k][1]
        answer.append((k, prob))

    answer.sort(key=lambda x: (x[1], -x[0]), reverse=True)
    return list(map(lambda x: x[0], answer))


result = solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
for r in result:
    print(r)