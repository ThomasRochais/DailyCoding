lst = [9, 12, 3, 5, 14, 10, 10]
x = 10
left = []
right = []
mid = []
for i in lst:
    if i < x:
        left.append(i)
    elif i > x:
        right.append(i)
    else:
        mid.append(i)
print(left + mid + right)