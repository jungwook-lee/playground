#include <iostream>

using namespace std;

void urlify(char* in_str, int true_length) {
  // count spaces
  int spaces = 0;
  for (int i = 0; i < true_length; i++) {
    if (in_str[i] == ' ') {
      spaces += 1;
    }
  }
  // get new length
  int new_len = true_length + (2 * spaces);
  int j = new_len - 1;
  for (int i = true_length - 1; i >= 0; i--) {
    if (in_str[i] != ' ') {
      in_str[j] = in_str[i];
      j -= 1;
    } else {
      in_str[j] = '0';
      in_str[j - 1] = '2';
      in_str[j - 2] = '%';
      j -= 3;
    }
  }
}

int main() {
  char test [] = "Mr John Smith    ";
  int t_len = 13;
  cout << test << endl;
  urlify(test, t_len);
  cout << test << endl;
  return 0;
}