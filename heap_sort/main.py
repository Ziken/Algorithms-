class HeapSort:
	@staticmethod
	def _heapify(L: list, heap_size: int, parent_index: int):
		is_parent_largest = False
		while not is_parent_largest:
			left_child_index = 2 * parent_index + 1
			right_child_index = 2 * parent_index + 2
			if left_child_index < heap_size and L[left_child_index] > L[parent_index]:
				largest = left_child_index
			else:
				largest = parent_index

			if right_child_index < heap_size and L[right_child_index] > L[largest]:
				largest = right_child_index

			if largest == parent_index:
				is_parent_largest = True
			else:
				L[parent_index], L[largest] = L[largest], L[parent_index]  # swap
				parent_index = largest

	@staticmethod
	def _build_heap(L: list, heap_size: int):
		parent_index = len(L) // 2 - 1
		while parent_index >= 0:
			HeapSort._heapify(L, heap_size, parent_index)
			parent_index = parent_index - 1

	@staticmethod
	def sort(L: list):
		heap_size = len(L)
		HeapSort._build_heap(L, heap_size)

		for i in range(heap_size - 1):
			L[heap_size - 1], L[0] = L[0], L[heap_size - 1]  # swap
			heap_size = heap_size - 1
			HeapSort._heapify(L, heap_size, 0)


class HeapSortRange:
	@staticmethod
	def _heapify(L: list, heap_size: int, parent_index: int, left_limit: int, right_limit: int):
		left_child_index = 2 * parent_index + 1 - left_limit
		right_child_index = 2 * parent_index + 2 - left_limit

		if left_limit <= left_child_index <= heap_size and L[left_child_index] > L[parent_index]:
			largest = left_child_index
		else:
			largest = parent_index

		if right_child_index <= right_limit and right_child_index <= heap_size and L[right_child_index] > L[largest]:
			largest = right_child_index

		if largest != parent_index:
			L[parent_index], L[largest] = L[largest], L[parent_index]  # swap
			HeapSortRange._heapify(L, heap_size, largest, left_limit, right_limit)

	@staticmethod
	def _build_heap(L: list, heap_size: int, left_limit: int, right_limit: int):
		i = right_limit
		while i >= left_limit:
			HeapSortRange._heapify(L, heap_size, i, left_limit, right_limit)
			i = i - 1

	@staticmethod
	def sort(L: list, left_limit: int, right_limit: int):
		heap_size = right_limit
		HeapSortRange._build_heap(L, heap_size, left_limit, right_limit)
		i = right_limit
		while i >= left_limit + 1:
			L[heap_size], L[left_limit] = L[left_limit], L[heap_size]
			heap_size = heap_size - 1
			HeapSortRange._heapify(L, heap_size, left_limit, left_limit, right_limit)
			i = i - 1


if __name__ == "__main__":
	import random

	some_list = [random.randrange(-1000, 1000) for i in range(100)]
	c1_list = list(some_list)
	c2_list = list(some_list)
	c3_list = list(some_list)
	c4_list = list(some_list)

	HeapSort.sort(c1_list)
	assert c1_list == sorted(c2_list)

	HeapSortRange.sort(c3_list, 0, 50)
	c4_list[0:51] = sorted(c4_list[0:51])
	assert c3_list == c4_list
