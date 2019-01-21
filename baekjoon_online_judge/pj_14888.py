# https://www.acmicpc.net/problem/14888 연산자 끼워넣기
from itertools import permutations


ADD = -1
SUB = -2
MUL = -3
DIV = -4
MAX = -1000000000
MIN = 1000000000

results = []


def solution(n, numbers, operators) :
	start = numbers[0]
	max, min = calculate(start, numbers[1:], operators)

	print(max)
	print(min)
	# print('max, min: ', max, min)


def calculate(curr, numbers, operators) :
	# print('curr, numbers, operators: ', curr, numbers, operators)
	# 남은 연산자가 모두 0임
	if operators.count(0) == 4 :
		return (curr, curr)

	sub_results = []

	# +가 남아있음
	if operators[0] != 0 :
		next = curr + numbers[0]
		next_numbers = numbers[1:]
		next_operators = [x for x in operators]
		next_operators[0] -= 1
		sub_results.append(calculate(next, next_numbers, next_operators))

	# -가 남아있음
	if operators[1] != 0 :
		next = curr - numbers[0]
		next_numbers = numbers[1:]
		next_operators = [x for x in operators]
		next_operators[1] -= 1
		sub_results.append(calculate(next, next_numbers, next_operators))

	# *가 남아있음
	if operators[2] != 0 :
		next = curr * numbers[0]
		next_numbers = numbers[1:]
		next_operators = [x for x in operators]
		next_operators[2] -= 1
		sub_results.append(calculate(next, next_numbers, next_operators))

	# /가 남아있음
	if operators[3] != 0 :
		next = 0
		if curr >= 0 :
			next = curr // numbers[0]
		else :
			next = ((curr * -1) // numbers[0]) * -1
		next_numbers = numbers[1:]
		next_operators = [x for x in operators]
		next_operators[3] -= 1
		sub_results.append(calculate(next, next_numbers, next_operators))


	# print('sub_results: ', sub_results)
	curr_max = max([x[0] for x in sub_results])
	curr_min = min([x[1] for x in sub_results])

	return (curr_max, curr_min)


if __name__ == '__main__' :
	N = int(input())
	NUMBERS = [int(x) for x in input().split(' ')]
	OPERATORS = [int(x) for x in input().split(' ')]

	solution(N, NUMBERS, OPERATORS)