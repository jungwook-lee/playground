#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

// Version with no bit vector
bool is_unique(string input) {
  if (input.size() > 128) return false;

  unordered_map<int, bool> ht = {};
  for (int i = 0; i < input.size(); i++) {
    char cur_char = int(input[i]);
    if (ht.find(cur_char) != ht.end())
      return false;
    ht[cur_char] = true;
  }
  return true;
}

// Version with bit vector
bool is_unique_2(string input) {
  // Try using a bit vector to keep track
  int tester = 0;
  for (int i = 0; i < input.size(); i++) {
    int cur_char =  1 << int(input[i] - 'a');
    if (tester & cur_char) return false;
    tester |= cur_char;
  }
  return true;
}

int main () {
    string test = "abcde";
    cout << is_unique(test) << endl;
    test = "abcdea";
    cout << is_unique(test) << endl;

    test = "abcde";
    cout << is_unique_2(test) << endl;
    test = "abcdea";
    cout << is_unique_2(test) << endl;
    return 0;
}