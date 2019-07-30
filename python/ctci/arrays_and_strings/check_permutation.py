# Simple Case
# def check_perm(str1, str2):
#     if len(str1) != len(str2):
#         return False
#
#     table1, table2 = dict(), dict()
#     for i in range(len(str1)):
#         if not str1[i] in table1:
#             table1[str1[i]] = 1
#         else:
#             table1[str1[i]] += 1
#
#         if not str2[i] in table2:
#             table2[str2[i]] = 1
#         else:
#             table2[str2[i]] += 1
#
#     for key, val in table1.iteritems():
#         if not key in table2:
#             return False
#         if val != table2[key]:
#             return False
#     return True

# Optimized
def check_perm(str1, str2):
    if len(str1) != len(str2):
        return False

    table = [0] * 128 # Depends on the given input.
    for i in range(len(str1)):
        table[ord(str1[i])] += 1

    for i in range(len(str2)):
        table[ord(str2[i])] -= 1
        if table[ord(str2[i])] < 0:
            return False

    return True

# O(nlogn) sort, then linear comparison
def check_perm_2(str1, str2):
    # convert str1 to bit list
    if sorted(str1) != sorted(str2):
        return False
    return True

if __name__ == '__main__':
    test1 = 'aaabbc'
    test2 = 'ababac'
    print(check_perm(test1, test2))
    test3 = 'ababab'
    print(check_perm(test1, test3))
    test4 = 'ababa'
    print(check_perm(test1, test4))

    test1 = 'aaabbc'
    test2 = 'ababac'
    print(check_perm_2(test1, test2))
    test3 = 'ababab'
    print(check_perm_2(test1, test3))
    test4 = 'ababa'
    print(check_perm_2(test1, test4))