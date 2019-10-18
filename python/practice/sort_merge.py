import random

def merge_sort(data):
    print('Split data', data)
    if len(data) > 1:
        mid = len(data) // 2
        # Note that data is copied, so no references
        left_half = data[:mid]
        right_half = data[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the left half and right half
        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                data[k] = left_half[i]
                i += 1
            else:
                data[k] = right_half[j]
                j += 1
            k += 1

        # Deal with remainders from left side
        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1

        # Deal with remainders from right side
        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1

        print('Merging', data)

    else:
        # Base case here, since if len array = 1,
        # Doesn't need to be sorted
        return

if __name__ == '__main__':
    print('Test Merge Sort')
    sample_size = 20
    sample = random.sample(range(100), sample_size)
    print(sample)
    merge_sort(sample)
    print(sample)
