with open("./Day 3/Input/problem_a.txt", "r") as f:
    width = 12
    sums = [0] * width
    no_of_lines = 0
    for line in f:
        no_of_lines += 1
        for i in range(len(line) - 1):
            sums[i] += int(line[i])

for i in range(len(sums)):
    if sums[i] >= no_of_lines // 2:
        sums[i] = 1
    else:
        sums[i] = 0

string_sums = [str(i) for i in sums]
binary_string = "".join(string_sums)

gamma = int(binary_string, 2)
epsilon = 2 ** (width) - 1 - gamma
print(gamma * epsilon)


class Tree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __str__(self):
        return str(self.data)


# Create a binary tree of length 12
base = Tree(None)


def binary_tree(levels, tree):
    if levels == 0:
        return Tree(0)
    tree.left = binary_tree(levels - 1, tree)
    tree.right = binary_tree(levels - 1, tree)


tree = binary_tree(12, Tree(None))
print(tree)


with open("./Day 3/Input/problem_b.txt") as f:
    for line in f:
        for i in range(len(line) - 1):
            pass
