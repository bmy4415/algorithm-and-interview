# https://www.acmicpc.net/problem/14889 스타트와 링크
from itertools import combinations

DEBUG = False


def solution(arr, n) :
    score_map = makeScoreMap(arr, n)
    peoples = range(n)
    team_combinations = combinations(peoples, int(n/2))

    MIN = 1000000
    for combination in team_combinations :
        result = check(n, combination, score_map)

        if DEBUG :
            print('combination, result: ', (combination[0]+1, combination[1]+1), result)

        if result < MIN :
            MIN = result

        if MIN == 0 :
            break

    print(MIN)

# 해당 조합에 대하여 양 팀의 능력치의 차이를 구함
def check(n, team1, score_map) :
    team1 = list(team1)
    team2 = set(range(n))
    for member in team1 :
        team2.remove(member)

    team2 = list(team2)

    score_team1 = 0
    comb_team1 = combinations(team1, 2)
    for comb in comb_team1 :
        score_team1 += score_map[comb]

    score_team2 = 0
    comb_team2 = combinations(team2, 2)
    for comb in comb_team2 :
        score_team2  += score_map[comb]

    return abs(score_team1 - score_team2)


# i와 j가 같은팀이 되었을 때의 능력치 값을 저장
# key: (i,j) value: Sij
def makeScoreMap(arr, n) :
    result = {}
    for i in range(n) :
        for j in range(i+1, n) :
            result[(i, j)] = arr[i][j] + arr[j][i]

    return result


if __name__ == '__main__' :
    N = int(input())
    ARR = []

    for _ in range(N) :
        row = [int(x) for x in input().split(' ')]
        ARR.append(row)

    solution(ARR, N)