def change_color(M, cell, new_color):
    init_color = M[cell[0]][cell[1]]
    for i in range(cell[0]-1, cell[0]+2):
        if i >= 0 and i < len(M):
            for j in range(cell[1]-1, cell[1]+2):
                if j >= 0 and j < len(M[0]):
                    if M[i][j] == init_color:
                        M[i][j] = new_color
    return M

M = [["B", "B", "W"], ["W", "W", "W"], ["W", "W", "W"], ["B", "B", "B"]]
print(M)
print(change_color(M, (1,1), "G"))
M = [["B", "B", "W"], ["W", "W", "W"], ["W", "W", "W"], ["B", "B", "B"]]
print(change_color(M, (2,2), "G"))
