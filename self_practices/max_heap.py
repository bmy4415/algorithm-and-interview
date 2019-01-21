class MaxHeap :
	def __init__(self) :
		self.count = 0 # # of element
		self.arr = [] # implement heap by using array

	def print_all(self) :
		level = 0
		while True :
			start = pow(2, level) - 1
			if start >= self.count :
				break
			end = min(start*2, self.count-1)
			for i in range(start, end+1) :
				print(self.arr[i], end=' ')

			print()
			level += 1


	def insert(self, value) :
		if self.count == 0 :
			self.count = 1
			self.arr.append(value)
			return

		self.arr.append(value)
		self.count += 1

		index = self.count - 1
		while index > 0 :
			parent_index = (index-1) // 2
			# print('parent_index:', parent_index)
			# print('parent, child:', self.arr[parent_index], self.arr[index])
			if self.arr[parent_index] < self.arr[index] :
				# swap
				temp = self.arr[parent_index]
				self.arr[parent_index] = self.arr[index]
				self.arr[index] = temp
				index = parent_index
				# print('after swap:', self.arr)

			else :
				break

	def delete(self) :
		if self.count == 0 :
			return

		# 가장 마지막 element를 root로 올림
		self.arr[0] = self.arr[self.count-1]
		self.arr.pop()
		self.count -= 1

		# root에서 부터 밑으로 내려감
		index = 0
		while True :
			left_child_index = 2*index + 1
			right_child_index = 2*index + 2

			if left_child_index >= self.count :
				return


			# left만 확인 가능
			if right_child_index >= self.count :
				if self.arr[left_child_index] > self.arr[index] :
					# swap
					temp = self.arr[left_child_index]
					self.arr[left_child_index] = self.arr[index]
					self.arr[index] = temp

				return

			# right도 확인 가능
			else :
				# 왼쪽이 크므로 왼쪽과 비교
				if self.arr[left_child_index] > self.arr[right_child_index] :
					if self.arr[left_child_index] > self.arr[index] :
						# swap
						temp = self.arr[left_child_index]
						self.arr[left_child_index] = self.arr[index]
						self.arr[index] = temp
						index = left_child_index

					else :
						return

				# 오른쪽이 크므로 오른쪽과 비교
				else :
					if self.arr[right_child_index] > self.arr[index] :
						# swap
						temp = self.arr[right_child_index]
						self.arr[right_child_index] = self.arr[index]
						self.arr[index] = temp
						index = right_child_index

					else :
						return



mh = MaxHeap()
mh.insert(3)
mh.insert(5)
mh.insert(1)
print('after insert 3, 5, 1')
mh.print_all()
mh.insert(77)
mh.insert(-1)
print('after insert 77, -1')
mh.print_all()
mh.delete()
print('after delete top')
mh.print_all()
mh.insert(7)
# print('afetr insert 7')
# mh.print_all()
mh.insert(8)
# print('after insert 8')
# mh.print_all()
mh.insert(0)
# print('after insert 0')
# mh.print_all()
mh.insert(9)
print('after insert 7, 8, 0, 9')
mh.print_all()
mh.delete()
print('after delete top')
mh.print_all()