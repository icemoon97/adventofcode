data = [line.rstrip("\n") for line in open("input04.txt")]

nums = [int(x) for x in data.pop(0).split(",")]

while "" in data:
	data.remove("")

class Board:
	def __init__(self, lines):
		self.size = 5
		self.board = lines

	def is_done(self, nums):
		for i in range(self.size):
			if all([(self.board[i][j] in nums) for j in range(self.size)]):
				return True
			if all([(self.board[j][i] in nums) for j in range(self.size)]):
				return True

		return False

	def sum_unmarked(self, nums):
		s = 0
		for i in range(self.size):
			for j in range(self.size):
				if self.board[i][j] not in nums:
					s += self.board[i][j]
		return s

boards = []

for i in range(0, len(data), 5):
	section = data[i:i + 5]

	b = []
	for line in section:
		line = [int(x) for x in line.split()]
		b.append(line)

	board = Board(b)
	boards.append(board)

def find_nth_winner(nums, boards, nth):
	called = set()
	winners = 0
	done = [False for _ in range(len(boards))]

	for n in nums:
		called.add(n)

		for i, b in enumerate(boards):
			if not done[i] and b.is_done(called):
				done[i] = True
				winners += 1

				if winners == nth:
					return n * b.sum_unmarked(called)

print("Part 1:", find_nth_winner(nums, boards, 1))
print("Part 2:", find_nth_winner(nums, boards, len(boards)))
