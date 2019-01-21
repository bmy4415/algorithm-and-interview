# https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRFInKex8DFAUo 원자 소멸 시뮬레이션


def solution(problems) :
	for i, problem in enumerate(problems) :
		N, atoms = problem
		result = simulate(atoms)
		print('#{} {}'.format(i+1, result))


def simulate(atoms) :
	# 좌표를 2배씩 늘려줌 -> 0.5sec 단위로 수행하기위해
	for atom in atoms :
		x, y, dir, e = atom
		atom[0] = 2*x
		atom[1] = 2*y


	time = 0
	total_energy = 0
	while time <= 4000 and atoms :
		time += 1
		dic = {} # key: (x,y) value: array of e
		for atom in atoms :
			x, y, dir, e = atom
			dx, dy = get_dir(dir)
			next_x = x + dx
			next_y = y + dy
			atom[0] = next_x
			atom[1] = next_y

			if (next_x, next_y) in dic :
				dic[(next_x, next_y)].append(e)
			else :
				dic[(next_x, next_y)] = [e]

		for point in dic :
			curr = dic[point] # array of e
			if len(curr) >= 2 :
				total_energy += sum(curr)
				x, y = point
				atoms = remove_dead(atoms, x, y)


		# print('time, total, atoms:', time/2, total_energy)
		# for atom in atoms :
		# 	x, y, dir, e = atom
		# 	print(x/2, y/2, dir, e)

	# print('total_energy, t:', total_energy, time)
	return total_energy

def remove_dead(atoms, x, y) :
	result = []
	for atom in atoms :
		curr_x, curr_y, dir, e = atom
		if curr_x == x and curr_y == y :
			continue
		else :
			result.append([curr_x, curr_y, dir, e])

	return result


def get_dir(dir) :
	if dir == 0 :
		return (0, 1)
	elif dir == 1 :
		return (0, -1)
	elif dir == 2 :
		return (-1, 0)
	elif dir == 3 :
		return (1, 0)




if __name__ == '__main__' :
	T = int(input())
	problems = [0] * T
	for i in range(T) :
		N = int(input())
		atoms = [0] * N
		for j in range(N) :
			x, y, dir, K = [int(x) for x in input().split(' ')[:4]]

			atoms[j] = [x, y, dir, K]
		problems[i] = (N, atoms)

	solution(problems)



# atoms = [
# 	[-6,5,3,1],
# 	[-3,5,2,1],
# 	[-5,2,1,1],
# 	[3,5,3,1],
# 	[5,7,1,1],
# 	[6,7,3,1],
# 	[7,5,2,1],
# 	[5,3,0,1],
# 	[-4,-4,1,1],
# 	[-4,-6,0,1],
# 	[5,-3,2,1],
# 	[4,-6,0,1],
# 	[6,-4,1,1],
# 	[9,-7,2,1],
# ]
# simulate(atoms)