# <pre> Python - Test-driven development </pre>
This project aims at mastering tests. And explains how to use Docstrings to create tests. In addition, shows the importance of documentation for each module and function
## <pre> Function prototypes    <img src="https://user-images.githubusercontent.com/107026397/209424557-72ec9e7b-8f5a-4c69-9136-2629ca6d2ab0.svg" width = 3% height= 3%> </pre>
| Files  | Prototypes |
| ------------- | ------------- |
|0-add_integer.py| def add_integer(a, b=98):|
|2-matrix_divided.py|def matrix_divided(matrix, div):|
|3-say_my_name.py|def say_my_name(first_name, last_name=""):|
|4-print_square.py|def print_square(size):|
|6-max_integer.py|def max_integer(list=[]):|
## <pre> Tasks   <img src="https://user-images.githubusercontent.com/107026397/209425131-1d190ca6-b53b-49a9-b00a-6d697c9e4473.svg" height=3% width=3%></pre>
### 0. Integers addition
* [0-add_integer.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x07-python-test_driven_development/0-add_integer.py): 
  * a and b must be integers or floats, otherwise raise a TypeError exception with the message a must be an integer or b must be an integer.
  * a and b must be first casted to integers if they are float.
  * Returns an integer: the addition of a and b
  * [0-add_integer.txt](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x07-python-test_driven_development/tests/0-add_integer.txt): Test for the function 0-add_integer.py.
<pre>
Constraints: Not allowed to import any module.
</pre>
### 1. Divide a matrix
* [2-matrix_divided.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x07-python-test_driven_development/2-matrix_divided.py): 
 * matrix must be a list of lists of integers or floats, otherwise raise a TypeError exception with the message matrix must be a matrix (list of lists) of integers/floats
 * Each row of the matrix must be of the same size, otherwise raise a TypeError exception with the message Each row of the matrix must have the same size
 * div must be a number (integer or float), otherwise raise a TypeError exception with the message div must be a number
 * div can???t be equal to 0, otherwise raise a ZeroDivisionError exception with the message division by zero
 * All elements of the matrix should be divided by div, rounded to 2 decimal places
 * Returns a new matrix
* [2-matrix_divided.txt](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x07-python-test_driven_development/tests/2-matrix_divided.txt): Test for the function in 2-matrix_divided.py.
 <pre>
Constraints: Not allowed to import any module.
</pre>
### 2. Say my name
* [3-say_my_name.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x07-python-test_driven_development/3-say_my_name.py): A function that prints My name is first name last name
  * first_name and last_name must be strings otherwise, raise a TypeError exception with the message first_name must be a string or last_name must be a string
  * [3-say_my_name.txt](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x07-python-test_driven_development/tests/3-say_my_name.txt) : Tests for the function in 3-say_my_name.py
 <pre>
Constraints: Not allowed to import any module.
</pre> 
### 3. Print square
* [4-print_square.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x07-python-test_driven_development/4-print_square.py):  a function that prints a square with the character #.
  * size is the size length of the square
  * size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
  * If size is less than 0, raise a ValueError exception with the message size must be >= 0
  * If size is a float and is less than 0, raise a TypeError exception with the message size must be an integer
<pre>
Constraints: Not allowed to import any module.
</pre> 
### 5. Max integer - Unittest
* [6-max_integer_test.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x07-python-test_driven_development/tests/6-max_integer_test.py): 
  *  file should be inside a folder tests.
  *  Have to use the unittest module.
  *  Test file should be python files (extension: .py)
  *  Test file should be executed by using this command: python3 -m unittest tests.6-max_integer_test
 
 


