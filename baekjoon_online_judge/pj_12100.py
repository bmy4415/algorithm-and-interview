# https://www.acmicpc.net/problem/12100 2048(Easy)

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3


def solution(N, ARR) :
	queue = []
	queue.append((ARR, 1, LEFT))
	queue.append((ARR, 1, RIGHT))
	queue.append((ARR, 1, UP))
	queue.append((ARR, 1, DOWN))
	max = 0

	while queue :
		arr, depth, dir = queue.pop(0)
		arr = slide(N, arr, dir)
		if depth == 5 :
			curr_max = largest(arr)
			if max < curr_max :
				max = curr_max
			continue

		if dir == LEFT :
			queue.append((arr, depth+1, RIGHT))
			queue.append((arr, depth+1, UP))
			queue.append((arr, depth+1, DOWN))
		elif dir == RIGHT :
			queue.append((arr, depth+1, LEFT))
			queue.append((arr, depth+1, UP))
			queue.append((arr, depth+1, DOWN))
		elif dir == UP :
			queue.append((arr, depth+1, LEFT))
			queue.append((arr, depth+1, RIGHT))
			queue.append((arr, depth+1, DOWN))
		elif dir == DOWN :
			queue.append((arr, depth+1, LEFT))
			queue.append((arr, depth+1, RIGHT))
			queue.append((arr, depth+1, UP))

	print(max)


def largest(arr) :
	max = 0
	N = len(arr)
	for i in range(N) :
		for j in range(N) :
			if arr[i][j] > max :
				max = arr[i][j]

	return max


def slide(N, ARR, dir) :
	if dir == LEFT :
		return left(N, ARR)
	elif dir == RIGHT :
		temp = left(N, reverse(ARR))
		result = reverse(temp)
		return result
	elif dir == UP :
		temp = left(N, transpose(ARR))
		result = transpose(temp)
		return result
	elif dir == DOWN :
		temp = left(N, reverse(transpose(ARR)))
		result = transpose(reverse(temp))
		return result


def left(N, ARR) :
	arr = [row[:] for row in ARR]
	temp = []
	for row in arr :
		non_zero = []
		for value in row :
			if value != 0 :
				non_zero.append(value)

		summed = []
		length = len(non_zero)
		i = 0
		while(i < length) :
			if i+1 < length and non_zero[i] == non_zero[i+1] :
				summed.append(non_zero[i] * 2)
				i += 2

			else :
				summed.append(non_zero[i])
				i += 1

		temp.append(summed)

	result = [[0]*N for _ in range(N)] # 으로 가득 차 있는 arr
	for i in range(N) :
		row = temp[i]
		for j in range(len(row)) :
			result[i][j] = temp[i][j]

	return result


def reverse(ARR) :
	result = []
	for row in ARR :
		result.append(row[::-1])

	return result


def transpose(ARR) :
	N = len(ARR)
	result = []
	for i in range(N) :
		result.append([row[i] for row in ARR])

	return result


if __name__ == '__main__' :
	N = int(input())
	ARR = [0] * N
	for i in range(N) :
		row = [int(x) for x in input().split(' ')]
		ARR[i] = row

	solution(N, ARR)


# arr = [
# 	[2,4,16,8],
# 	[8,4,0,0],
# 	[16,8,2,0],
# 	[2,8,2,0],
# ]

# print('UP--------')
# result = slide(4, arr, UP)
# for row in result :
# 	print(row)


# print('DOWN--------')
# result = slide(4, arr, DOWN)
# for row in result :
# 	print(row)


# print('LEFT--------')
# result = slide(4, arr, LEFT)
# for row in result :
# 	print(row)

# print('RIGHT--------')
# result = slide(4, arr, RIGHT)
# for row in result :
# 	print(row)


# print('original---------')
# for row in arr :
# 	print(row)