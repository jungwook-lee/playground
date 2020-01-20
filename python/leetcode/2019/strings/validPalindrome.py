def validPalindrome(s):
    if not s:
        return True
    i, j = 0, len(s) - 1
    while j >= i:
        if not s[i].isalnum():
            i += 1
            continue
        if not s[j].isalnum():
            j -= 1
            continue
        if s[i].lower() == s[j].lower():
            i += 1
            j -= 1
        else:
            return False
    return True

print(validPalindrome("R2d2a2d2R"))
print(validPalindrome("A man, a plan, a canal: Panama"))
print(validPalindrome("race a car"))
print(validPalindrome(""))
print(validPalindrome("     "))
print(validPalindrome("a;@#@b#$a!b%"))