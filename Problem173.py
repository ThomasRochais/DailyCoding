from itertools import permutations
def subconcat(lst, word):
    indices = []
    for p in permutations(lst):
        concatword = "".join(p)
        try: 
            indices.append(word.index(concatword))
        except ValueError:
            continue
    print(indices)
    return indices

subconcat(["cat", "dog"], "dogcatcatcodecatdog")
subconcat(["dog", "cat"], "barfoobazbitbyte")
