#ifndef CPP_DYNAMIC_ARRAY_H_
#define CPP_DYNAMIC_ARRAY_H_

#include <vector>

class DynamicArray{
  public:
    DynamicArray();
    ~DynamicArray();

    int get_length();
    int get_size();
    int get_item(int index);
    void append(int num);
    void resize(int capacity);

  private:
    int* make_array(int capacity);

    int count;
    int capacity;
    int* int_array;
};

#endif //CPP_DYNAMIC_ARRAY_H_