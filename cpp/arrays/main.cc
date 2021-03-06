// Array practice from http://www.cplusplus.com/doc/tutorial/arrays/
#include <iostream>

#include "dynamic_array.h"
#include "dynamic_array.cc"

using namespace std;

// Testing array as function input
void print_array(int arg[], int arr_size) {
  for (int i = 0; i < arr_size; i++) {
    cout << arg[i] << " ";
  }
  cout << endl;
  return;
}

void test_cpp_arrays() {
  // Implement an array in C++ (random initialization)
  const int arr_size = 5;
  int foo0 [arr_size];
  print_array(foo0, arr_size);

  // Initialiaze with values
  int foo1 [arr_size] = {1, 2, 3, 4, 5};
  print_array(foo1, arr_size);

  // Initialize with values, rest will be default values
  int foo2 [arr_size] = {1, 2, 3};
  print_array(foo2, arr_size);

  // Initialize with no values
  int foo3 [5] = {};
  cout << "Array size is " << sizeof(foo3)/sizeof(*foo3) << endl;

  // Compiler automatically checks for the size
  int foo4 [] = {1, 2, 3, 4, 5, 6, 7};
  cout << "Array size is " << sizeof(foo4)/sizeof(*foo4) << endl;

  // Can also also declare like
  int foo5[] {1, 2, 3, 4, 5};

  // Access elements
  cout << foo5[3] << endl;
  foo5[3] = 10;
  cout << foo5[3] << endl;
  cout << foo5[3 + 1] << endl;
  cout << foo5[foo5[0]] << endl;

  // Multidimensional
  int bar [10][10];

  // Call a function with an array input
  int bar1 [4];
  print_array(bar1, sizeof(bar1)/sizeof(int));
}

int main() {
    // Test cpp array types
    test_cpp_arrays();

    // Test Dynamic Array Implementation
    DynamicArray d_arr;
    cout << d_arr.get_size() << endl;

    d_arr.append(0);
    d_arr.append(1);
    d_arr.append(2);
    d_arr.append(3);
    d_arr.append(4);
    d_arr.append(5);
    d_arr.append(6);
    d_arr.append(255);

    cout << d_arr.get_size() << endl;
    cout << d_arr.get_item(7) << endl;

    return 0;
}
