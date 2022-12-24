# <pre> Python - if/else, loops, functions </pre>
This project focuses on mastering the importance of indentation and how to use the if and if ... else statements. It provides practice cases to master the while and for loops, the break and continues statements, and pass statement. range and diving into functions in Python are also part of this project. It also focuses on understanding scope of variables, understanding traceback, and how to use arithmetic operators.


## <pre> Function prototypes    <img src="https://user-images.githubusercontent.com/107026397/209424557-72ec9e7b-8f5a-4c69-9136-2629ca6d2ab0.svg" width = 3% height= 3%> </pre>
| Files  | Prototypes |
| ------------- | ------------- |
|7-islower.py  | def islower(c):|
|8-uppercase.py| def uppercase(str):|
|9-print_last_digit.py | def print_last_digit(number):|
|10-add.py  | def add(a, b):  |
| 11-pow.py | def pow(a, b):  |
| 12-fizzbuzz.py | def fizzbuzz():  |
| 13-insert_number.c | listint_t *insert_node(listint_t **head, int number);  |
| 101-remove_char_at.py  | def remove_char_at(str, n): |
| 102-magic_calculation.py | def magic_calculation(a, b, c): |

## <pre> Tasks   <img src="https://user-images.githubusercontent.com/107026397/209425131-1d190ca6-b53b-49a9-b00a-6d697c9e4473.svg" height=3% width=3%></pre>
### 0. Positive anything is better than negative nothing
* [0-positive_or_negative.py]( https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x01-python-if_else_loops_functions/0-positive_or_negative.py): Python script that assigns random signed number to the variable number each time it is executed. It prints whether the number stored in the variable number is positive or negative or zero.
* The output of the program is:
    * The number, followed by
        * if the number is greater than 0: `is positive`
        * if the number is 0: `is zero`
        * if the number is less than 0: `is negative`
    * followed by a new line
* [Source-code](https://github.com/holbertonschool/0x01.py/blob/master/0-positive_or_negative_py)
### 1. The last digit
* [1-last_digit.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x01-python-if_else_loops_functions/1-last_digit.py): Python script that assign a random signed number to the variable number each time it is executed. It also  print the last digit of the number stored in the variable number.
* The output of the program is:
   * the string `Last digit of is`, followed by the `last digit of number`, followed by
      * if the last digit is greater than 5: the string and `is greater than 5`
      * if the last digit is 0: the string and `is 0`
      * if the last digit is less than 6 and not 0: the string and `is less than 6 and not 0`
   * followed by a new line
* [Source-code](https://github.com/holbertonschool/0x01.py/blob/master/1-last_digit_py)
### 2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game
* [2-print_alphabet.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x01-python-if_else_loops_functions/2-print_alphabet.py): Python script  that prints the ASCII alphabet, in lowercase, not followed by a new line.
 <pre  text-align= center> abcdefghijklmnopqrstuvwxyz</pre>
### 3. When I was having that alphabet soup, I never thought that it would pay off
* [3-print_alphabt.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x01-python-if_else_loops_functions/3-print_alphabt.py): Python program that prints  the ASCII alphabet, in lowercase, not followed by a new line. 
* The program prints all letters except `q` and `e`
<pre>abcdfghijklmnoprstuvwxyz</pre>
### 4. Hexadecimal printing
* [4-print_hexa.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x01-python-if_else_loops_functions/4-print_hexa.py): Python script that prints all numbers from 0 to 98 in decimal and in hexadecimal.
<pre>0 = 0x0
1 = 0x1
2 = 0x2
3 = 0x3
4 = 0x4
5 = 0x5
6 = 0x6
7 = 0x7
8 = 0x8
9 = 0x9
10 = 0xa
11 = 0xb
12 = 0xc
13 = 0xd
14 = 0xe
15 = 0xf
16 = 0x10
17 = 0x11
18 = 0x12
...
96 = 0x60
97 = 0x61
98 = 0x62</pre>
### 5. 00...99
*[5-print_comb2.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x01-python-if_else_loops_functions/5-print_comb2.py): Python script that prints o to 99.
<pre>00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99</pre>
### 6. Inventing is a combination of brains and materials. The more brains you use, the less material you need
* [6-print_comb3.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x01-python-if_else_loops_functions/6-print_comb3.py): Python script that prints all possible different combinations of two digits.
      * Numbers must be separated by ,, followed by a space
      * The two digits must be different
         * Note: 01 and 10 are considered the same combination of the two digits 0 and 1
      * The last number should be followed by a new line
   <pre> 01, 02, 03, 04, 05, 06, 07, 08, 09, 12, 13, 14, 15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28, 29, 34, 35, 36, 37, 38, 39, 45, 46, 47, 48, 49, 56, 57, 58, 59, 67, 68, 69, 78, 79, 89</pre> 
   

