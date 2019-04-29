class Node:
	def __init__(self, value):
		self.value = value
		self.next = None
		self.prev = None
		self.len = 0

	def __str__(self):
		return "<Node {0}>".format(self.value)


class Sentinel:
	def __init__(self):
		self.value = 0
		self.prev = self

	@property
	def next(self):
		return self

	@next.setter
	def next(self, n):
		pass


class LinkedList:
	def __init__(self):
		self.root = None
		self.sentinel = Sentinel()
		self.size = 0

	def append(self, key):
		if not self.root:
			self.root = Node(key)
			self.root.prev = self.sentinel
			self.root.next = self.sentinel
			self.sentinel.prev = self.root
		else:
			new_node = Node(key)
			new_node.next = self.sentinel
			last_node = self.sentinel.prev
			last_node.next = new_node
			new_node.prev = last_node

			self.sentinel.prev = new_node

		self.size += 1

	def remove(self, key):
		found_node = self._search(key)
		return self._remove(found_node)

	def _remove(self, found_node) -> bool:
		if found_node is self.sentinel:
			return False

		if found_node == self.root:
			self.root = self.root.next
			self.root.prev = self.sentinel
		else:
			found_node.next.prev = found_node.prev
			found_node.prev.next = found_node.next
			del found_node

		self.size -= 1

		return True

	def search(self, key) -> bool:
		found_node = self._search(key)
		return found_node is not self.sentinel

	def _search(self, key) -> Node:
		n = self.root
		while n is not self.sentinel and n.value != key:
			n = n.next

		return n

	def print(self):
		n = self.root
		while n is not self.sentinel:
			print(" ({0} -> |{1}| -> {2}) ".format(n.prev.value, n.value, n.next.value), end="")
			n = n.next

		print()

	def scale(self, ll):
		last_node = self.sentinel.prev
		last_node.next = ll.root
		ll.root.prev = last_node
		self.sentinel.prev = ll.sentinel.prev
		ll.sentinel.prev.next = self.sentinel

		self.size += ll.size

	def get(self, index: int, default=None):
		node = self._get(index)
		if node:
			return node.value
		else:
			return default

	def _get(self, index: int):
		if index >= self.size:
			return None

		i = 0
		current_node = self.root
		while i < index:
			current_node = current_node.next
			i += 1

		return current_node

	def delete(self, index: int):
		node = self._get(index)
		return self._remove(node)

	def insert(self, index: int, key):
		if index >= self.size:
			self.append(key)
		else:
			found_node = self._get(index)
			new_node = Node(key)
			if found_node == self.root:
				new_node.prev = self.sentinel
				new_node.next = self.root
				self.root.prev = new_node
				self.root = new_node
			else:
				found_node.prev.next = new_node
				new_node.next = found_node
				new_node.prev = found_node.prev
				found_node.prev = new_node

		self.size += 1

	def __iter__(self):
		current_node = self.root
		while current_node is not self.sentinel:
			yield current_node.value
			current_node = current_node.next


if __name__ == "__main__":
	import random

	RANGE = 10000
	inserted_values = []
	ll = LinkedList()
	for i in range(1000):
		val = random.randrange(-RANGE, RANGE)
		inserted_values.append(val)
		ll.append(val)

	assert list(ll) == inserted_values

	ll.insert(1, 11)
	inserted_values.insert(1, 11)
	assert list(ll) == inserted_values

	key_to_remove = random.choice(inserted_values)
	inserted_values.remove(key_to_remove)
	ll.remove(key_to_remove)
	assert list(ll) == inserted_values

	key_to_search = random.choice(inserted_values)

	assert ll.search(key_to_search)
