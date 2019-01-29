# https://www.welcomekakao.com/learn/courses/30/lessons/42839?language=python3
'''

'''

from itertools import permutations


def is_prime(number):
    if number in [0, 1]:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def solution(numbers):
    result = set()

    for i in range(len(numbers)):
        cases = permutations(numbers, i+1)
        for case in cases:
            number = int(''.join(case))
            if is_prime(number):
                result.add(number)

    return len(result)


print(solution('17'))