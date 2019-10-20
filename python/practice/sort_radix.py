import math
import random

def countSort(data, digit=0):
    count = [0] * 10
    ans = [None for _ in data]

    # Store counts
    for val in data:
        # Convert the units and store them in counts
        index = int (val / (10 ** digit))
        count[index % 10] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # reconstruct the char array
    for val in reversed(data):
        c_i = int(val / (10 ** digit)) % 10
        index = count[c_i]
        ans[index - 1] = val
        count[c_i] -= 1

    for i in range(len(ans)):
        data[i] = ans[i]

def radix_sort(data):
    max_num = max(data)

    # Calculate how many digits
    digits = int(math.log(max_num, 10))
    for exp in range(digits + 1):
        countSort(data, exp)

if __name__ == '__main__':
    sample_size = 100
    sample = random.sample(range(100), sample_size)
    radix_sort(sample)
    print(sample)