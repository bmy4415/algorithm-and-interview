# https://www.acmicpc.net/problem/14502 연구소
from itertools import combinations


def solution(N, M, ARR) :
	points = []
	viruses = []
	for i in range(N) :
		for j in range(M) :
			if ARR[i][j] == 0 :
				points.append((i, j))
			elif ARR[i][j] == 2 :
				viruses.append((i, j))

	all_combs = combinations(points, 3)

	MAX = 0
	for comb in all_combs :
		result = check(N, M, ARR, viruses, comb)
		if result > MAX :
			MAX = result

	print(MAX)

# 주어진 comb에 대하여 안전지대의 값을 return함
def check(N, M, ARR, viruses, comb) :
	arr = [[x for x in row] for row in ARR] # deep copy
	queue = [x for x in viruses]

	for wall in comb :
		n, m = wall
		arr[n][m] = 1



	while(len(queue) > 0) :
		curr = queue.pop()
		n, m = curr
		arr[n][m] = 2

		# 바이러스가 퍼질 수 있는 곳 확인
		if n-1>=0 and arr[n-1][m] == 0 :
			queue.append((n-1, m))
		if n+1<N and arr[n+1][m] == 0 :
			queue.append((n+1, m))
		if m-1>=0 and arr[n][m-1] == 0 :
			queue.append((n, m-1))
		if m+1<M and arr[n][m+1] == 0 :
			queue.append((n, m+1))


	num_safe_zones = 0
	for i in range(N) :
		for j in range(M) :
			if arr[i][j] == 0 :
				num_safe_zones += 1

	# print('--------------------------')
	# print(comb, num_safe_zones)
	# for row in arr :
	# 	print(row)

	return num_safe_zones


if __name__ == '__main__' :
	N, M = [int(x) for x in input().split(' ')]
	ARR = []
	for _ in range(N) :
		row = [int(x) for x in input().split(' ')]
		ARR.append(row)

	solution(N, M, ARR)