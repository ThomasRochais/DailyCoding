from collections import deque

def transform_path(start, end, dic):
    wordlist = [start]
    if start == end:
        return start
    if end not in dic:
        return None
    level, wordlength = 0, len(start)
    Q = deque()
    Q.append(start)
    while (len(Q) > 0):
        level += 1
        wordlist.append(None)
        sizeofQ = len(Q)
        for i in range(sizeofQ):
            word = [j for j in Q.popleft()]
            for pos in range(wordlength):
                orig_char = word[pos] # Retain the original character at the current position
                for c in range(ord('a'), ord('z')+1): # Replace the current character with every possible lowercase alphabet
                    word[pos] = chr(c)
                    if("".join(word) == end):
                        wordlist[level] = "".join(word)
                        return wordlist
                    if ("".join(word) in dic):
                        del dic["".join(word)]
                        Q.append("".join(word))
                        wordlist[level] = "".join(word)
                word[pos] = orig_char
    return None


D = {}
D["dot"] = 1
D["dop"] = 1
D["dat"] = 1
D["cat"] = 1
start = "dog"
target = "cat"
print(transform_path(start, target, D))

D = {}
D["dot"] = 1
D["tod"] = 1
D["dat"] = 1
D["dar"] = 1
start = "dog"
target = "cat"
print(transform_path(start, target, D))


D = {}
D["poon"] = 1
D["plee"] = 1
D["same"] = 1
D["poie"] = 1
D["plie"] = 1
D["poin"] = 1
D["plea"] = 1
start = "toon"
target = "plea"
print(transform_path(start, target, D))

D = {}
D["poon"] = 1
D["plee"] = 1
D["same"] = 1
D["poie"] = 1
D["plie"] = 1
D["poin"] = 1
D["plea"] = 1
D["toie"] = 1
D["toin"] = 1
start = "toon"
target = "toin"
print(transform_path(start, target, D))