data = [line.rstrip("\n") for line in open("input04.txt")]

req_fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
req_fields2 = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"])

valid = 0

i = 0

def is_valid(passport):
	fields = passport.split()

	for field in fields:
		key = field.split(":")[0]
		value = field.split(":")[1]

		if set(keys) != req_fields and set(keys) != req_fields2:
			return False

		if key == "byr":
			if len(value) != 4:
				return False
			if int(value) < 1920 or int(value) > 2002:
				return False
		if key == "iyr":
			if len(value) != 4:
				return False
			if int(value) < 2010 or int(value) > 2020:
				return False
		if key == "eyr":
			if len(value) != 4:
				return False
			if int(value) < 2020 or int(value) > 2030:
				return False
		if key == "hgt":
			num = int(value[:-2])
			if value.endswith("cm"):
				if num < 150 or num > 193:
					return False
			elif value.endswith("in"):
				if (num < 59 or num > 76):
					return False
			else:
				return False
		if key == "hcl":
			if value[0] != "#" or len(value) != 7:
				return False
			for letter in value[1:]:
				if letter not in "0123456789abcdef":
					return False
		if key == "ecl":
			if value not in ["amb", "blu", "brn", "gry" ,"grn" ,"hzl" ,"oth"]:
				return False
		if key == "pid":
			if len(value) != 9:
				return False
			if not value.isnumeric():
				return False

	return True


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


	if is_valid(passport):
		valid += 1

	i += 1

print(valid)