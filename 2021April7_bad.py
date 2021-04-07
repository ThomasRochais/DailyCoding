def neighbors(M, current):
    i = current[0]
    j = current[1]
    neighbors = set()
    if M[i][j] != 0:
        raise Exception("Currently inside wall")
    if i-1 >= 0 and M[i-1][j] == 0:
        neighbors.add((i-1,j))
    if i + 1 < len(M) and M[i+1][j] == 0:
        neighbors.add((i+1,j))
    if j-1 >= 0 and M[i][j-1] == 0:
        neighbors.add((i,j-1))
    if j+1 < len(M[0]) and M[i][j+1] == 0:
        neighbors.add((i,j+1))
    return neighbors

def step_forward(M, current, walked_through):
    next_steps = set()
    for n in neighbors(M, current):
        if n not in walked_through:
            next_steps.add(n)
    return next_steps

def paths(M, start, end):
    if M[start[0]][start[1]] != 0 or M[end[0]][end[1]] != 0:
        raise Exception("Starts or end inside a wall")
    else:
        walked_through = set()
        path = []
        current = start
        path.append(current)
        walked_through.add(current)
        while current != end:
            print(current)
            next_steps = step_forward(M, current, walked_through)
            current = next_steps.pop()
            walked_through.add(current)
            path.append(current)
    print(path)
    return path

start = (0, 0)
end = (-1, -1)
M = [[0, 0, 1],
     [0, 0, 1],
     [1, 0, 0]]
#print(step_forward(M, (1,1), set()))
print(paths(M, start, end))