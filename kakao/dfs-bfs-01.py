# https://www.welcomekakao.com/learn/courses/30/lessons/43165?language=python3
'''
dfs(=> recursion!!!)을 이용
각 숫자는 +, -의 부호를 갖을 수 있으므로 숫자를 하나씩 빼며 모든 경우를 고려
itertools.combinations을 사용해도 되지만, 이 경우 효율성 테스트에서 문제 생길 수 있음
예를들어 +++++, ++++- 인 경우, itertools를 사용하면 총 10번 계산하지만, recursion을 사용하면 앞의 ++++(4회)는 계산을 공유하고
마지막 +/-만 추가하여 총 6번 계산함
'''



def solution(numbers, target):
    # numbers를 다 사용한 경우
    if not numbers:
        if target == 0:
            return 1
        else:
            return 0

    number = numbers[0]

    return solution(numbers[1:], number - target) + solution(numbers[1:], number + target)




numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))
