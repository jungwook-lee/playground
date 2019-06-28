// Sample Header file from https://www.geeksforgeeks.org/binary-heap/

// A C++ program to demonstrate common Binary Heap Operations
#include<iostream>
#include<climits>
using namespace std;

// Prototype of a utility function to swap two integers
void swap(int *x, int *y);

// A class for Min Heap
class MinHeap
{
    int *harr; // pointer to array of elements in heap
    int capacity; // maximum possible size of min heap
    int heap_size; // Current number of elements in min heap
public:
    // Constructor
    MinHeap(int capacity);

    // to heapify a subtree with the root at given index
    void MinHeapify(int i);

    int parent(int i) { return (i-1)/2; }

    // to get index of left child of node at index i
    int left(int i) { return (2*i + 1); }

    // to get index of right child of node at index i
    int right(int i) { return (2*i + 2); }

    // to extract the root which is the minimum element
    int extractMin();

    // Decreases key value of key at index i to new_val
    void decreaseKey(int i, int new_val);

    // Returns the minimum key (key at root) from min heap
    int getMin() { return harr[0]; }

    // Deletes a key stored at index i
    void deleteKey(int i);

    // Inserts a new key 'k'
    void insertKey(int k);
};

void swap(int *x, int *y) {
    if (x == NULL || y == NULL) {
        return;
    }

    int temp_val= *x;
    *x = *y;
    *y = temp_val;
}

MinHeap::MinHeap(int capacity) {
    heap_size = 0;
    capacity = capacity;
    harr = new int[capacity];
}

void MinHeap::MinHeapify(int i) {
    if (harr == NULL) {
        return;
    }

    int l = left(i);
    int r = right(i);
    int smallest = i;

    if (l < heap_size && harr[l] < harr[i]) {
        smallest = l;
    }
    if (r < heap_size && harr[r] < harr[smallest]) {
        smallest = r;
    }
    if (smallest != i) {
        swap(&harr[i], &harr[smallest]);
        MinHeapify(smallest);
    }
}

int MinHeap::extractMin() {
    if (heap_size <= 0) {
        cout << "Heap is empty!" << endl;
        return INT_MAX;
    }
    if (heap_size == 1) {
        heap_size--;
        return harr[0];
    }

    // First swap with last element
    int min_val = harr[0];
    harr[0] = harr[heap_size - 1];
    heap_size--;
    MinHeapify(0);

    return min_val;
}

// Decreases value of key at index 'i' to new_val.  It is assumed that
// new_val is smaller than harr[i].
void MinHeap::decreaseKey(int i, int new_val) {
    harr[i] = new_val;
    while (i != 0 && harr[parent(i)] > new_val) {
        swap(&harr[parent(i)], &harr[i]);
        i = parent(i);
    }
}

void MinHeap::insertKey(int k) {
    if (heap_size == capacity) {
        cout << "\nOverflow: Could not insertKey\n";
    }

    int i = heap_size;
    harr[i] = k;
    heap_size += 1;

    // Fix the heap
    while (i > 0 && harr[parent(i)] > k) {
        swap(&harr[parent(i)], &harr[i]);
        i = parent(i);
    }
}

void MinHeap::deleteKey(int i) {
    decreaseKey(i, INT_MIN);
    extractMin();
}

int main()
{
    MinHeap h(11);
    h.insertKey(3);
    h.insertKey(2);
    h.deleteKey(1);
    h.insertKey(15);
    h.insertKey(5);
    h.insertKey(4);
    h.insertKey(45);
    cout << h.extractMin() << " ";
    cout << h.getMin() << " ";
    h.decreaseKey(2, 1);
    cout << h.getMin();
    return 0;
}
