from sort_insertion import insertion_sort

def bucket_sort(data):
    # Create buckets
    n = 10
    buckets = [[] for i in range(n)]

    # Fill the buckets with data
    for val in data:
        index = int(n * val)
        buckets[index].append(val)

    # Sort each of the buckets using insertion sort
    for bucket in buckets:
        insertion_sort(bucket)

    out = []
    for bucket in buckets:
        out.extend(bucket)

    return out

if __name__ == '__main__':
    x = [0.897, 0.565, 0.656,
         0.1234, 0.665, 0.3434]
    print("Sorted Array is")
    print(bucket_sort(x))