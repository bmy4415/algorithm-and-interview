# https://www.acmicpc.net/problem/11404


def solution(MAP, N) :
	for k in range(N) :
		for i in range(N) :
			for j in range(N) :
				if i == j :
					continue

				if MAP[i][k] == 0 or MAP[k][j] == 0 :
					continue

				if MAP[i][j] == 0 or MAP[i][k] + MAP[k][j] < MAP[i][j] :
					MAP[i][j] = MAP[i][k] + MAP[k][j]

	for row in MAP :
		print(' '.join([str(x) for x in row]))


if __name__ == '__main__' :
	N = int(input())
	M = int(input())

	MAP = [[0 for _ in range(N)] for _ in range(N)]

	for i in range(M) :
		start, end, cost = [int(x) for x in input().split(' ')]

		if MAP[start-1][end-1] == 0 or MAP[start-1][end-1] > cost :
			MAP[start-1][end-1] = cost


	solution(MAP, N)