#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;

// O(nlogn) version. Sort then compare
bool check_permutation(string str1, string str2) {
  sort(str1.begin(), str1.end());
  sort(str2.begin(), str2.end());
  if (str1 != str2) return false;
  return true;
}

// O(n) version with some space usage
bool check_permutation_2(string s1, string s2) {
  if (s1.size() != s2.size()) return false;

  // Count occurance of characters assuming ASCII
  int table [128] = {0};
  for (auto c: s1) {
    table[int(c)]++;
  }

  for (auto c:s2) {
    table[int(c)]--;
    if (table[int(c)] < 0) return false;
  }
  return true;
}

int main () {
    string test = "aaabbc";
    string test1 = "ababac";
    string test2 = "ababab";
    string test3 = "abab";

    cout << check_permutation(test, test1) << endl;
    cout << check_permutation(test, test2) << endl;
    cout << check_permutation(test, test3) << endl;

    cout << check_permutation_2(test, test1) << endl;
    cout << check_permutation_2(test, test2) << endl;
    cout << check_permutation_2(test, test3) << endl;
    return 0;
}