import math
def maj_el(list):
    N = len(list)
    half = math.floor(N/2)
    dic = {}
    for num in list:
        if num in dic:
            dic[num] = dic[num] + 1
        else:
            dic[num] = 1
        if dic[num] > half:
            return num
    return "No majority element"

print(maj_el([1, 2, 1, 1, 3, 4, 0]))
print(maj_el([1, 2, 1, 1, 3, 4, 1]))
print(maj_el([1, 2, 1, 1, 1, 1]))