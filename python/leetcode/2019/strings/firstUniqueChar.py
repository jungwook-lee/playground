import collections

def firstUniqueChar(s):
    if not s:
        return -1

    mem = collections.defaultdict(int)
    for l in s:
        mem[l] += 1

    for i in range(len(s)):
        if mem[s[i]] == 1:
            return i
    return -1

print(firstUniqueChar("leetcode"))
print(firstUniqueChar("loveleetcode"))
print(firstUniqueChar(""))
print(firstUniqueChar("f"))
print(firstUniqueChar("fffffz"))
print(firstUniqueChar("ffzzaabb"))
