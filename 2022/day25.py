input_file = "input25.txt"
# input_file = "input25test.txt"

with open(input_file, "r") as file:
	data = file.read().split("\n")

def snafu2dec(s):
    num = []
    for char in s:
        match char:
            case "-":
                num.append(-1)
            case "=":
                num.append(-2)
            case _:
                num.append(int(char))

    return sum([n * 5**i for i,n in enumerate(num[::-1])])

def dec2snafu(n):
    s = []
    while n > 0:
        s.append(n % 5)
        n //= 5

    s.append(0)
    for i in range(len(s) - 1):
        if s[i] >= 3:
            s[i] -= 5
            s[i+1] += 1

    for i, digit in enumerate(s):
        if digit == -1:
            s[i] = "-"
        elif digit == -2:
            s[i] = "="
        else:
            s[i] = str(digit)

    s.reverse()
    return "".join(s).lstrip("0")

total = 0

for line in data:
    val = snafu2dec(line)
    assert dec2snafu(val) == line
    total += val

print("Part 1:", dec2snafu(total))



# total = 0

# def snafu(n):
#     s = ""
#     while n > 0:
#         s = str(n % 5) + s
#         n //= 5
    
#     s = "0" + s
#     s = [int(x) for x in list(s)]
#     for _ in range(len(s)):
#         for i, char in enumerate(s):
#             if char >= 3:
#                 s[i] -= 5
#                 s[i-1] += 1

#     final = ""
#     for n in s:
#         if n >= 0:
#             final += str(n)
#         elif n == -1:
#             final += "-"
#         else:
#             final += "="

#     if final[0] == "0":
#         final = final[1:]

#     return final

# for line in data:
#     num = []
#     for char in line:
#         if char.isdigit():
#             num.append(int(char))
#         elif char == "-":
#             num.append(-1)
#         elif char == "=":
#             num.append(-2)
#         else:
#             print("bad")

#     val = 0
#     for i,n in enumerate(num[::-1]):
#         val += n * 5**i

#     print(line, val, snafu(val))
#     total += val

# print(total)
# print(snafu(total))
