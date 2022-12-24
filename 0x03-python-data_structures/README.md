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
*  [2-replace_in_list.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x03-python-data_structures/2-replace_in_list.py): A function that `replaces an element of a list at a specific position` (like in C).
   * If `idx is negative`, the function should not modify anything, and `returns the original list`
   * If `idx is out of range` (> of number of element in my_list), the function should not modify anything, and `returns the original list` 
  <pre>
  Constraints:
  
  Not allowed to import any module
  Not allowed to import any module</pre>
### 3. Print a list of integers... in reverse!
* [3-print_reversed_list_integer.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x03-python-data_structures/3-print_reversed_list_integer.py): A function that prints all integers of a list, in reverse order.
   * Format: one integer per line.
   * Can assume that the list only contains integers
<pre>
Constraints:

Not allowed to cast integers into strings
Have to use str.format() to print integers
</pre>
### 4. Replace in a copy
* [4-new_in_list.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x03-python-data_structures/4-new_in_list.py): A function that replaces an element in a list at a specific position without modifying the original list (like in C).
      * If idx is negative, the function should return a copy of the original list
      * If idx is out of range (> of number of element in my_list), the function should return a copy of the original list 
<pre>
Constraints:

Not allowed to import any module
Not allowed to use try/except
</pre>
### 5. Can you C me now?
* [5-no_c.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x03-python-data_structures/5-no_c.py): A function that removes all characters c and C from a string.
   * function should return the new string
 <pre>
Constraints:

Not allowed to import any module
Not allowed to use str.replace()
 </pre>
 ### 6. Lists of lists = Matrix
 * [6-print_matrix_integer.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x03-python-data_structures/6-print_matrix_integer.py): A function that prints a matrix of integers.
 <pre>
Constraints:

Not allowed to import any module
Can assume that the list only contains integers
Not allowed to cast integers into strings
Have to use str.format() to print integers
</pre>
###  7. Tuples addition
* [7-add_tuple.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x03-python-data_structures/7-add_tuple.py): A function that adds 2 tuples.
   * Returns a tuple with 2 integers:
      * The first element is the addition of the first element of each argument
      * The second element is the addition of the second element of each argument
   * If a tuple is smaller than 2,  value 0 is used for each missing integer.
   * If a tuple is bigger than 2, only the first 2 integers is used.
   * Can assume that the two tuples will only contain integers.
 <pre>
 Constraints: Not allowed to import any module
 </pre>
 ### 8. More returns!
  * [8-multiple_returns.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x03-python-data_structures/8-multiple_returns.py): A function that returns a tuple with the length of a string and its first character.
      * If the sentence is empty, the first character should be equal to None
 <pre>
 Constraints:
 
Not allowed to import any module
</pre>
### 9. Find the max
* [9-max_integer.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x03-python-data_structures/9-max_integer.py): A function that finds the biggest integer of a list.
     * If the list is empty, return None.
     * Assume that the list only contains integers.
<pre>
Not allowed to import any module
Not allowed to use the builtin max()
</pre>
### 10. Only by 2
 * [10-divisible_by_2.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x03-python-data_structures/10-divisible_by_2.py): A function that finds all multiples of 2 in a list.
   * Return a new list with `True` or `False`, depending on whether the integer at the same position in the original list is a multiple of 2
   * The new list should have the `same size` as the original list.
<pre>
Constraints:

Not allowed to import any module
</pre>
### 11. Delete at
 * [11-delete_at.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x03-python-data_structures/11-delete_at.py): A function that deletes the item at a specific position in a list.
      * If `idx is negative or out of range`, nothing change (returns the `same list`) 
<pre>
Constraints:
Not allowed to use pop()
Not allowed to import any module
</pre>  
### 12. Switch
* [12-switch.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x03-python-data_structures/12-switch.py):  Switch value of a and b
*  [Source-code](https://github.com/holbertonschool/0x03.py/blob/master/12-switch_py)
<pre>
Constraints:
program should be exactly 5 lines long
</pre>  
### 13. Linked list palindrome
*  [13-is_palindrome.c](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x03-python-data_structures/13-is_palindrome.c): A function in C that checks if a singly linked list is a palindrome.
*  Return: 0 if it is not a palindrome, 1 if it is a palindrome.
*  An empty list is considered a palindrome.
   *  [linked_lists.c](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x03-python-data_structures/linked_lists.c): This file contains print function, add node function and free list function.
   *  
 


         


