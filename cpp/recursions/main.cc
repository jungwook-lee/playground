// Practice using recursions in cpp
#include <iostream>
#include <tuple>

using namespace std;

int factorial(int n) {
  // Base case
  if (n == 0)
    return 1;
  else
    // Recursion Case
    return n * factorial(n - 1);
}

int binary_search(int* data, int target, int low, int high) {
  if (low > high)
    return -1;
  int mid = (high + low) / 2;

  if (data[mid] == target) {
    return mid;
  } else if (data[mid] > target) {
    binary_search(data, target, low, mid);
  } else {
    binary_search(data, target, mid, high);
  }
}

struct double_int
{
  int f_n0;
  int f_n1;
};

double_int fib(int n) {
  double_int ret_val;
  double_int out_val;

  if (n <= 1) {
    ret_val.f_n0 = n;
    ret_val.f_n1 = 0;
    return ret_val;
  } else {
    // returns 2 numbers, where [0] is a+b, [1] is a
    out_val = fib(n - 1);
    ret_val.f_n0 = out_val.f_n1 + out_val.f_n0;
    ret_val.f_n1 = out_val.f_n0;
    return ret_val;
  }
}

int main() {
  // Calculate factorial
  int test_num = 5;
  cout << factorial(test_num) << endl;

  int test_array [10] = {2, 4, 5, 7, 8, 9, 12, 14, 17, 19};
  cout << binary_search(test_array, 12, 0, 9) << endl;

  test_num = 6;
  double_int out = fib(test_num);
  cout << out.f_n0 << endl;

  return 0;
}