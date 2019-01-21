# https://www.acmicpc.net/problem/3190 뱀

DIRS = [(0,1), (1,0), (0,-1), (-1,0)]

def solution(N, K, L, APPLES, ROTATES) :
	# -1: 벽, 0: 땅, 1: 사과
	arr = [[0] * (N+2) for _ in range(N+2)]
	for i in range(N+2) :
		arr[0][i] = -1
		arr[N+1][i] = -1
		arr[i][0] = -1
		arr[i][N+1] = -1

	for apple in APPLES :
		x, y = apple
		arr[x][y] = 1


	body = [(1, 1)]
	time = 0
	dir = (0, 1)
	curr_x, curr_y = 1, 1

	while True :
		time += 1
		dx, dy = dir
		curr_x += dx
		curr_y += dy

		# direction setting
		if ROTATES :
			X, C = ROTATES[0]
			if X == time :
				ROTATES.pop(0)
				if C == 'L' :
					temp = DIRS.pop()
					DIRS.insert(0, temp)
					dir = DIRS[0]
				elif C == 'D' :
					temp = DIRS.pop(0)
					DIRS.append(temp)
					dir = DIRS[0]

		# 몸이나 벽에 부딪히면 끝
		if (curr_x, curr_y) in body or arr[curr_x][curr_y] == -1 :
			print(time)
			return


		body.append((curr_x, curr_y))
		if arr[curr_x][curr_y] == 1 :
			arr[curr_x][curr_y] = 0 # 사과를 먹으면 없어짐
		else :
			body.pop(0)



if __name__ == '__main__' :
	N = int(input())
	K = int(input())
	APPLES = [0] * K
	for i in range(K) :
		x, y = [int(x) for x in input().split(' ')]
		APPLES[i] = (x, y)

	L = int(input())
	ROTATES = [0] * L
	for i in range(L) :
		X, C = input().split(' ')
		ROTATES[i] = (int(X), C)

	solution(N, K, L, APPLES, ROTATES)