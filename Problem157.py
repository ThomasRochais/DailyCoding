import enchant
from itertools import permutations
def palindrome(str):
    d = enchant.Dict("en_US")
    perm = permutations(str)
    for new_str in perm:
        n_str = ''.join(new_str)
        if d.check(n_str) and n_str != "abc":
            print(True)
            return True
    print(False)
    return False

palindrome("carrace")
palindrome("daily")