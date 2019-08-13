#include <iostream>
#include <bitset>

using namespace std;

int repeatedArithmeticShift(int x, int count) {
  for (int i = 0; i < count; i++) {
    x >>= 1;
  }
  return x;
}

int repeatedLogicalShift(int x, int count) {
  for (int i = 0; i < count; i++) {
    x <<= 1;
  }
  return x;
}

bool getBit(int num, int i) {
  return (num & (1 << i - 1)) != 0;
}

int setBit(int num, int i) {
  return (num | (1 << i - 1));
}

int clearBit(int num, int i) {
  return (num & ~(1 << i - 1));
}

int updateBit(int num, int i, int val) {
  int mask = ~(1 << i - 1);
  return (num & mask) | (val << i - 1);
}

void print_bits(int num) {
  bitset<8> test_bit(num);
  cout << test_bit << endl;
}

int main() {
  int test = -93242;
  int count = 40;

  // Should output -1, since 1111....
  cout << repeatedArithmeticShift(test, count) << endl;

  // Should output 0, since 00000....
  cout << repeatedLogicalShift(test, count) << endl;

  int test_out;
  int test_var = 18;

  print_bits(test_var);

  test_out = getBit(test_var, 2);
  cout << test_out << endl;

  test_out = getBit(test_var, 3);
  cout << test_out << endl;

  test_out = setBit(test_var, 3);
  print_bits(test_out);

  test_out = clearBit(test_var, 3);
  print_bits(test_out);

  test_out = updateBit(test_var, 5, 0);
  print_bits(test_out);

  test_out = updateBit(test_var, 5, 1);
  print_bits(test_out);

  return 0;
}