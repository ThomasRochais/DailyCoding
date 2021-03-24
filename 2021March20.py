# Array of integers in which two elements appear exactly once
# and all other elements appear exactly twice
L = [2, 4, 6, 8, 10, 2, 6, 10] 
S = {} # Storing the frequency of appearance
n = len(L)
# for i in range(n):
#     if L[i] not in S:
#         S[L[i]] = 1
#     else:
#         del S[L[i]]
# print(S.keys())

# A better solution in constant space:
xor = L[0]
for i in range(1, n): # Using the xor operator to reduce the list
    xor = xor ^ L[i]
diffBit = 0
for i in range(32): # Finding the first differing bit in xor
    if xor & (1 << i) != 0: # Use the shift operator << for bits
        diffBit = i
        break
# Make 2 lists divided based on weather the i'th bit is a 0 or a 1
# Actually we only need to store the xor reduction of those lists
l1 = 0
l2 = 0
for i in range(n):
    if L[i] & (1 << diffBit) ==0:
        l1 = l1 ^ L[i]
    else:
        l2 = l2 ^ L[i]
print(l1, l2)