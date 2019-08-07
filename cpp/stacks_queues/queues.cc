#include <iostream>

using namespace std;

// Implement a Queue using a linked list
class Queue {
  private:
  // Node class definition
    class Node {
      public:
        int data;
        Node* next;

      Node(int data, Node* next) {
        this->data = data;
        this->next = next;
      }
    };

  Node* head;
  Node* tail;

  public:
    Queue() {
      this->head = NULL;
      this->tail = NULL;
    }

    // insert from the tail
    void insert(int item) {
      Node* new_node = new Node(item, NULL);
      if (this->tail != NULL) {
        this->tail->next = new_node;
      }
      this->tail = new_node;
      if (this->head == NULL) {
        this->head = this->tail;
      }
    }

    // remove from the head
    int remove() {
      if (this->head == NULL) {
        throw "Queue Empty!";
      }
      int ret_val = this->head->data;
      Node* temp_head = this->head;
      this->head = this->head->next;
      if (this->head == NULL) {
        this->tail = NULL;
      }
      free(temp_head);
      return ret_val;
    }

    int peek() {
      if (this->head == NULL) {
        throw "Queue Empty!";
      }
      return (this->head)->data;
    }

    bool isEmpty() {
      return (this->head == NULL);
    }

};

int main() {
  Queue q;
  q.insert(1);
  cout << (q.peek()) << endl;
  q.insert(2);
  cout << (q.peek()) << endl;
  q.insert(3);
  cout << (q.peek()) << endl;
  cout << (q.isEmpty()) << endl;

  cout << (q.remove()) << endl;
  cout << (q.remove()) << endl;
  cout << (q.remove()) << endl;
  cout << (q.isEmpty()) << endl;
}