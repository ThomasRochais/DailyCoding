def rotate_cp(M):
    N = len(M)
    Mat = M.copy()
    for i in range(N):
        Mat[i] = [M[N-1-j][i] for j in range(N)]
    return Mat

def swap(i, j):
    return j, i

def rotate(M):
    N = len(M)
    for i in range(round(N/2)):
        for j in range(i,N-i-1):
            # Swap the 4 corners of a square:
            tmp = M[i][j]
            M[i][j] = M[N-1-j][i]
            M[N-1-j][i] = M[N-1-i][N-1-j]
            M[N-1-i][N-1-j] = M[j][N-1-i]
            M[j][N-1-i] = tmp

M = [[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
rotate(M)
print(M)
M = [[1, 2], 
 [3, 4]]
rotate(M)
print(M)