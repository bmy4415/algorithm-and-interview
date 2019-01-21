# python3 list를 통해서 쉽게 구현가능


class Queue :
	def __init__(self) :
		self.items = []

	def isEmpty(self) :
		return len(self.items) == 0

	def enqueue(self, item) :
		self.items.insert(0, item)

	def dequeue(self) :
		return self.items.pop()

	def printAllItems(self) :
		print('queue: ', self.items)

# test
queue = Queue()

print(queue.isEmpty()) 	# True

queue.enqueue(1)
queue.printAllItems()	# [1]

queue.enqueue(2)
queue.printAllItems()	# [2, 1]

print(queue.dequeue())	# 1
queue.printAllItems()	# [2]

queue.enqueue(3)
queue.printAllItems()	# [3, 2]

queue.enqueue(4)
queue.printAllItems()	# [4, 3, 2]

print(queue.dequeue())	# 2
queue.printAllItems()	# [4, 3]