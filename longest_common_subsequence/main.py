import enum


class Direction(enum.Enum):
	UNDEFINED = 0
	LEFT = 1
	UP = 2
	EQUAL = 3
	FOUND = 4


class LCS:
	def __init__(self, seq1, seq2):
		self.seq1 = seq1
		self.seq2 = seq2

		self.lcs_list, self.directions = self._get_lcs_list()

	def _get_lcs_list(self) -> (list, dict):
		len_seq1 = len(self.seq1)
		len_seq2 = len(self.seq2)

		lcs_list = [[0] * (len_seq2 + 1) for i in range(len_seq1 + 1)]
		directions = [[Direction.UNDEFINED] * (len_seq2 + 1) for i in range(len_seq1 + 1)]

		for i in range(1, len_seq1 + 1):
			for j in range(1, len_seq2 + 1):
				if self.seq1[i - 1] == self.seq2[j - 1]:
					lcs_list[i][j] = lcs_list[i - 1][j - 1] + 1
					directions[i][j] = Direction.FOUND
				elif lcs_list[i][j - 1] > lcs_list[i - 1][j]:
					directions[i][j] = Direction.LEFT
					lcs_list[i][j] = lcs_list[i][j - 1]
				elif lcs_list[i - 1][j] > lcs_list[i][j - 1]:
					directions[i][j] = Direction.UP
					lcs_list[i][j] = lcs_list[i - 1][j]
				else:
					directions[i][j] = Direction.EQUAL
					lcs_list[i][j] = lcs_list[i][j - 1]

		return lcs_list, directions

	def find_longest_subsequence(self) -> str:
		longest_subsequence = ""
		i = len(self.seq1)
		j = len(self.seq2)
		while i > 0 and j > 0:
			if self.directions[i][j] == Direction.EQUAL:
				j -= 1
			elif self.directions[i][j] == Direction.LEFT:
				j -= 1
			elif self.directions[i][j] == Direction.UP:
				i -= 1
			elif self.directions[i][j] == Direction.FOUND:
				longest_subsequence = self.seq1[i - 1] + longest_subsequence
				j -= 1
				i -= 1

		return longest_subsequence

	def find_all_longest_seqs(self) -> set:
		n = len(self.seq1)
		m = len(self.seq2)
		found_seqs = set()
		if self.directions[n][m] != Direction.FOUND:
			self._helper_find_all_longest_seqs(found_seqs, n, m, "")
		else:
			self._helper_find_all_longest_seqs(found_seqs, n, m, self.seq1[-1])

		return found_seqs

	def _helper_find_all_longest_seqs(self, found_seqs: set, i: int, j: int, current_subsequence: str):
		coords = dict()
		self._get_nearest_found_signs(coords, i, j)
		if coords:
			for (x, y), sign in coords.items():
				self._helper_find_all_longest_seqs(found_seqs, x - 1, y - 1, sign + current_subsequence)
		else: # no more signs found, subsequence must be the longest one
			found_seqs.add(current_subsequence)

	def _get_nearest_found_signs(self, coords: dict, i: int, j: int):
		if self.directions[i][j] == Direction.EQUAL:
			self._get_nearest_found_signs(coords, i, j - 1)
			self._get_nearest_found_signs(coords, i - 1, j)
		elif self.directions[i][j] == Direction.LEFT:
			self._get_nearest_found_signs(coords, i, j - 1)
		elif self.directions[i][j] == Direction.UP:
			self._get_nearest_found_signs(coords, i - 1, j)
		elif self.directions[i][j] == Direction.FOUND:
			coords[(i, j)] = self.seq1[i - 1]


if __name__ == "__main__":
	try:
		with open("seq1.txt") as file1, open("seq2.txt") as file2:
			sq_1 = file1.read()
			sq_2 = file2.read()

		# sq_1 = "ADBECF"
		# sq_2 = "DEFABC"

		lcs = LCS(sq_1, sq_2)
		print(lcs.find_longest_subsequence())
		found_seqs = lcs.find_all_longest_seqs()
		print(found_seqs)
	except FileNotFoundError:
		print("Files 'seq1.txt' and 'seq2.txt' not found!")
