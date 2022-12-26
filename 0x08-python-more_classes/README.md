# <pre> Python - More Classes and Objects </pre>
This project is a continuation from previous project Python classes. This project further deep dives in to Data Abstraction, Data Encapsulation, Information Hiding and  property. Magic method __str__ and __repr__ are also discussed here. We also learned about class method and static method.
## <pre> Tasks   <img src="https://user-images.githubusercontent.com/107026397/209425131-1d190ca6-b53b-49a9-b00a-6d697c9e4473.svg" height=3% width=3%></pre>
### 0. Simple rectangle
* [0-rectangle.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x08-python-more_classes/0-rectangle.py):  An empty class Rectangle that defines a rectangle:
<pre>
Constraint: Not allowed to import any module
</pre>
### 1. Real definition of a rectangle
* [1-rectangle.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x08-python-more_classes/1-rectangle.py): a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
    * Private instance attribute: width:
        * Property def width(self): to retrieve it
        * Property setter def width(self, value): to set it:
            * width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
            * if width is less than 0, raise a ValueError exception with the message width must be >= 0
    * Private instance attribute: height:
      * Property def height(self): to retrieve it
      * Property setter def height(self, value): to set it:
          * Height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
          * if height is less than 0, raise a ValueError exception with the message height must be >= 0
    * Instantiation with optional width and height: def __init__(self, width=0, height=0):
  <pre>
  Constraint: Not allowed to import any module
  </pre>
  ### 2. Area and Perimeter
  * [2-rectangle.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x08-python-more_classes/2-rectangle.py): a class Rectangle that defines a rectangle by: (based on 1-rectangle.py)
      * Private instance attribute: width:
           * property def width(self): to retrieve it
           * property setter def width(self, value): to set it:
                * width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
                * if width is less than 0, raise a ValueError exception with the message width must be >= 0
      * Private instance attribute: height:
           * Property def height(self): to retrieve it
           * Property setter def height(self, value): to set it:
                * Height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
                * if height is less than 0, raise a ValueError exception with the message height must be >= 0
      * Instantiation with optional width and height: def __init__(self, width=0, height=0):
      * Public instance method: def area(self): that returns the rectangle area
      * Public instance method: def perimeter(self): that returns the rectangle perimeter:
           * if width or height is equal to 0, perimeter is equal to 0
<pre>
  Constraint: Not allowed to import any module
</pre>
### 3. String representation
* [3-rectangle.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x08-python-more_classes/3-rectangle.py): a class Rectangle that defines a rectangle by: (based on 2-rectangle.py)
   * Private instance attribute: width:
      * property def width(self): to retrieve it
      * property setter def width(self, value): to set it:
         * width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
         * if width is less than 0, raise a ValueError exception with the message width must be >= 0
   * Private instance attribute: height:
      * property def height(self): to retrieve it
      * property setter def height(self, value): to set it:
         * height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
         * if height is less than 0, raise a ValueError exception with the message height must be >= 0
   * Instantiation with optional width and height: def __init__(self, width=0, height=0):
   * Public instance method: def area(self): that returns the rectangle area
   * Public instance method: def perimeter(self): that returns the rectangle perimeter:
      * if width or height is equal to 0, perimeter has to be equal to 0
   * print() and str() should print the rectangle with the character #: (see example below)
      * if width or height is equal to 0, return an empty string
<pre>
  Constraint: Not allowed to import any module
</pre>
### 4. Eval is magic
* [4-rectangle.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x08-python-more_classes/4-rectangle.py): a class Rectangle that defines a rectangle by: (based on 3-rectangle.py)
     * Private instance attribute: width:
         * Property def width(self): to retrieve it
         * Property setter def width(self, value): to set it:
              * width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
              * if width is less than 0, raise a ValueError exception with the message width must be >= 0
     * Private instance attribute: height:
         * property def height(self): to retrieve it
         * property setter def height(self, value): to set it:
            * height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
            * if height is less than 0, raise a ValueError exception with the message height must be >= 0
     * Instantiation with optional width and height: def __init__(self, width=0, height=0):
     * Public instance method: def area(self): that returns the rectangle area
     * Public instance method: def perimeter(self): that returns the rectangle perimeter:
         * if width or height is equal to 0, perimeter has to be equal to 0
     * print() and str() should print the rectangle with the character #: (see example below)
         * if width or height is equal to 0, return an empty string
     * repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval() (see example below)
<pre>
  Constraint: Not allowed to import any module
</pre>
### 5. Detect instance deletion
* [5-rectangle.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x08-python-more_classes/5-rectangle.py): a class Rectangle that defines a rectangle by: (based on 4-rectangle.py)
   * Private instance attribute: width:
      * property def width(self): to retrieve it
      * property setter def width(self, value): to set it:
         * width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
         * if width is less than 0, raise a ValueError exception with the message width must be >= 0
   * Private instance attribute: height:
      * property def height(self): to retrieve it
      * property setter def height(self, value): to set it:
         * height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
         * if height is less than 0, raise a ValueError exception with the message height must be >= 0
   * Instantiation with optional width and height: def __init__(self, width=0, height=0):
   * Public instance method: def area(self): that returns the rectangle area
   * Public instance method: def perimeter(self): that returns the rectangle perimeter:
      * if width or height is equal to 0, perimeter has to be equal to 0
   * print() and str() should print the rectangle with the character #:
      * if width or height is equal to 0, return an empty string
   * repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval()
   * Print the message Bye rectangle... (... being 3 dots not ellipsis) when an instance of Rectangle is deleted.
 <pre>
  Constraint: Not allowed to import any module
</pre>
### 6. How many instances
* [6-rectangle.py](https://github.com/Bezawork-pr/alx-higher_level_programming/blob/master/0x08-python-more_classes/6-rectangle.py): A class Rectangle that defines a rectangle by: (based on 5-rectangle.py)
   * Private instance attribute: width:
      * Property def width(self): to retrieve it
      * Property setter def width(self, value): to set it:
         * width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
         * if width is less than 0, raise a ValueError exception with the message width must be >= 0
   * Private instance attribute: height:
      * property def height(self): to retrieve it
      * property setter def height(self, value): to set it:
         * height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
         * if height is less than 0, raise a ValueError exception with the message height must be >= 0
   * Public class attribute number_of_instances:
      * Initialized to 0
      * Incremented during each new instance instantiation
      * Decremented during each instance deletion
   * Instantiation with optional width and height: def __init__(self, width=0, height=0):
   * Public instance method: def area(self): that returns the rectangle area
   * Public instance method: def perimeter(self): that returns the rectangle perimeter:
      * if width or height is equal to 0, perimeter has to be equal to 0
   * print() and str() should print the rectangle with the character #:
      * if width or height is equal to 0, return an empty string
   * repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval()
   * Print the message Bye rectangle... (... being 3 dots not ellipsis) when an instance of Rectangle is deleted
 <pre>
  Constraint: Not allowed to import any module
</pre>
