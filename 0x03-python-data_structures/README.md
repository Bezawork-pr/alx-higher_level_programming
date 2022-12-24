# <pre> Python - Data Structures: Lists, Tuples </pre>
This project targets to master lists, learn to identify the difference between strings and lists and learn to use lists as stacks and queues. In addition, learn about list comprehensions, tuples, tuple packing, sequence and sequence unpacking.
## <pre> Function prototypes    <img src="https://user-images.githubusercontent.com/107026397/209424557-72ec9e7b-8f5a-4c69-9136-2629ca6d2ab0.svg" width = 3% height= 3%> </pre>
| Files  | Prototypes |
| ------------- | ------------- |
| 0-print_list_integer.py|def print_list_integer(my_list=[]): |
|1-element_at.py| def element_at(my_list, idx):|
| 2-replace_in_list.py  | def replace_in_list(my_list, idx, element): |
| 3-print_reversed_list_integer.py | def print_reversed_list_integer(my_list=[]):  |
| 4-new_in_list.py  | def new_in_list(my_list, idx, element):  |
| 5-no_c.py  | def no_c(my_string):  |
| 6-print_matrix_integer.py  | def print_matrix_integer(matrix=[[]]): |
| 7-add_tuple.py  |def add_tuple(tuple_a=(), tuple_b=()):  |
| 8-multiple_returns.py  | def multiple_returns(sentence):  |
| 9-max_integer.py  | def max_integer(my_list=[]):  |
| 10-divisible_by_2.py  | def divisible_by_2(my_list=[]):  |
| 11-delete_at.py  | def delete_at(my_list=[], idx=0): |
| 13-is_palindrome.c,  | int is_palindrome(listint_t ** head);  |
| 100-print_python_list_info.c | void print_python_list_info(PyObject *p); |
## <pre> Tasks   <img src="https://user-images.githubusercontent.com/107026397/209425131-1d190ca6-b53b-49a9-b00a-6d697c9e4473.svg" height=3% width=3%></pre>
### 0. Print a list of integers
*  [0-print_list_integer.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x03-python-data_structures/0-print_list_integer.py): A  function that `prints all integers of a list`.
    *  Assume that the list `only contains integers`
<pre>
Constraints : 
Not allowed to import any module
Not allowed to cast integers into strings
Have to use str.format() to print integers
</pre>
### 1. Secure access to an element in a list
* [1-element_at.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x03-python-data_structures/1-element_at.py): A function that retrieves an element from a list like in C.
  * If `idx is negative`, the function should return `None`
  * If `idx is out of range` (> of number of element in my_list), the function should return `None` 
### 2. Replace element
*  [2-replace_in_list.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x03-python-data_structures/2-replace_in_list.py): A function that replaces an element of a list at a specific position (like in C).
   * If idx is negative, the function should not modify anything, and returns the original list
   * If idx is out of range (> of number of element in my_list), the function should not modify anything, and returns the original list 
  <pre>
  Constraints:
  
  Not allowed to import any module
  Not allowed to import any module
  </pre>
