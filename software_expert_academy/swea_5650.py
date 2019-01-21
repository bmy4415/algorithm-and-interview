# https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRF8s6ezEDFAUo 핀볼게임

LEFT = (0, -1)
RIGHT = (0, 1)
UP = (-1, 0)
DOWN = (1, 0)


def solution(problems) :
	for i, problem in enumerate(problems) :
		N, arr = problem
		result = answer(N, arr)

		print('#{} {}'.format(i+1, result))


def answer(N, ARR) :
	# 경계에 벽(5)를 만들어줌
	arr = []
	arr.append([5] * (N+2))
	for row in ARR :
		temp = row[:]
		temp.insert(0, 5)
		temp.append(5)
		arr.append(temp)
	arr.append([5] * (N+2))


	worm_holes = {}
	queue = []
	curr_max = 0
	for i in range(N+2) :
		for j in range(N+2) :
			# 모든 경우에 대해서 test
			if arr[i][j] == 0 :
				queue.append((i, j, LEFT))
				queue.append((i, j, RIGHT))
				queue.append((i, j, UP))
				queue.append((i, j, DOWN))

			# worm hole의 위치 파악
			if arr[i][j] in (6, 7, 8, 9, 10) :
				if arr[i][j] in worm_holes :
					worm_holes[arr[i][j]].append((i, j))
				else :
					worm_holes[arr[i][j]] = [(i, j)]


	# worm_holes[number][(x, y)] = (x', y')으로 설정
	for number in worm_holes :
		p1, p2 = worm_holes[number]
		worm_holes[number] = {}
		worm_holes[number][p1] = p2
		worm_holes[number][p2] = p1



	for state in queue :
		result = simulate(arr, state, worm_holes)
		if result > curr_max :
			curr_max = result



	# print('maps~~~')
	# for row in arr :
	# 	print(row)

	# print('worm holes~~')
	# for key in worm_holes :
	# 	print(key, worm_holes[key])

	return curr_max



# simulate후 return score
def simulate(arr, state, worm_holes) :
	x, y, dir = state
	dx, dy = dir
	curr_x = x + dx
	curr_y = y + dy
	score = 0

	while True :
		dx, dy = dir
		curr = arr[curr_x][curr_y]

		# 처음위치로 돌아옴 -> 종료
		if curr_x==x and curr_y==y :
			return score

		# 블랙홀 -> 종료
		if curr == -1 :
			return score

		if curr == 0 :
			curr_x += dx
			curr_y += dy
			continue

		if curr == 1 :
			score += 1
			if dir == LEFT :
				dir = UP
				curr_x -= 1
			elif dir == RIGHT :
				dir = LEFT
				curr_y -= 1
			elif dir == UP :
				dir = DOWN
				curr_x += 1
			elif dir == DOWN :
				dir = RIGHT
				curr_y += 1
			continue

		if curr == 2 :
			score += 1
			if dir == LEFT :
				dir = DOWN
				curr_x += 1
			elif dir == RIGHT :
				curr_y -= 1
				dir = LEFT
			elif dir == UP :
				curr_y += 1
				dir = RIGHT
			elif dir == DOWN :
				curr_x -= 1
				dir = UP
			continue

		if curr == 3 :
			score += 1
			if dir == LEFT :
				curr_y += 1
				dir = RIGHT
			elif dir == RIGHT :
				curr_x += 1
				dir = DOWN
			elif dir == UP :
				curr_y -= 1
				dir = LEFT
			elif dir == DOWN :
				curr_x -= 1
				dir = UP
			continue

		if curr == 4 :
			score += 1
			if dir == LEFT :
				curr_y += 1
				dir = RIGHT
			elif dir == RIGHT :
				curr_x -= 1
				dir = UP
			elif dir == UP :
				curr_x += 1
				dir = DOWN
			elif dir == DOWN :
				curr_y -= 1
				dir = LEFT
			continue

		if curr == 5 :
			score += 1
			if dir == LEFT :
				curr_y += 1
				dir = RIGHT
			elif dir == RIGHT :
				curr_y -= 1
				dir = LEFT
			elif dir == UP :
				curr_x += 1
				dir = DOWN
			elif dir == DOWN :
				curr_x -= 1
				dir = UP
			continue


		# 웜홀에 도달
		worm_x, worm_y = worm_holes[curr][(curr_x, curr_y)]
		curr_x = worm_x + dx
		curr_y = worm_y + dy


if __name__ == '__main__' :
	T = int(input())
	problems = [0] * T
	for i in range(T) :
		N = int(input())
		arr = [0] * N
		for j in range(N) :
			row = [int(x) for x in input().split(' ')[:N]]
			arr[j] = row

		problems[i] = (N, arr)

	solution(problems)