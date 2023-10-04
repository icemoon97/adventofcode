data = [line.rstrip("\n") for line in open("input04.txt")]

req_fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
req_fields2 = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"])

valid = 0

i = 0

while i < len(data):
	line = data[i]
	passport = ""
	while line != "" and i < len(data) - 1:
		passport += " " + line
		i += 1
		line = data[i]

	keys = []
	for field in passport.split():
		key = field.split(":")[0]
		keys.append(key)

	if set(keys) == req_fields or set(keys) == req_fields2:
		valid += 1

	i += 1

print(valid)