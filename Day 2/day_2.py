with open("./Day 2/Input/problem_a.txt") as f:
    horizontal = depth = 0
    for line in f:
        keyword, value = line.split(" ")
        value = int(value)
        if keyword == "forward":
            horizontal += value
        elif keyword == "up":
            depth -= value
        elif keyword == "down":
            depth += value
        else:
            raise ValueError("Unexpected keyword.")

print(horizontal * depth)

with open("./Day 2/Input/problem_b.txt") as f:
    horizontal = depth = aim = 0
    for line in f:
        keyword, value = line.split(" ")
        value = int(value)
        if keyword == "forward":
            horizontal += value
            depth += aim * value
        elif keyword == "up":
            aim -= value
        elif keyword == "down":
            aim += value
        else:
            raise ValueError("Unexpected keyword.")

print(horizontal * depth)
