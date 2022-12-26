# <pre> Python - Classes and Objects </pre>
This projects aims at mastering Object Oriented Programming. The concepts dealt here are class, object, instance and others. Types of attributes are also discused here i.e public, protected and private attributes. The project further explains the Python self for class, and magic functions like __init__ and __dict
## <pre> Tasks   <img src="https://user-images.githubusercontent.com/107026397/209425131-1d190ca6-b53b-49a9-b00a-6d697c9e4473.svg" height=3% width=3%></pre>
### 0. My first square
* [0-square.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x06-python-classes/0-square.py): An empty class Square that defines a square.
<pre>
Constraint: Not allowed to import any module.
</pre>
### 1. Square with size
* [1-square.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x06-python-classes/1-square.py): a class Square that defines a square by: (based on 0-square.py)
  * Private instance attribute: size
  * Instantiation with size (no type/value verification)
<pre>
Constraint: Not allowed to import any module.
</pre>
### 2. Size validation
* [2-square.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x06-python-classes/2-square.py): A class Square that defines a square by:(based on 1-square.py)
  * Private instance attribute: size
  * Instantiation with optional size: def __init__(self, size=0):
    * size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
    * if size is less than 0, raise a ValueError exception with the message size must be >= 0 
<pre>
Constraint: Not allowed to import any module.
</pre>
### 3. Area of a square
* [3-square.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x06-python-classes/3-square.py): A class Square that defines a square by:  (based on 2-square.py)
  * Private instance attribute: size.
  * Instantiation with optional size: def __init__(self, size=0):
    * size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
    * if size is less than 0, raise a ValueError exception with the message size must be >= 0
  * Public instance method: def area(self): that returns the current square area.
<pre>
Constraint: Not allowed to import any module.
</pre>
### 4. Access and update private attribute
* [4-square.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x06-python-classes/4-square.py):  A class Square that defines a square by:(based on 3-square.py)
* Private instance attribute: size.
  * property def size(self): to retrieve it
  * property setter def size(self, value): to set it:
    * size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
    * if size is less than 0, raise a ValueError exception with the message size must be >= 0
  * Instantiation with optional size: def __init__(self, size=0):
  * Public instance method: def area(self): that returns the current square area
<pre>
Constraint: Not allowed to import any module.
</pre>

### 5. Printing a square
* [5-square.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x06-python-classes/5-square.py) : Write a class Square that defines a square by: (based on 4-square.py)
  * Private instance attribute: size:
  * property setter def size(self, value): to set it:
    * size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
    * if size is less than 0, raise a ValueError exception with the message size must be >= 0
  * Instantiation with optional size: def __init__(self, size=0)
  * Public instance method: def area(self): that returns the current square area
  * Public instance method: def my_print(self): that prints in stdout the square with the character #:
    * if size is equal to 0, print an empty line
 <pre>
 Constraint: Not allowed to import any module.
 </pre>
### 6. Coordinates of a square
* [6-square.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x06-python-classes/6-square.py): a class Square that defines a square by: (based on 5-square.py)
  * Private instance attribute: size:
    * property def size(self): to retrieve it
    * property setter def size(self, value): to set it:
      * size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
      * if size is less than 0, raise a ValueError exception with the message size must be >= 0
    * Private instance attribute: position
      * property def position(self): to retrieve it  
      * property setter def position(self, value): to set it:
        * position must be a tuple of 2 positive integers, otherwise raise a TypeError exception with the message position must be a tuple of 2 positive integers
    * Instantiation with optional size and optional position: def __init__(self, size=0, position=(0, 0)):
    * Public instance method: def area(self): that returns the current square area
    * Public instance method: def my_print(self): that prints in stdout the square with the character #:
      * if size is equal to 0, print an empty line
      * position should be use by using space - Don’t fill lines by spaces when position[1] > 0
 <pre> Constraint: Not allowed to import any module.</pre> 
 
