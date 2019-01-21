# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRQm6qfL0DFAUo 벽돌 깨기

DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def solution(problems) :
	for num, problem in enumerate(problems) :
		n, w, h, arr = problem

		cnt, new_arr, history = bfs(n, w, h, arr)
		# print('broken_cnt, arr, history: ', cnt, history)
		# for row in new_arr :
		# 	print(row)


		rest_count = 0
		for i in range(h) :
			for j in range(w) :
				if new_arr[i][j] != 0 :
					rest_count += 1

		print('#{} {}'.format(num+1, rest_count))
		# print('answer: ', rest_count)


def bfs(N, W, H, ARR) :
	queue = []
	tops = find_tops(ARR, W, H)
	for top in tops :
		x, y = top
		queue.append((ARR,x,y,0,1,[]))

	max_count = 0 # 최대 벽돌 깬 수
	max_arr = None # 최대 벽돌 깬 후 상태
	max_history = None # 최대 벽돌 깬 history
	while queue :
		arr, x, y, count, level, history = queue.pop(0)
		if level > N :
			break

		cnt, new_arr, history = kill(arr, count, x, y, W, H, history)
		if level == N and max_count < cnt :
			max_count = cnt
			max_arr = new_arr
			max_history = history

		tops = find_tops(new_arr, W, H)
		# N회 부수진 않았지만 모든 벽돌을 다 부수는 경우
		if not tops :
			max_count = cnt
			max_arr = new_arr
			max_history = history


		for top in tops :
			x, y = top
			queue.append((new_arr,x,y,cnt,level+1,history))

	return (max_count, max_arr, max_history)



def find_tops(arr, W, H) :
	result = []
	for j in range(W) :
		for i in range(H) :
			if arr[i][j] != 0 :
				result.append((i, j))
				break

	return result


# arr와 (x,y)를 받아서 벽돌을 부숨
# return (cnt, arr, history)
def kill(ARR, count, x, y, w, h, HISTORY) :
	arr = [row[:] for row in ARR] # deep copy
	history = HISTORY[:] # deep copy
	history.append((x, y)) # history 추가
	queue = []
	queue.append((x, y))

	while queue :
		curr_x, curr_y = queue.pop(0)
		if arr[curr_x][curr_y] != 0 :
			num = arr[curr_x][curr_y]
			arr[curr_x][curr_y] = 0
			count += 1

			for i in range(num) :
				for dir in DIRS :
					next_x = curr_x + i * dir[0]
					next_y = curr_y + i * dir[1]

					if inRange(next_x, next_y, w, h) and arr[next_x][next_y] != 0 :
						queue.append((next_x, next_y))

	# 빈칸 내리기
	for j in range(w) :
		for i in reversed(range(h)) :
			if arr[i][j] == 0 :
				found = -1
				for k in reversed(range(i)) :
					if arr[k][j] != 0 :
						found = k
						break

				if found != -1 :
					arr[i][j] = arr[found][j]
					arr[found][j] = 0

				else :
					break



	return (count, arr, history)


# 해당 좌표가 범위에 있는지 확인
def inRange(x, y, w, h) :
	if x>=0 and x<h and y>=0 and y<w :
		return True
	else :
		return False



if __name__ == '__main__' :
	T = int(input())
	PROBLEMS = [0] * T
	for i in range(T) :
		N, W, H = [int(x) for x in input().split(' ')[:3]]
		ARR = [0] * H
		for j in range(H) :
			row = [int(x) for x in input().split(' ')[:W]]
			ARR[j] = row

		PROBLEMS[i] = (N, W, H, ARR)

	solution(PROBLEMS)



# ARR = [
# 	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
# 	[1, 0, 0, 0, 1, 0, 0, 0, 0, 0,],
# 	[1, 0, 3, 0, 1, 1, 0, 0, 0, 1,],
# 	[1, 1, 1, 0, 1, 2, 0, 0, 0, 9,],
# 	[1, 1, 4, 0, 1, 1, 0, 0, 1, 1,],
# 	[1, 1, 4, 1, 1, 1, 2, 1, 1, 1,],
# 	[1, 1, 5, 1, 1, 1, 1, 2, 1, 1,],
# 	[1, 1, 6, 1, 1, 1, 1, 1, 2, 1,],
# 	[1, 1, 1, 1, 1, 1, 1, 1, 1, 5,],
# 	[1, 1, 7, 1, 1, 1, 1, 1, 1, 1,],
# ]
# w, h = 10, 10


# print('before kill--------------')
# for row in ARR :
# 	print(row)

# # cnt, arr, history = kill(ARR, 1, 2, 10, 10, [])
# # print('after kill: ', cnt, history)
# # for row in arr :
# # 	print(row)

# cnt, arr, history = kill(ARR, 2, 2, 10, 10, [])
# print('after kill: ', cnt, history)
# for row in arr :
# 	print(row)

# cnt, arr, history = kill(arr, 8, 6, 10, 10, history)
# print('after kill: ', cnt, history)
# for row in arr :
# 	print(row)