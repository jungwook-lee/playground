#include <iostream>

using namespace std;

class Node {
    public:
    int data;
    Node* next = NULL;

    // Default Constructor
    Node() {this->data = 0;}

    // Constructor
    Node(int num) {this->data = num;}
};

class LinkedList {
    public:
    Node* head;

    void print_list() {
        // Check if head is NULL
        if (this->head == NULL)
            return;

        Node* cur_node = head;
        while (cur_node != NULL) {
            cout << cur_node->data << " ";
            cur_node = cur_node->next;
        }
        cout << endl;
    }

    // TODO: Implement the following
    void insert();
    void insert_end();
    void delete_at();
};

int main() {
  // Make a linked list with int as the data
  LinkedList list;

  Node node1(5);
  Node node2(10);
  Node node3(4);

  list.head = &node1;
  node1.next = &node2;
  node2.next = &node3;

  list.print_list();

  return 0;
}