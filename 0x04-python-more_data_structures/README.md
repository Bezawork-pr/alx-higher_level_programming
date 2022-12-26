# <pre> Python - More Data Structures: Set, Dictionary </pre>
This project targets mastering how to use sets, how to iterate through sets, how to use dictionaries and how to iterate through dictionaries. In addition, it also covers lambda function, map, reduce and filter functions.
## <pre> Function prototypes    <img src="https://user-images.githubusercontent.com/107026397/209424557-72ec9e7b-8f5a-4c69-9136-2629ca6d2ab0.svg" width = 3% height= 3%> </pre>
| Files  | Prototypes |
| ------------- | ------------- |
| 0-square_matrix_simple.py| def square_matrix_simple(matrix=[]):|
|1-search_replace.py|def search_replace(my_list, search, replace):|
|2-uniq_add.py | def uniq_add(my_list=[]):|
|3-common_elements.py |def common_elements(set_1, set_2): |
|4-only_diff_elements.py  |def only_diff_elements(set_1, set_2): |
|5-number_keys.py|def number_keys(a_dictionary):|
|6-print_sorted_dictionary.py|def print_sorted_dictionary(a_dictionary):|
|7-update_dictionary.py| def update_dictionary(a_dictionary, key, value):|
|8-simple_delete.py|def simple_delete(a_dictionary, key=""):|
|9-multiply_by_2.py|def multiply_by_2(a_dictionary):|
|10-best_score.py|def best_score(a_dictionary):|
|11-multiply_list_map.py|def multiply_list_map(my_list=[], number=0):|
|12-roman_to_int.py|def roman_to_int(roman_string):|
|100-weight_average.py|def weight_average(my_list=[]):|
|101-square_matrix_map.py| def square_matrix_map(matrix=[]): |
|102-complex_delete.py|def complex_delete(a_dictionary, value):|

## <pre> Tasks   <img src="https://user-images.githubusercontent.com/107026397/209425131-1d190ca6-b53b-49a9-b00a-6d697c9e4473.svg" height=3% width=3%></pre>
### 0. Squared simple
* [0-square_matrix_simple.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/0-square_matrix_simple.py): A function that computes the square value of all integers of a matrix.
  * Returns a new matrix:
    * Same size as matrix
    * Each value is the square of the value of the input  
<pre>
Constraints:

Initial matrix should not be modified.
Not allowed to import any module.
</pre>
### 1. Search and replace
* [1-search_replace.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/1-search_replace.py): A function that replaces all occurrences of an element by another in a new list.
   * my_list is the initial list
   * search is the element to replace in the list
   * replace is the new element
<pre>
Constraints:

Not allowed to import any module.
</pre>
### 2. Unique addition
* [2-uniq_add.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/2-uniq_add.py): A function that adds all unique integers in a list (only once for each integer).
<pre>
Constraints:

Not allowed to import any module.
</pre>
### 3. Present in both
* [3-common_elements.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/3-common_elements.py): A function that returns a set of common elements in two sets.
<pre>
Constraints:

Not allowed to import any module.
</pre>
### 4. Only differents
* [4-only_diff_elements.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/4-only_diff_elements.py): A function that returns a set of all elements present in only one set.
<pre>
Constraints:

Not allowed to import any module.
</pre>
### 5. Number of keys
* [5-number_keys.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/5-number_keys.py): A function that returns the number of keys in a dictionary.
<pre>
Constraints:

Not allowed to import any module.
</pre>
### 6. Print sorted dictionary
* [6-print_sorted_dictionary.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/6-print_sorted_dictionary.py): A function that prints a dictionary by ordered keys.
   * Keys are sorted by alphabetic order.
   * Sorted keys of the first level.
   * Dictionary values can have any type
<pre>
Constraints:

Not allowed to import any module.
</pre>
### 7. Update dictionary
* [7-update_dictionary.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/7-update_dictionary.py): A function that replaces or adds key/value in a dictionary.
   * Assumption
     * key argument will be always a string.
     * value argument will be any type
   * If a key exists in the dictionary, the value will be replaced
   * If a key doesn’t exist in the dictionary, it will be created
<pre>
Constraints: Not allowed to import any module.
</pre>
### 8. Simple delete by key
* [8-simple_delete.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/8-simple_delete.py): A function that deletes a key in a dictionary.
   * Assumption
      * key argument will be always a string
   * If a key doesn’t exist, the dictionary won’t change
<pre>
Constraints: Not allowed to import any module.
</pre> 
### 9. Multiply by 2
* [9-multiply_by_2.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/9-multiply_by_2.py): A function that returns a new dictionary with all values multiplied by 2.
   * Assumption
      * All values are only integers 
   * Returns a new dictionary
<pre>
Constraints: Not allowed to import any module.
</pre> 
### 10. Best score
* [10-best_score.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/10-best_score.py): A function that returns a key with the biggest integer value.
   * Assumption:
     * All values are only integers.
   * If no score found, returns None 
 <pre>
Constraints: Not allowed to import any module.
</pre> 
### 11. Multiply by using map
* [11-multiply_list_map.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/11-multiply_list_map.py): A function that returns a list with all values multiplied by a number without using any loops.
   * Returns a new list:
      * Same length as my_list
      * Each value should be multiplied by number
   * Initial list is not modified.
   <pre>
Constraints:

Have to use map.
Not allowed to import any module.
</pre>
### 12. Roman to Integer
* [12-roman_to_int.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/12-roman_to_int.py): A function  that converts a Roman numeral to an integer.
   * Assumption:
      * number will be between 1 to 3999.
   *  Returns an integer.
   *  If the roman_string is not a string or None, returns 0
 ### 13. Weighted average!
 * [100-weight_average.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/100-weight_average.py): A function that returns the weighted average of all integers tuple (<score>, <weight>)
    * Returns 0 if the list is empty.
  <pre>
Constraints: Not allowed to import any module.
</pre>
 ### 14. Squared by using map
 [101-square_matrix_map.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/101-square_matrix_map.py): A function that computes the square value of all integers of a matrix using map.
 * Returns a new matrix:
 
 


 
       






[]()
[]()



   


