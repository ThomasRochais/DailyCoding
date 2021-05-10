def first_recurring(str):
    dic = {}
    for s in str:
        if s in dic:
            return s
        else:
            dic[s] = 1
    return None
print(first_recurring("acbbac"))
print(first_recurring("abcdef"))