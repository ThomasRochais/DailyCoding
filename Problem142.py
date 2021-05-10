def sol(S):
    left = 0
    right = 0
    n = len(S)
    for i in range(n):
        if S[i] == "(":
            left += 1
        elif S[i] == ")":
            left -= 1
            if left < 0:
                return("Not Balanced")
        else:
            left += 1
        if S[n-1-i] == ")":
            right += 1
        elif S[n-1-i] == "(":
            right -= 1
            if right < 0:
                return("Not Balanced")
        else:
            right += 1
    return("Balanced")

print(sol("(()*"))
print(sol("(*)"))
print(sol(")*("))
print(sol("(*(*)))"))
print(sol("(*))"))
print(sol("***)("))
print(sol("***)(**"))
print(sol("()"))
print(sol("(*))"))