# https://www.acmicpc.net/problem/15685 드래곤 커브

DIRS = [
	(1,0),
	(0,-1),
	(-1,0),
	(0,1)
]

def solution(N, infos) :
	arr = [[0] * 101 for _ in range(101)]
	for info in infos :
		x, y, d, g = info
		curve = get_curve(x, y, d, g)

		# draw curve
		for point in curve :
			x, y = point
			if x>=0 and x<=100 and y>=0 and y<=100 :
				arr[x][y] = 1

	count = 0
	for i in range(100) :
		for j in range(100) :
			if arr[i][j]==1 and arr[i+1][j]==1 and arr[i][j+1]==1 and arr[i+1][j+1]==1 :
				count += 1

	print(count)


def get_curve(x, y, d, g) :
	dx, dy = d
	if g == 0 :
		return [(x,y), (x+dx, y+dy)]

	prev = get_curve(x,y,d,g-1)
	return prev[:len(prev)-1] + rotate90(prev)

def rotate90(curve) :
	arr = curve[:len(curve)-1] # deep copy
	last_x, last_y = curve[len(curve)-1]
	result = [(last_x, last_y)]
	for point in reversed(arr) :
		x, y = point
		next_x = last_x + (last_y - y)
		next_y = last_y - (last_x - x)
		# print('x, y, nx, ny, lx, ly', x, y, next_x, next_y, last_x, last_y)
		result.append((next_x, next_y))

	return result


if __name__ == '__main__' :
	N = int(input())
	curves = [0] * N
	for i in range(N) :
		x, y, d, g = [int(x) for x in input().split(' ')]
		curves[i] = (x,y,DIRS[d],g)

	solution(N, curves)

# curve = [(0,0),(1,0),(1,-1)]
# print('original: ', curve)
# rot = rotate90(curve)
# print('rot: ', rot)

# result = get_curve(0,0,DIRS[0],3)
# print(result)