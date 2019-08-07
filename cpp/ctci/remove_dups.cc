#include <iostream>
#include <unordered_map>

using namespace std;

struct Node{
  int data;
  Node* next;
};

void remove_dups(Node* head) {
  // early exit
  if (head == NULL) return;

  // make hash
  unordered_map<int, bool> hash;
  hash[head->data] = true;
  Node* prev = head;
  Node* cur = head->next;
  while (cur != NULL) {
    if (hash.find(cur->data) != hash.end()) {
      // remove element
      prev->next = cur->next;
      cur = cur->next;
    } else {
      hash[cur->data] = true;
      cur = cur->next;
      prev = prev->next;
    }
  }
}

void print_nodes(Node* head) {
  Node* cur = head;
  while(cur != NULL) {
    cout << cur->data;
    cur = cur->next;
  }
  cout << endl;
}

int main() {
  Node node_1;
  node_1.data = 1;
  Node node_2;
  node_2.data = 2;
  Node node_3;
  node_3.data = 3;
  Node node_4;
  node_4.data = 1;

  node_1.next = &node_2;
  node_2.next = &node_3;
  node_3.next = &node_4;
  node_4.next = NULL;

  print_nodes(&node_1);

  remove_dups(&node_1);
  print_nodes(&node_1);
  return 0;
}