from math import inf
# Returns minimum distance in string "str" between word1 and word2
# as measured by the number of words between word1 and word2
def dist_words(str, word1, word2):
    words = str.split()
    p1 = -inf
    p2 = inf
    pw1 = None
    pw2 = None
    min_dist = inf
    for i in range(len(words)):
        if words[i] == word1 or words[i] == word2:
            if (pw1 == None or pw1 == words[i]) and pw2 != words[i]:
                pw1 = words[i]
                p1 = i
            else:
                pw2 = words[i]
                p2 = i
        min_dist = min(min_dist, abs(p2-p1)-1)
        if min_dist == 0:
            return 0
    return (min_dist)
print(dist_words("dog cat hello cat dog dog hello cat world", "hello", "world"))