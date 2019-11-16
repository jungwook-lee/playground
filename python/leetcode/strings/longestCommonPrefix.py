def longestCommonPrefix(strs):
    if not strs:
        return ""
    if len(strs) == 1:
        return strs[0]
    elif not strs[0]:
        return ""

    i, prefix = 0, ""
    while i < len(strs[0]):
        cur_l = strs[0][i]
        for word in strs:
            if not word:
                return ""
            if i >= len(word):
                return prefix
            if word[i] != cur_l:
                return prefix
        prefix += cur_l
        i += 1
    return prefix

# Example Good Answer

# def longestCommonPrefix(self, strs):
#     """
#     :type strs: List[str]
#     :rtype: str
#     """
#     if not strs:
#         return ""
#     shortest = min(strs, key=len)
#     for i, ch in enumerate(shortest):
#         for other in strs:
#             if other[i] != ch:
#                 return shortest[:i]
#     return shortest

test = ["flower","flow","flight"]
print(longestCommonPrefix(test))

test = ["dog","racecar","car"]
print(longestCommonPrefix(test))

test = ["abc","ab","a"]
print(longestCommonPrefix(test))

test = ["abc","ab",""]
print(longestCommonPrefix(test))

test = ["","ab","a"]
print(longestCommonPrefix(test))

test = []
print(longestCommonPrefix(test))

test = ["abcdefg", "abcdefgh", "abcdfghe"]
print(longestCommonPrefix(test))