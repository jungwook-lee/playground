import collections

def countSort(arr):
    count = [0] * 256
    ans = ["" for _ in arr]

    # Store counts
    for c in arr:
        count[ord(c)] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # reconstruct the char array
    for c in arr:
        index = count[ord(c)]
        ans[index - 1] = c
        count[ord(c)] -= 1

    return "".join(ans)

if __name__ == '__main__':
    arr = "geeksforgeeks"
    ans = countSort(arr)
    print(ans)