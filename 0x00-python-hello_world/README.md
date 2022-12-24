# <pre>Python - Hello, World</pre>
This project focuses on mastering how to use the Python interpreter, how to print text and variables using print, how to use strings, how to implement indexing and slicing, and how to implement the official Python coding style.
## <pre>Function Prototypes   <img src="https://user-images.githubusercontent.com/107026397/209423040-0ba70fc0-8862-492e-944b-fa10de86e407.svg" width=3% height=3%/></pre>
| File  | Prototype |
| ------------- | ------------- |
| 10-check_cycle.c  | int check_cycle(listint_t *list);  |
| 102-magic_calculation.py  | def magic_calculation(a, b);  |

## <pre> Tasks   <img src="https://user-images.githubusercontent.com/107026397/209345588-c8cc3382-31c2-417b-888a-666928ab0e1d.svg" width=3% height=3%/></pre>
### 0. Run Python file <br>
   * [0-run](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x00-python-hello_world/0-run) : Shell Script that runs Python script. The Python file name will be saved in the environment variable `$PYFILE`.
### 1. Run inline <br>
  * [1-run_inline](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x00-python-hello_world/1-run_inline) : Shell Script that runs Python script. The Python code will be saved in the environment variable `$PYCODE`.
### 2. Hello, print <br>
  * [2-print.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x00-python-hello_world/2-print.py): Python script that prints exactly `Programming is like building a multilingual puzzle`, followed by a new line.
### 3. Print integer <br>
  * [3-print_number.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x00-python-hello_world/3-print_number.py): Print the integer stored in the variable number, followed by `Battery street`, followed by a new line.<br>
  * [Source-code](https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py)
### 4. Print float <br>
  * [4-print_float.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x00-python-hello_world/4-print_float.py) : Print the float stored in the variable number with a precision of 2 digits.
### 5. Print string <br>
  * [5-print_string.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x00-python-hello_world/5-print_string.py) : Print 3 times a string stored in the variable str, followed by its first 9 characters. <br>
  * [Source-code](https://github.com/holbertonschool/0x00.py/blob/master/5-print_string.py)
### 6. Play with strings <br>
  * [6-concat.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x00-python-hello_world/6-concat.py) : Print `Welcome to Holberton School!`.
  * [Source-code](https://github.com/holbertonschool/0x00.py/blob/master/6-concat.py)
### 7. Copy - Cut - Paste <br>
  * [7-edges.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x00-python-hello_world/7-edges.py) : Print sliced string variable<br>
    * word_first_3 should contain the first 3 letters of the variable word.<br>
    * word_last_2 should contain the last 2 letters of the variable word.<br>
    * word_last_2 should contain the last 2 letters of the variable word.<br>
   * [Source code](https://github.com/holbertonschool/0x00.py/blob/master/7-edges.py)
### 8. Create a new sentence <br>
  * [8-concat_edges.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x00-python-hello_world/8-concat_edges.py) : Print `object-oriented programming with Python`.<br>
  * [Source-code](https://github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py)
### 9. Easter Egg<br>
  * [9-easter_egg.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x00-python-hello_world/9-easter_egg.py): Write a `Python script that prints “The Zen of Python”, by TimPeters`, followed by a new line.
### 10. Linked list cycle <br>
  * [10-check_cycle.c](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x00-python-hello_world/10-linked_lists.c): Function that checks if a linked list contains a cycle.
  * [lists.h](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x00-python-hello_world/lists.h): Header file for 10-check_cyle.c.
  * 
### 11. Hello, write <br>
  * [100-write.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x00-python-hello_world/100-write.py) :  Python script that prints exactly `and that piece of art is useful - Dora Korpar, 2015-10-19`, followed by a new line.
### 12. Compile <br>
  * [101-compile](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x00-python-hello_world/101-compile) : A script that compiles a Python script file. The output filename is $PYFILEc
### 102-magic_calculation.py
  * [102-magic_calculation.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x00-python-hello_world/102-magic_calculation.py) :  Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:
 <pre>3           0 LOAD_CONST               1 (98)
                  3 LOAD_FAST                0 (a)
                  6 LOAD_FAST                1 (b)
                  9 BINARY_POWER
                 10 BINARY_ADD
                 11 RETURN_VALUE
 </pre>
