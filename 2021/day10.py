data = [line.rstrip("\n") for line in open("input10.txt")]

def valid(line):
	start = {
		"(",
		"{",
		"[",
		"<"
	}

	pairs = {
		")" : "(",
		"}" : "{",
		"]" : "[",
		">" : "<"
	}
	
	stack = []
	
	for i in range(len(line)):
		char = line[i]
		if char in start:
			stack.append(char)
		else:
			if not stack:
				return False
	
			expected = stack.pop()
			if expected != pairs[char]:
				#return pairs[char]
				return False

	print(stack)
	return stack;

table = {
	"(" : 3,
	"[": 57,
	"{" : 1197,
	"<" : 25137
}

table2 = {
	"(" : 1,
	"[" : 2,
	"{" : 3,
	"<" : 4
}

s = []
for line in data:
	score = 0
	v = valid(line)
	if v:
		while len(v) > 0:
			char = v.pop()
			score *= 5
			score += table2[char]

		s.append(score)

s.sort()
print(s[len(s) // 2])

	

