# Return all partial sums up to index i
def partial_sums(list):
    psums = [list[0]]
    for i in range(1, len(list)):
        psums.append(psums[-1] + list[i])
    return psums

def sum(i, j, psums):
    if i > 0:
        return psums[j-1] - psums[i-1]
    else:
        return psums[j-1]

L = [1,2,3,4,5]
psums = partial_sums(L)
print(psums)
print(sum(1, 3, psums))
print(sum(0, 3, psums))
print(sum(2, 4, psums))
