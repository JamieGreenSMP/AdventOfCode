with open("./Day 1/Input/problem_1.txt") as f:
    last = 0
    total = 0
    for line in f:
        if int(line) > last:
            total += 1
        last = int(line)

print(total - 1)


with open("./Day 1/Input/problem_1b.txt") as f:
    a = b = c = last = total = 0
    for line in f:
        current = int(line) + a + b
        if current > last:
            total += 1
        b = a
        a = int(line)
        last = current

print(total - 3)
