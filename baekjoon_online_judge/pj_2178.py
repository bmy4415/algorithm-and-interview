# https://www.acmicpc.net/problem/2178

def solution(maze, distance, queue) :
	N = len(maze)
	M = len(maze[0])

	while(len(queue)) :
		x, y = queue.pop(0) # dequeue

		#왼쪽
		if (y-1 >= 0 and distance[x][y-1] == 0 and maze[x][y-1] == 1) :
			queue.append((x, y-1)) # queue에 추가
			distance[x][y-1] = distance[x][y] + 1
		#오른쪽
		if (y+1 < M and distance[x][y+1] == 0 and maze[x][y+1] == 1) :
			queue.append((x, y+1)) # queue에 추가
			distance[x][y+1] = distance[x][y] + 1
		#위
		if (x-1 >= 0 and distance[x-1][y] == 0 and maze[x-1][y] == 1) :
			queue.append((x-1, y)) # queue에 추가
			distance[x-1][y] = distance[x][y] + 1
		#아래
		if (x+1 < N and distance[x+1][y] == 0 and maze[x+1][y] == 1) :
			queue.append((x+1, y)) # queue에 추가
			distance[x+1][y] = distance[x][y] + 1

	return distance[N-1][M-1]

if __name__ == '__main__' :
	# size
	N, M = [int(x) for x in input().split(' ')]

	# MAZE
	MAZE = []
	for i in range(N) :
		row = [int(x) for x in input()]
		MAZE.append(row)


	# print(N, M)
	# print(MAZE)


	# DISTNACE
	DISTANCE = []
	for i in range(N) :
		row = [0] * M
		DISTANCE.append(row)

	DISTANCE[0][0] = 1 # 첫번째 자리의 distance
	QUEUE = [(0, 0)] # 첫번째 자리 추가

	dist = solution(MAZE, DISTANCE, QUEUE)

	print(dist)
