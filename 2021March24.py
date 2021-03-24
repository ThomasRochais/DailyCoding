from math import inf

def nearestLarger(L, index):
    val = L[index]
    i = index + 1
    j = index - 1
    N = len(L)
    while i < N or j > 0:
        if i < N:
            if L[i] > val:
                return i
            i += 1
        if j > 0:
            if L[j] > val:
                return j
            j -= 1
    return inf
print(nearestLarger([4, 1, 3, 5, 6], 0))
print(nearestLarger([4, 1, 3, 5, 6], 4))
print(nearestLarger([4, 1, 3, 5, 6], 2))
print(nearestLarger([4, 1, 3, 5, 6], 1))

# If we can preprocess the array, we can do this in constant time:
def nextLarger(L):
    N = len(L)
    s = [] # Stack of elements from the list L
    si = [] # Corresponding indices as taken from L
    nextLarger = {} # Dictionary of next largest element
    s.append(L[0]) # Start with the first element in the list
    si.append(0)
    for i in range(1, N): # Loop through every list element
        next = L[i]
        if len(s) != 0: # If the stack is not empty
            el = s.pop() # Extract the latest element added to the stack
            eli = si.pop() # And the corresponding index
            # If the popped elemement is smaller than next, then
            # a) store the pair, next is indeed the next largest element
            # b) keep popping while elements are smaller and stack is not empty
                 # indeed, next is also the next largest element for all those smaller elements
            while el < next:
                nextLarger[eli] = i
                if len(s) == 0:
                    break
                el = s.pop()
                eli = si.pop()
            # If element is greater than next, then push the element back
            if el > next:
                s.append(el)
                si.append(eli)
        # Push next to stack so that we can find next greater for it
        s.append(next)
        si.append(i)
    # After iterating over the loop, the remaining elements in stack do not have
    # the next greater element, so assign +inf for them
    while len(s) != 0:
        el = s.pop()
        eli = si.pop()
        nextLarger[eli] = inf
    return(nextLarger)

def nearestLargerList(L):
    N = len(L)
    nL = nextLarger(L)
    pL = nextLarger(L[::-1])
    nearestLargers = {}
    for i in range(N):
        if abs(nL[i] - i) <= abs(pL[N-1-i] - N-1-i):
            nearestLargers[i] = nL[i]
        else:
            nearestLargers[i] = pL[N-1-i]
    return(nearestLargers)

L1 = nearestLargerList([4, 1, 3, 5, 6])
L2 = nearestLargerList([11, 13, 21, 3])
print(L1)
print(L2)
print(L1[0])
print(L1[4])
print(L1[2])
print(L1[1])