def palindromes(lst):
    indices = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j:
                word = lst[i] + lst[j]
                if is_palindrome(word):
                    indices.append((i,j))
    return indices

def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

print(palindromes(["code", "edoc", "da", "d"]))