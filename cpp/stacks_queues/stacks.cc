#include <iostream>

using namespace std;

// Implement a stack using a linked list
class Stack {

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

  public:
    // Default Constructor
    Stack() {
      this->head = NULL;
    }

    void push(int item) {
      Node* new_node = new Node(item, this->head);
      this->head = new_node;
    }

    int pop() {
      if (head == NULL) {
        throw "Stack Empty!";
      }
      Node* cur_head = this->head;
      int ret_val = cur_head->data;
      this->head = cur_head->next;
      free(cur_head);
      return ret_val;
    }

    int peek() {
      if (head == NULL) {
        throw "Stack Empty!";
      }
      return (this->head)->data;
    }

    bool isEmpty() {
      return (head == NULL);
    }
};

int main() {
  Stack st;
  st.push(1);
  cout << (st.peek()) << endl;
  st.push(2);
  cout << (st.peek()) << endl;
  st.push(3);
  cout << (st.peek()) << endl;
  cout << (st.isEmpty()) << endl;

  cout << (st.pop()) << endl;
  cout << (st.pop()) << endl;
  cout << (st.pop()) << endl;
  cout << (st.isEmpty()) << endl;
}