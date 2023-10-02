data = [line.rstrip("\n") for line in open("input16.txt")][0]

class BITS:
	def __init__(self, packet, is_hex=False):
		if is_hex:
			packet = self.hex2bin(packet)
		self.packet = packet
		self.i = 0

		self.version = self.get(3)
		self.tid = self.get(3)

		self.children = []

		if self.tid == 4:
			literal = ""
			while self.getBits(1) != "0":
				literal += self.getBits(4)

			literal += self.getBits(4)
			self.val = int(literal, 2)
		else:
			length_tid = self.get(1)
			if length_tid == 0:
				length = self.get(15)
				end = self.i + length
				while self.i < end:
					child = BITS(self.packet[self.i:])
					self.children.append(child)
					self.i += child.i
			else:
				sub_count = self.get(11)
				sub = 0
				while sub < sub_count:
					child = BITS(self.packet[self.i:])
					self.children.append(child)
					self.i += child.i
					sub += 1

			vals = [child.val for child in self.children]
			if self.tid == 0:
				self.val = sum(vals)
			elif self.tid == 1:
				self.val = 1
				for v in vals:
					self.val *= v
			elif self.tid == 2:
				self.val = min(vals)
			elif self.tid == 3:
				self.val = max(vals)
			elif self.tid == 5:
				self.val = int(vals[0] > vals[1])
			elif self.tid == 6:
				self.val = int(vals[0] < vals[1])
			elif self.tid == 7:
				self.val = int(vals[0] == vals[1])


	def hex2bin(self, word):
		h = bin(int(word, 16))[2:]
		h = h.zfill(len(word) * 4)
		return h

	def get(self, n):
		num = int(self.packet[self.i:self.i+n], 2)
		self.i += n
		return num

	def getBits(self, n):
		bits = self.packet[self.i:self.i+n]
		self.i += n
		return bits

b = BITS(data, is_hex=True)

def part1(b):
	if len(b.children) == 0:
		return b.version

	n = 0
	for child in b.children:
		n += part1(child)
	return n + b.version

print("Part 1:", part1(b))
print("Part 2:", b.val)
