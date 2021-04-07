def num_paths(M, i, j):
    if M[i][j] != 0:
        raise Exception("Inside a wall")
    if i == 0 and j == 0:
        return 1
    elif i == 0:
        if 1 in M[0][0:j]:
            return 0
        else:
            return 1
    elif j == 0:
        if 1 in [col[0] for col in M][0:i]:
            return 0
        else:
            return 1
    if M[i-1][j] == 0 and M[i][j-1] == 0:
        return num_paths(M, i-1, j) + num_paths(M, i, j-1)
    elif M[i-1][j] == 0:
        return num_paths(M, i-1, j)
    elif M[i][j-1] == 0:
        return num_paths(M, i, j-1)
    else:
        return 0

def count_paths(M):
    print(num_paths(M, len(M)-1, len(M[0])-1))


M = [[0, 0, 1],
     [0, 0, 1],
     [1, 0, 0]]
count_paths(M)
M = [[0, 0, 0, 0],
     [0, 1, 1, 0],
     [1, 0, 0, 0],
     [1, 0, 1, 0],
     [0, 0, 1, 0],
     [1, 0, 0, 0]]
count_paths(M)
M = [[0, 0, 0],
     [0, 1, 0],
     [0, 0, 0]]
count_paths(M)