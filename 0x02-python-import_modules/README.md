# <pre> Python - import & modules </pre>
This project is targeted at mastering how to import functions from another file and how to use those imported functions. Another focus of the project is how to create a module and how to use  built-in function dir(). Other topics dealt with are preventing code in your script from being executed when imported and taking command line arguments with your Python programs.
## <pre> Function prototypes    <img src="https://user-images.githubusercontent.com/107026397/209424557-72ec9e7b-8f5a-4c69-9136-2629ca6d2ab0.svg" width = 3% height= 3%> </pre>
| Files  | Prototypes |
| ------------- | ------------- |
| 0-add.py|def add(a, b): |
|102-magic_calculation.py | def magic_calculation(a, b):|
## <pre> Tasks   <img src="https://user-images.githubusercontent.com/107026397/209425131-1d190ca6-b53b-49a9-b00a-6d697c9e4473.svg" height=3% width=3%></pre>
### 0. Import a simple function from a simple file mandatory
* [0-add.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x02-python-import_modules/0-add.py): A program that imports the function def add(a, b): from the file [add_0.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x02-python-import_modules/add_0.py) and prints the result of the addition 1 + 2 = 3

<pre>
Constrains:

Can only use the word add_0 once in your code
Not allowed to use * for importing or __import__
Code should not be executed when imported 
</pre>
### 1. My first toolbox!
* [1-calculation.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x02-python-import_modules/1-calculation.py): A program that imports functions from the file  [calculator_1.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x02-python-import_modules/calculator_1.py), does some Maths, and prints the result.
  * define:
    * the value 10 to a variable a
    * the value 5 to a variable b
     * and use those two variables only, as arguments when calling functions (including print)
<pre>
Constraints:

Use the function print more than 4 times.
The word calculator_1 should be used only once in file.
Not allowed to use * for importing or __import__
Code should not be executed when imported
</pre>
### 2. How to make a script dynamic!
 * [2-args.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x02-python-import_modules/2-args.py): A program that prints the number of and the list of its arguments.
 * The output is:
    * Number of argument(s) followed by argument (if number is one) or arguments (otherwise), followed by
    * `:` (or `.` if no arguments were passed) followed by
    * a new line, followed by (if at least one argument),
    * one line per argument:
    * the position of the argument (starting at 1) followed by :, followed by the argument value and a new line
 <pre>
 Constraint: Code should not be executed when imported.
 </pre>
### 3. Infinite addition
*  [3-infinite_add.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x02-python-import_modules/3-infinite_add.py): A program that prints the result of the addition of all arguments, followed by a new line.
<pre>
 Constraint: Code should not be executed when imported.
</pre>
### 4. Who are you?
*  [4-hidden_discovery.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x02-python-import_modules/4-hidden_discovery.py): A program that prints all the names defined by the compiled module  [hidden_4.pyc](https://github.com/holbertonschool/0x02.py/raw/master/hidden_4.pyc)(please download it locally).
    *  print one name per line, in alpha order.
    *  print only names that do not start with __
<pre>
 Constraint: Code should not be executed when imported.</pre>
### 5. Everything can be imported
* [5-variable_load.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x02-python-import_modules/5-variable_load.py): A program that imports the variable a from the file  [variable_load_5.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x02-python-import_modules/variable_load_5.py) and prints its value.
<pre>
Constraint:

Not allowed to use * for importing or __import__
Code should not be executed when imported
</pre>
### 6. Build my own calculator!
* [100-my_calculator.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x02-python-import_modules/100-my_calculator.py): A program that imports all functions from the file calculator_1.py and handles basic operations.
   *  `Usage: ./100-my_calculator.py a operator b`
   *  If the number of arguments is not 3, the program prints:
      * `Usage: ./100-my_calculator.py <a> <operator> <b>` followed with a new line.
      * exit with the value 1
   * operator can be:
     * '+' for addition
     * '-' for subtraction
     * '*' for multiplication
     * '/' for division
   * If the operator is not one of the above:
     * print Unknown operator. Available operators: +, -, * and / followed with a new line
     * exit with the value 1
<pre>
Constraints:

Not allowed to use * for importing or __import__
Code should not be executed when imported
</pre>
### 7. Easy print
* [101-easy_print.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x02-python-import_modules/101-easy_print.py):  A program that prints #pythoniscool, followed by a new line, in the standard output.
<pre>
Not allowed to use print or eval or open or import sys.
</pre>
### 8. ByteCode -> Python #3
*  [102-magic_calculation.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x02-python-import_modules/102-magic_calculation.py): Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:

<pre>
  3           0 LOAD_CONST               1 (0)
              3 LOAD_CONST               2 (('add', 'sub'))
              6 IMPORT_NAME              0 (magic_calculation_102)
              9 IMPORT_FROM              1 (add)
             12 STORE_FAST               2 (add)
             15 IMPORT_FROM              2 (sub)
             18 STORE_FAST               3 (sub)
             21 POP_TOP

  4          22 LOAD_FAST                0 (a)
             25 LOAD_FAST                1 (b)
             28 COMPARE_OP               0 (<)
             31 POP_JUMP_IF_FALSE       94

  5          34 LOAD_FAST                2 (add)
             37 LOAD_FAST                0 (a)
             40 LOAD_FAST                1 (b)
             43 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             46 STORE_FAST               4 (c)

  6          49 SETUP_LOOP              38 (to 90)
             52 LOAD_GLOBAL              3 (range)
             55 LOAD_CONST               3 (4)
             58 LOAD_CONST               4 (6)
             61 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             64 GET_ITER
        >>   65 FOR_ITER                21 (to 89)
             68 STORE_FAST               5 (i)

  7          71 LOAD_FAST                2 (add)
             74 LOAD_FAST                4 (c)
             77 LOAD_FAST                5 (i)
             80 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             83 STORE_FAST               4 (c)
             86 JUMP_ABSOLUTE           65
        >>   89 POP_BLOCK

  8     >>   90 LOAD_FAST                4 (c)
             93 RETURN_VALUE

 10     >>   94 LOAD_FAST                3 (sub)
             97 LOAD_FAST                0 (a)
            100 LOAD_FAST                1 (b)
            103 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
            106 RETURN_VALUE
            107 LOAD_CONST               0 (None)
            110 RETURN_VALUE
</pre>
### 9. Fast alphabet
* [103-fast_alphabet.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x02-python-import_modules/103-fast_alphabet.py): A program that prints the alphabet in uppercase, followed by a new line.
<pre>
Constraints:

* Not allowed to use:
   * Any loops
   * Any conditional statements
   * str.join()
   * Any string literal
   * Any system calls
</pre>
