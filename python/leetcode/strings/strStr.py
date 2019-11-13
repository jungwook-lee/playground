# Naive O(m*n) case
def strStr(haystack, needle):
    h, n = haystack, needle
    if not n:
        return 0
    if not h:
        return -1
    if len(h) < len(n):
        return -1

    cur, i, j = 0, 0, 0
    while i < len(h):
        if n[j] == h[i]:
            j += 1
            i += 1
        elif j > 0 and n[j] != h[i]:
            j = 0
            cur += 1
            i = cur
        else:
            i += 1
            cur += 1

        if j >= len(n):
            return i - len(n)
    return -1

print(strStr("hello","ll"))
print(strStr("aaaaa","bba"))
print(strStr("needle", "needles"))
print(strStr("", ""))
print(strStr("", "a"))
print(strStr("abab", ""))
print(strStr("hello this is me", "is"))
print(strStr("lelelelelelelelelel", "lel"))
print(strStr("lelelelelelelelelee", "lee"))
print(strStr("mississippi", "issip"))
print(strStr("mississippi", "pi"))
print(strStr("mississippi", "sipp"))