# In-place version of insertion sort
import random

def insertion_sort(data):
    for i in range(1, len(data)):
        cur_val = data[i]
        j = i - 1
        while 0 <= j and cur_val < data[j]:
            # Move the element to the next
            data[j + 1] = data[j]
            j -= 1
        # Swap when next data is larger
        data[j + 1] = cur_val

if __name__ == '__main__':
    sample = random.sample(range(100), 20)
    print(sample)
    insertion_sort(sample)
    print(sample)