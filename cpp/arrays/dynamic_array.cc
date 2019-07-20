#include <iostream>
#include <vector>
#include "dynamic_array.h"

using namespace std;

DynamicArray::DynamicArray () {
  this->count = 0;
  this->capacity = 1;
  this->int_array = DynamicArray::make_array(this->capacity);
};

DynamicArray::~DynamicArray() {
  free(this->int_array);
}

int DynamicArray::get_length() {
  return this->count;
}

int DynamicArray::get_size() {
  return this->capacity;
}

int DynamicArray::get_item(int index) {
  // If the array is NULL, early exit
  if (this->int_array == NULL) {
    return -1;
  }

  // If the index doesn't make sense exit
  if (0 < index && index >= this->capacity) {
    return -1;
  }

  return this->int_array[index];
}

void DynamicArray::append(int num) {
  // check if count is smaller than the capacity
  if (this->count == this->capacity) {
    DynamicArray::resize(2 * this->capacity);
  }
  this->int_array[this->count] = num;
  this->count += 1;
}

void DynamicArray::resize(int capacity) {
  // First make a new array with the size
  int* new_array = make_array(capacity);

  // Second, copy the contents over
  for (int i = 0; i < this->count; i++) {
    new_array[i] = this->int_array[i];
  }

  // Third, replace the point to the new one
  free(this->int_array);
  this->int_array = new_array;
  this->capacity = capacity;
}

int* DynamicArray::make_array(int capacity) {
  // make the array
  int* ret_arr = NULL;
  ret_arr = (int*) malloc(sizeof(int) * capacity);
  return ret_arr;
}

