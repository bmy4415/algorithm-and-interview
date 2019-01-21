# https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRDL1aeugDFAUo 무선 충전

STOP = 0
UP = 1
RIGHT = 2
DOWN = 3
LEFT = 4

# map: key: (x,y) value: array of (bc, e)
# a: (ax,ay)
# b: (bx,by)
# return max charge amount
def get_max(map, a, b) :
	if a not in map and b not in map :
		return 0

	if a in map and b not in map :
		arr = map[a]
		max = 0
		for item in arr :
			num, p = item
			if p > max :
				max = p

		return max

	if a not in map and b in map :
		arr = map[b]
		max = 0
		for item in arr :
			num, p = item
			if p > max :
				max = p

		return max


	# a,b 둘 다 충전 가능한 bc가 있는 경우
	max = 0
	arr1 = map[a]
	arr2 = map[b]
	for i in range(len(arr1)) :
		for j in range(len(arr2)) :
			bc1, e1 = arr1[i]
			bc2, e2 = arr2[j]
			sum = 0
			if bc1 == bc2 :
				sum = e1
			else :
				sum = e1+e2

			if sum > max :
				max = sum

	return max


# 시작점과 이동경로를 받아서 좌표의 array를 return
def get_route(x, y, arr) :
	result = [(x, y)]
	curr_x = x
	curr_y = y
	for dir in arr :
		if dir == STOP :
			curr_x, curr_y = curr_x, curr_y
			result.append((curr_x, curr_y))
		elif dir == UP :
			curr_x, curr_y = curr_x, curr_y-1
			result.append((curr_x, curr_y))
		elif dir == RIGHT :
			curr_x, curr_y = curr_x+1, curr_y
			result.append((curr_x, curr_y))
		elif dir == DOWN :
			curr_x, curr_y = curr_x, curr_y+1
			result.append((curr_x, curr_y))
		elif dir == LEFT :
			curr_x, curr_y = curr_x-1, curr_y
			result.append((curr_x, curr_y))

	return result

# key: (x,y) value: array of (bc#, p)
def get_point_bc_map(BCs) :
	dic = {}
	for i, bc in enumerate(BCs) :
		num = i+1
		x, y, c, p = bc

		for dx in range(-c, c+1) :
			temp = c - abs(dx)
			for dy in range(-temp, temp+1) :
				# 지도 벗어나는것은 버림
				if x+dx > 10 or x+dx < 1 or y+dy > 10 or y+dy < 1 :
					continue

				point = (x+dx, y+dy)
				if point in dic :
					dic[point].append((num, p))
				else :
					dic[point] = [(num, p)]

	return dic


# M: 총 이동시간
# num_BC: bc의 갯수
# A: A의 이동경로 list
# B: B의 이동경로 list
# BCs: bc의 정보들
# return charge amount
def solve(M, A, B, BCs) :
	route_a = get_route(1,1,A)
	route_b = get_route(10,10,B)
	point_bc_map = get_point_bc_map(BCs) # key: (x,y) value: array of (bc#, e)


	# print('map')
	# points = list(point_bc_map.keys())
	# points.sort()
	# for point in points :
	# 	print(point, ':', point_bc_map[point])

	total = 0
	for i in range(M+1) :
		a = route_a[i]
		b = route_b[i]

		charge = get_max(point_bc_map, a, b)

		# print('a, b, charge:', a, b, charge)

		total += charge

	return total


def solution(problems) :
	for i, problem in enumerate(problems) :
		M, A, B, BCs = problem
		result = solve(M, A, B, BCs)
		print('#{} {}'.format(i+1, result))


if __name__ == '__main__' :
	T = int(input())
	problems = [0] * T
	for i in range(T) :
		M, num_BC = [int(x) for x in input().split(' ')[:2]]
		A = [int(x) for x in input().split(' ')[:M]]
		B = [int(x) for x in input().split(' ')[:M]]
		BCs = [0] * num_BC
		for j in range(num_BC) :
			x, y, c, p = [int(x) for x in input().split(' ')[:4]]
			BCs[j] = (x,y,c,p)

		problems[i] = (M, A, B, BCs)

	solution(problems)


## test get_point_bc_map
# numb_BC = 3
# BCs = [
# 	(4, 4, 1, 100),
# 	(7,10,3,40),
# 	(6,3,2,70),
# ]

# result = get_point_bc_map(BCs)
# # points = list(result.keys())
# # points.sort()
# # for point in points :
# # 	print(point, ':', result[point])

## test get_max
# result1 = get_max(result[(4,5)], result[(5,4)])
# print(result1)


## test get_route
# A = [2, 2, 3, 2, 2, 2, 2, 3, 3, 4, 4, 3, 2, 2, 3, 3, 3, 2, 2, 3,]
# B = [4, 4, 1, 4, 4, 1, 4, 4, 1, 1, 1, 4, 1, 4, 3, 3, 3, 3, 3, 3,]
# result_a = get_route(1,1,A)
# result_b = get_route(10,10,B)
# print('result a')
# for item in result_a :
# 	print(item)

# print('result_b')
# for item in result_b :
# 	print(item)