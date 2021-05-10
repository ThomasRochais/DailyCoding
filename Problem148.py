# Given n bits, generate gray code: 
# an array of bit patterns from 0 to 2^(n-1) 
# such that successive patterns differ by one bit
def binList(g):
    for i in range(len(g)):
        print(format(g[i], "03b"), end=" ")
    print()

def pad(list, val):
    padded_list = []
    for i in range(len(list)):
        padded_list.append(val+list[i])
    return padded_list

def grey_code(n):
    if n == 1:
        return ["0", "1"]
    prev_grey = grey_code(n-1)
    return pad(prev_grey, "0") + pad(prev_grey, "1")[::-1]
    

print(grey_code(1))
print(grey_code(2))
print(grey_code(3))
print(grey_code(4))