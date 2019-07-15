# Practice implementation of dynamicaly array in python
import ctypes

class DynamicArray(object):

    def __init__(self):
        self.n = 0 # Count actual elements
        self.capacity = 1 # Default capacity
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self, k):
        if not 0 <= k < self.n:
            return IndexError
        return self.A[k]

    def append(self, ele):
        if self.n == self.capacity:
            self._resize(2 * self.capacity)
        self.A[self.n] = ele
        self.n += 1

    def _resize(self, new_cap):
        B = self.make_array(new_cap)
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B
        self.capacity = new_cap

    def make_array(self, new_cap):
        return (new_cap * ctypes.py_object)()

if __name__ == "__main__":
    arr = DynamicArray()

    for i in range(8):
        arr.append(i)
        print('Inserting {}, arr size {}'.format(i, arr.capacity))

