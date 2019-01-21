# key: number
# use linear probing
class OpenAddressHashTable :
	def __init__(self) :
		self.arr = [('EMPTY', None)] * 2
		self.num_element = 0
	def insert(self, key, value) :
		if self.num_element == len(self.arr) :
			self._resize()

		index = self._hash(key)
		i = index
		while i < len(self.arr) :
			status = self.arr[i][0]
			if status == 'EMPTY' or status == 'DEL' :
				self.arr[i] = (key, value)
				self.num_element += 1
				return
			else :
				i += 1
				continue

		i = 0
		while i < index :
			status = self.arr[i][0]
			if status == 'EMPTY' or status == 'DEL' :
				self.arr[i] = (key, value)
				self.num_element += 1
				return
			else :
				i += 1
				continue

	def delete(self, key) :
		index = self._hash(key)
		i = index
		while i < len(self.arr) :
			status = self.arr[i][0]
			if status == key :
				self.arr[i] = ('DEL', None)
				self.num_element -= 1
				return
			else :
				i += 1

		i = 0
		while i < index :
			status = self.arr[i][0]
			if status == key :
				self.arr[i] = ('DEL', None)
				self.num_element -= 1
				return
			else :
				i += 1

	def search(self, key) :
		index = self._hash(key)
		i = index
		while i < len(self.arr) :
			status = self.arr[i][0]
			if status == key :
				return self.arr[i][1]
			else :
				i += 1

		i = 0
		while i < index :
			status = self.arr[i][0]
			if status == key :
				return self.arr[i][1]
			else :
				i += 1

		return None

	def print_all(self) :
		print('# of elements:', self.num_element)
		for i, node in enumerate(self.arr) :
			print(i, node)

	def _resize(self) :
		new_arr = [('EMPTY', None)] * len(self.arr) * 2 # 2배 확장
		for i, node in enumerate(self.arr) :
			new_arr[i] = node

		self.arr = new_arr

	def _hash(self, key) :
		return key % len(self.arr)


hash_table = OpenAddressHashTable()
hash_table.print_all()

hash_table.insert(1, 'jaewan')
print('insert 1, jaewan')
hash_table.print_all()
hash_table.insert(5, 'shinhwi')
print('insert 5, shinhwi')
hash_table.print_all()
hash_table.insert(33, 'genguk')
print('insert 33, genguk')
hash_table.print_all()
print('search 5:', hash_table.search(5))
hash_table.delete(1)
print('delete 1')
hash_table.print_all()