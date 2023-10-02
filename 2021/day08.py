data = [line.rstrip("\n") for line in open("input08.txt")]


easy_seg = {
	2 : 1,
	3 : 7,
	4 : 4,
	7 : 8
}


seg2num = {
	"abcefg" : 0,
	"cf" : 1,
	"acdeg" : 2,
	"acdfg" : 3,
	"bcdf" : 4,
	"abdfg" : 5,
	"abdefg" : 6,
	"acf" : 7,
	"abcdefg" : 8,
	"abcdfg" : 9
}

"""
num2seg = {
	0 : set(list("abcefg")),
	1 : set(list("cf")),
	2 : set(list("acdeg")),
	3 : set(list("acdfg")),
	4 : set(list("bcdf")),
	5 : set(list("abdfg")),
	6 : set(list("abdefg")),
	7 : set(list("acf")),
	8 : set(list("abcdefg")),
	9 : set(list("abcdfg"))
}
"""

result = 0

for line in data:
	line = line.split()
	signals = line[:10]
	output = line[11:]
	print(signals, output)

	mapping = {}
	r_mapping = {}

	sig_len = {}
	num2seg = {}

	for x in signals:
		l = len(x)
		if l in sig_len:
			sig_len[l].append(x)
		else:
			sig_len[l] = [x]

		if l in easy_seg:
			num2seg[easy_seg[l]] = x

	print(sig_len)

	for char in num2seg[7]:
		if char not in num2seg[1]:
			mapping[char] = "a"
			r_mapping["a"] = char

	for signal in sig_len[5]:
		if len(set(signal) & set(num2seg[1])) == 2:
			num2seg[3] = signal
			char = (set(num2seg[4]) & set(signal) - set(num2seg[1])).pop()
			mapping[char] = "d"
			r_mapping["d"] = char

	for char in num2seg[4]:
		if char not in num2seg[1] and char not in mapping:
			mapping[char] = "b"
			r_mapping["b"] = char

	for signal in sig_len[5]:
		if signal == num2seg[3]:
			continue

		if r_mapping["b"] in signal:
			num2seg[5] = signal
			char = (set(num2seg[1]) & set(signal)).pop()
			mapping[char] = "f"
			r_mapping["f"] = char
		else:
			num2seg[2] = signal

	c = (set(num2seg[3]) - set(num2seg[5])).pop()
	mapping[c] = "c"
	r_mapping["c"] = c

	e = (set(num2seg[2]) - set(num2seg[3])).pop()
	mapping[e] = "e"
	r_mapping["e"] = e

	g = (set(num2seg[5]) - set(num2seg[4]) - set(r_mapping["a"])).pop()
	mapping[g] = "g"
	r_mapping["g"] = g

	print(mapping)
	print(r_mapping)

	final = ""
	for out in output:
		translated = [mapping[char] for char in out]
		translated.sort()
		translated = "".join(translated)
		final += str(seg2num[translated])
	final = int(final)

	print(final)
	result += final

	
print(result)
	
	
