# https://www.acmicpc.net/problem/13460 구슬 탈출 2

LEFT = (0, -1)
RIGHT = (0, 1)
UP = (-1, 0)
DOWN = (1, 0)


def solution(N, M, ARR) :
	states = set() # 현재까지의 red, blue의 위치
	queue = []

	rx, ry, bx, by = -1, -1, -1, -1
	for i in range(N) :
		for j in range(M) :
			if ARR[i][j] == 'R' :
				rx, ry = i, j

			if ARR[i][j] == 'B' :
				bx, by = i, j

	states.add((rx, ry, bx, by))
	queue.append((ARR, 1, rx, ry, bx, by, LEFT))
	queue.append((ARR, 1, rx, ry, bx, by, RIGHT))
	queue.append((ARR, 1, rx, ry, bx, by, UP))
	queue.append((ARR, 1, rx, ry, bx, by, DOWN))
	result = -1

	# bfs
	while queue :
		arr, level, rx, ry, bx, by, dir = queue.pop(0)
		if level == 11 :
			break

		arr, success, rx, ry, bx, by = move(arr, dir, rx, ry, bx, by)
		if success == 1 :
			result = level
			break

		if success == 0 and (rx, ry, bx, by) not in states:
			states.add((rx, ry, bx, by))
			# 직전 방향을 제외한 3방향을 queue에 넣음
			if dir == LEFT :
				queue.append((arr, level+1, rx, ry, bx, by, RIGHT))
				queue.append((arr, level+1, rx, ry, bx, by, UP))
				queue.append((arr, level+1, rx, ry, bx, by, DOWN))
			elif dir == RIGHT :
				queue.append((arr, level+1, rx, ry, bx, by, LEFT))
				queue.append((arr, level+1, rx, ry, bx, by, UP))
				queue.append((arr, level+1, rx, ry, bx, by, DOWN))
			elif dir == UP :
				queue.append((arr, level+1, rx, ry, bx, by, RIGHT))
				queue.append((arr, level+1, rx, ry, bx, by, LEFT))
				queue.append((arr, level+1, rx, ry, bx, by, DOWN))
			elif dir == DOWN :
				queue.append((arr, level+1, rx, ry, bx, by, RIGHT))
				queue.append((arr, level+1, rx, ry, bx, by, UP))
				queue.append((arr, level+1, rx, ry, bx, by, LEFT))

	print(result)


# return (arr, 성공여부, red_x, red_y, blue_x, blue_y)
def move(ARR, dir, red_x, red_y, blue_x, blue_y) :
	arr = [row[:] for row in ARR] # deep copy
	dx, dy = dir
	result_red_x = -1
	result_red_y = -1
	result_blue_x = -1
	result_blue_y = -1

	# 빨간공 이동
	curr_x = red_x
	curr_y = red_y
	while True :
		next_x = curr_x + dx
		next_y = curr_y + dy

		if arr[next_x][next_y] == '#' :
			result_red_x = curr_x
			result_red_y = curr_y
			arr[red_x][red_y] = '.'
			break

		if arr[next_x][next_y] == 'O' :
			result_red_x = next_x
			result_red_y = next_y
			arr[red_x][red_y] = '.'
			break

		curr_x = next_x
		curr_y = next_y

	# 파란공 이동
	curr_x = blue_x
	curr_y = blue_y
	while True :
		next_x = curr_x + dx
		next_y = curr_y + dy

		if arr[next_x][next_y] == '#' :
			result_blue_x = curr_x
			result_blue_y = curr_y
			arr[blue_x][blue_y] = '.'
			break

		if arr[next_x][next_y] == 'O' :
			result_blue_x = next_x
			result_blue_y = next_y
			arr[blue_x][blue_y] = '.'
			break

		curr_x = next_x
		curr_y = next_y

	# 빨간공과 파란공의 위치가 같음
	if result_red_x==result_blue_x and result_red_y==result_blue_y :
		# 둘 다 구멍에 들어감 => 실패
		if arr[result_red_x][result_red_y] == 'O' :
			return ([[]], -1, 0, 0, 0, 0)

		# 둘 다 구멍에 들어가지 않음 => 빨간공 파란공의 위치 조정 후 다음 단계 진행
		drx, dry, dbx, dby = adjust(dir, red_x, red_y, blue_x, blue_y)
		result_red_x += drx
		result_red_y += dry
		result_blue_x += dbx
		result_blue_y += dby
		return (arr, 0, result_red_x, result_red_y, result_blue_x, result_blue_y)

	# 빨간공과 파란공의 위치가 다름
	else :
		# 빨간공이 구멍으로 들어감 => 성공
		if arr[result_red_x][result_red_y] == 'O' :
			return ([[]], 1, 0, 0, 0, 0)

		# 파란공이 구멍으로 들어감 => 실패
		if arr[result_blue_x][result_blue_y] == 'O' :
			return ([[]], -1, 0, 0, 0, 0)

		# 빨간공, 파란공 둘 다 구멍으로 들어가지 않음 => 다음 단계 진행
		return (arr, 0, result_red_x, result_red_y, result_blue_x, result_blue_y)


# 빨간공과 파란공이 같은 위치에 도달했을 때 겹치지 않도록 조정 해야 하는 정도를 return
def adjust(dir, red_x, red_y, blue_x, blue_y) :
	if dir == LEFT :
		if red_y < blue_y :
			return (0, 0, 0, 1)
		else :
			return (0, 1, 0, 0)
	elif dir == RIGHT :
		if red_y < blue_y :
			return (0, -1, 0, 0)
		else :
			return (0, 0, 0, -1)
	elif dir == UP :
		if red_x < blue_x :
			return (0, 0, 1, 0)
		else :
			return (1, 0, 0, 0)
	elif dir == DOWN :
		if red_x < blue_x :
			return (-1, 0, 0, 0)
		else :
			return (0, 0, -1, 0)



if __name__ == '__main__' :
	N, M = [int(x) for x in input().split(' ')]
	ARR = [0] * N
	for i in range(N) :
		ARR[i] = [x for x in input()]

	solution(N, M, ARR)



# N, M = 7, 7
# arr = [
# 	['#','#','#','#','#','#','#',],
# 	['#','.','.','.','R','B','#',],
# 	['#','.','#','#','#','#','#',],
# 	['#','.','.','.','.','.','#',],
# 	['#','#','#','#','#','.','#',],
# 	['#','O','.','.','.','.','#',],
# 	['#','#','#','#','#','#','#',],
# ]

# arr, success, rx, ry, bx, by = move(arr, RIGHT, 1, 4, 1, 5)
# if success == 0 :
# 	arr[rx][ry] = 'R'
# 	arr[bx][by] = 'B'
# print('success, rx, ry, bx, by', success, rx, ry, bx, by)
# for row in arr :
# 	print(row)