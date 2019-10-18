import random

def quick_sort(data, low, high):
    # Base case is exit, when low and high are same
    if (low < high):
        pi = partition(data, low, high)

        quick_sort(data, low, pi - 1)
        quick_sort(data, pi + 1, high)

# partition/pivot function
def partition(data, low, high):
    """ Pivot function used in quick sort, but selects the last
    element as the pivoting point"""
    key = data[high]
    i = low - 1
    for j in range(low, len(data) - 1):
        if data[j] < key:
            i += 1
            data[i], data[j] = data[j], data[i]
    data[i + 1], data[high] = data[high], data[i + 1]
    return (i + 1)


if __name__ == '__main__':
    print('Test Partitioning from i = 0, 6')
    sample = [10, 80, 30, 90, 40, 50, 70]
    print(sample)
    partition(sample, 1 , len(sample) - 1)
    print(sample)

    print('Test Partitioning from i = 2, 6')
    sample = [10, 80, 30, 90, 40, 50, 70]
    print(sample)
    partition(sample, 2 , len(sample) - 1)
    print(sample)

    print('Test Partitioning from i = 2, 4')
    sample = [10, 80, 30, 90, 40, 50, 70]
    print(sample)
    partition(sample, 2 , 4)
    print(sample)

    print('Test Quick Sort')
    sample_size = 20
    sample = random.sample(range(100), sample_size)
    print(sample)
    quick_sort(sample, 0, sample_size - 1)
    print(sample)
