# https://www.acmicpc.net/problem/14891 톱니바퀴


DEBUG = False

LEFT_END = 0
RIGHT_END = 3
RIGHT_TOOTH_INDEX = 2
LEFT_TOOTH_INDEX = 6
CLOCK_UNWISE = -1
CLOCK_WISE = 1
LEFT = 0
RIGHT = 1


def solution(TOBNI, ACTIONS) :
	for action in ACTIONS :
		index, direction = action
		simulate(TOBNI, index-1, direction)

		# if DEBUG :
		# 	print('after action: ', action)
		# 	for row in TOBNI :
		# 		print(row)

	score = calculagteScore(TOBNI)
	print(score)


def calculagteScore(TOBNI) :
	score = 0

	if DEBUG :
		print('inner calculate', TOBNI[0][0], TOBNI[1][0], TOBNI[2][0], TOBNI[3][0])
		for row in TOBNI :
			print(row)

	if TOBNI[0][0] == 1 :
		score += 1
	if TOBNI[1][0] == 1 :
		score += 2
	if TOBNI[2][0] == 1 :
		score += 4
	if TOBNI[3][0] == 1 :
		score += 8

	return score


# 회전 방향 toggle
def toggle(direction) :
	if direction == CLOCK_WISE :
		return CLOCK_UNWISE
	else :
		return CLOCK_WISE


# 해당 action을 실행
def simulate(TOBNI, index, direction) :
	# 왼쪽 방향
	checkAndRorate(TOBNI, index-1, LEFT, toggle(direction))
	# 오른쪽 방향
	checkAndRorate(TOBNI, index+1, RIGHT, toggle(direction))
	# 본체

	# if DEBUG :
	# 	print('-------------after left right rotate-----------------')
	# 	print('index, direction: ', index, direction)
	# 	for row in TOBNI :
	# 		print(row)


	if DEBUG :
		print('original rotate, index, direction: ', index, direction)
	if direction == CLOCK_UNWISE :
		# 반시계방향 회전
		temp = TOBNI[index].pop(0)
		TOBNI[index].append(temp)
	elif direction == CLOCK_WISE :
		# 시계방향 회전
		temp = TOBNI[index].pop()
		TOBNI[index].insert(0, temp)

	if DEBUG :
		print('after action: ', index, direction)
		for row in TOBNI :
			print(row)


## TOBNI, TOBNI index, (left or right), (clock unwise or clock wise)
def checkAndRorate(TOBNI, index, dir, rot_dir) :
	# base case
	if index < LEFT_END or index > RIGHT_END :
		return

	if dir == LEFT :
		# 왼쪽방향
		if TOBNI[index][RIGHT_TOOTH_INDEX] != TOBNI[index+1][LEFT_TOOTH_INDEX] :
			# 회전대상, 왼쪽것 처리 후 회전
			checkAndRorate(TOBNI, index-1, LEFT, toggle(rot_dir))

			if DEBUG :
				print('rotate, index, dir: ', index, rot_dir)

			if rot_dir == CLOCK_UNWISE :
				# 반시계방향 회전
				temp = TOBNI[index].pop(0)
				TOBNI[index].append(temp)
			elif rot_dir == CLOCK_WISE :
				# 시계방향 회전
				temp = TOBNI[index].pop()
				TOBNI[index].insert(0, temp)

	elif dir == RIGHT :
		# 오른쪽방향
		if TOBNI[index][LEFT_TOOTH_INDEX] != TOBNI[index-1][RIGHT_TOOTH_INDEX] :
			# 회전대상, 오른쪽것 처리 후 회전
			checkAndRorate(TOBNI, index+1, RIGHT, toggle(rot_dir))

			if DEBUG :
				print('rotate, index, dir: ', index, rot_dir)

			if rot_dir == CLOCK_UNWISE :
				# 반시계방향 회전
				temp = TOBNI[index].pop(0)
				TOBNI[index].append(temp)
			elif rot_dir == CLOCK_WISE :
				# 시계방향 회전
				temp = TOBNI[index].pop()
				TOBNI[index].insert(0, temp)

	return



if __name__ == '__main__' :
	TOBNI = [[int(x) for x in input()] for _ in range(4)]
	K = int(input())

	ACTIONS = []
	for _ in range(K) :
		index, direction = [int(x) for x in input().split(' ')]
		ACTIONS.append((index, direction))

	solution(TOBNI, ACTIONS)