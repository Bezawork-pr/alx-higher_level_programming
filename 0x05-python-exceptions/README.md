# <pre> Python - Exceptions </pre>
This projects aims at mastering the difference between errors and exceptions, how to use exceptions, how to correctly handle exceptions, and understanding the purpose of exceptions. In addition, it dives into understanding the reason behind catching exceptions, and how to raise a builtin exception. 
## <pre> Function prototypes    <img src="https://user-images.githubusercontent.com/107026397/209424557-72ec9e7b-8f5a-4c69-9136-2629ca6d2ab0.svg" width = 3% height= 3%> </pre>
| Files  | Prototypes |
| ------------- | ------------- |
|0-safe_print_list.py| def safe_print_list(my_list=[], x=0):|
|1-safe_print_integer.py|def safe_print_integer(value): |
|2-safe_print_list_integers.py|def safe_print_list_integers(my_list=[], x=0):|
|3-safe_print_division.py|def safe_print_division(a, b):|
|4-list_division.py|def list_division(my_list_1, my_list_2, list_length):|
|5-raise_exception.py|def raise_exception():|
|6-raise_exception_msg.py|def raise_exception_msg(message=""):|
|100-safe_print_integer_err.py|def safe_print_integer_err(value):|
|101-safe_function.py|def safe_function(fct, *args):|
|102-magic_calculation.py|def magic_calculation(a, b):|
## <pre> Tasks   <img src="https://user-images.githubusercontent.com/107026397/209425131-1d190ca6-b53b-49a9-b00a-6d697c9e4473.svg" height=3% width=3%></pre>
### 0. Safe list printing
* [0-safe_print_list.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x05-python-exceptions/0-safe_print_list.py): A function that prints x elements of a list.
      * Assumption:
            * my_list can contain any type (integer, string, etc.)
            * x represents the number of elements to print
            * x can be bigger than the length of my_list
      * Returns the real number of elements printed
<pre>
Constraints:

Have to use try: / except.
Not allowed to import any module.
Not allowed to use len()
</pre>




