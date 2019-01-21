# circular linked list

class Node :
	def __init__(self, value) :
		self.value = value
		self.prev = None
		self.next = None

class LinkedList :
	def __init__(self) :
		self.count = 0 # number of elements
		self.head = None
		self.tail = None

	# tail에 value값을 갖는 node를 추가
	def insert(self, value) :
		if self.head is None :
			node = Node(value)
			node.next = node
			node.prev = node
			self.head = node
			self.tail = node
			self.count += 1

		else :
			node = Node(value)
			node.prev = self.tail
			node.next = self.head
			self.tail.next = node
			self.head.prev = node
			self.tail = node
			self.count += 1


	# 처음 발견되는 value node를 제거
	def delete(self, value) :
		node = self.search(value)
		if node :
			node = node[1]
			prev = node.prev
			prev.next = node.next
			next = node.next
			next.prev = prev
			node.prev = None
			node.next = None
			self.count -= 1

	# 처음 발견되는 node를 return
	def search(self, value) :
		curr = self.head
		for i in range(self.count) :
			if curr.value == value :
				return (i+1, curr)
			else :
				curr = curr.next

		return None

	def print_all(self) :
		curr = self.head
		print('total {} elements'.format(self.count))
		for i in range(self.count) :
			print(curr.value, end=' ')
			curr = curr.next
		print()

	def print_detail(self) :
		curr = self.head
		print('detail print prev, curr, next')
		for i in range(self.count) :
			print(curr.prev.value, curr.value, curr.next.value)
			curr = curr.next



## test
ll = LinkedList()
ll.insert(3)
ll.insert(5)
ll.insert(7)
ll.insert(44)
ll.print_detail()
result = ll.search(7)
print('get 7', end=' => ')
if result :
	print('{}th element'.format(result[0]))
else :
	print('no such element')

ll.delete(7)
print('after delete 7')
ll.print_all()
ll.print_detail()