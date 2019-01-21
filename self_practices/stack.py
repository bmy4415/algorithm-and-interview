# python3 list 이용하여 쉽게 구현 가능

class Stack :
	def __init__(self) :
		self.items = []

	def isEmpty(self) :
		return len(self.items) == 0

	def pop(self) :
		return self.items.pop()

	def top(self) :
		return self.items[len(self.items) - 1]

	def push(self, item) :
		self.items.append(item)


	def printAllItems(self) :
		print('stack: ', self.items)


# test

stack = Stack()

stack.push(1)
stack.printAllItems() # [1]

stack.push(2)
stack.printAllItems() # [1, 2]

stack.push(3)
stack.printAllItems() # [1, 2, 3]

print(stack.pop()) # 3
print(stack.top()) # 2
stack.printAllItems() # [1, 2]

stack.push(4)
stack.printAllItems() # [1, 2, 4]