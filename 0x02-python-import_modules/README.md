# <pre> Python - import & modules </pre>
This project is targeted at mastering how to import functions from another file and how to use those imported functions. Another focus of the project is how to create a module and how to use  built-in function dir(). Other topics dealt with are preventing code in your script from being executed when imported and taking command line arguments with your Python programs.
## <pre> Function prototypes    <img src="https://user-images.githubusercontent.com/107026397/209424557-72ec9e7b-8f5a-4c69-9136-2629ca6d2ab0.svg" width = 3% height= 3%> </pre>
| Files  | Prototypes |
| ------------- | ------------- |
| 0-add.py|def add(a, b): |
|102-magic_calculation.py | def magic_calculation(a, b):|
## <pre> Tasks   <img src="https://user-images.githubusercontent.com/107026397/209425131-1d190ca6-b53b-49a9-b00a-6d697c9e4473.svg" height=3% width=3%></pre>
### 0. Import a simple function from a simple file mandatory
* [0-add.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x02-python-import_modules/0-add.py): A program that imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3
* import function from [add_0.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x02-python-import_modules/add_0.py)
<pre>
Constrains:
Can only use the word add_0 once in your code
Not allowed to use * for importing or __import__
Code should not be executed when imported 
</pre>
### 1. My first toolbox!
* [1-calculation.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x02-python-import_modules/1-calculation.py): A program that imports functions from the file calculator_1.py, does some Maths, and prints the result.
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
 * [2-args.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x02-python-import_modules/2-args.py):A program that prints the number of and the list of its arguments.
 * The output is:
  * Number of argument(s) followed by argument (if number is one) or arguments (otherwise), followed by
  * `:` (or `.` if no arguments were passed) followed by
  * a new line, followed by (if at least one argument),
  * one line per argument:
    * the position of the argument (starting at 1) followed by :, followed by the argument value and a new line
 <pre>
 Code should not be executed when imported.
 </pre>

