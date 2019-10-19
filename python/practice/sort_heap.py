import random


def heap_sort(data):
    # heapify the array
    for i in range(len(data) // 2 - 1, -1, -1):
        max_heap(data, len(data), i)

    # Extract elements
    for i in range(len(data) - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        max_heap(data, i, 0)


def max_heap(data, n, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    # Check left child
    if left < n and data[largest] < data[left]:
        largest = left

    # Check right child
    if right < n and data[largest] < data[right]:
        largest = right

    # Heapify if the largest is left or right
    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        max_heap(data, n, largest)


if __name__ == '__main__':
    print('Test Heap Sort')
    sample_size = 9
    sample = random.sample(range(100), sample_size)
    print(sample)

    heap_sort(sample)
    print(sample)
