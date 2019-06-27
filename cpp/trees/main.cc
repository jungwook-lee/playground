#include <iostream>

using namespace std;

class Node {
  public:
    Node* left;
    Node* right;
    int data;

    // Constructor
    Node(int num): left{NULL}, right{NULL} {data = num;}

    Node(int num, Node* n_left, Node* n_right): data{num}, left{n_left}, right{n_right} {}

};

void in_order_print(Node* root) {
  if (root != NULL) {
    in_order_print(root->left);
    cout << root->data;
    in_order_print(root->right);
  }
}

int main() {
  Node node1(1), node2(7), node3(10);
  Node node4(3, &node1, &node2);
  Node node5(2, &node3, NULL);
  Node root(5, &node4, &node5);
  
  in_order_print(&root);
  cout << endl;
  return 0;
}
