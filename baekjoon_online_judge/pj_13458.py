# https://www.acmicpc.net/problem/13458 시험감독관


def solution(N, B, C, students) :
	count = N
	arr = students[:]
	arr = list(map(lambda x: x-B, arr)) # 총감독관

	for number in arr :
		if number > 0 :
			q, r = divmod(number, C)
			if r == 0 :
				count += q
			else :
				count += q+1

	print(count)


if __name__ == '__main__' :
	N = int(input())
	students = [int(x) for x in input().split(' ')]
	B, C = [int(x) for x in input().split(' ')]

	solution(N, B, C, students)