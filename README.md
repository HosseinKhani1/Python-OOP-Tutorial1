# Python-OOP-Tutorial1

This is a very simple code with the goal to practice some of the important object oriented program in python. The main goals are summarized below:

- Defining class to take arbitrary number of arguments
- Representation of instances,
- Inheritance,
- Be able to work with __dic__ as a dictionary that keep track of attributes of instances,
- Sorting dictionaries and define costumize sort method for dictionaries using Lambda expressions.


## The first step: defining class Box 
In order to define an instance of class Box as a "box" in this example, we just consider the point at the top left of the box and the point at the bottom right of the box.

The idea of class Box is to initialize instances of Box either by specifying the x and y coordinates of top-left point and down-right point (in this case four entries), or passing the points top-left and down-right as tuples (in this case two entries). Also we want to enter the entries or arguments by a specific order:

1. If we have four arguments to enter, first we pass the x,y coordinates of top-left point as x1,y1, and then we enter the x,y coordinated of the down-right point as x2,y2. For instance, in our code the instance box is defined as: box=Box(x1=2,x2=3,y1=1,y2=4), and we want to have a representation of the instance with the right ordering of coordinates which means: box is represented by: (2,1),(2,4).

2. In the other way, we should be able to intialize the instance box by passing simply points p1 and p2 to the class. For example, box = Box(p1=(2,3),p2=(1,4)) and the printing result should be: box is represented by (2,3),(1,4). 

Note that, in both cases it does not matter in which order we are going to enter the arguments. As long as we use the write keywords for the arguments (x1, x2, y1, y2 or p1 , p2) for representation we always should have the coordinated of the first point and then the coordinated of second point.

To do so, we have used the prefix operators ** in the definition of __init__ method of class Box. Using such operators in the argument section of a function, specifies that there are an arbitrary number of arguments that can come in. In fact, the prefix asterisk operator, do a kind of unpacking process over the data entered to the function. For more information about it take a look at the unpacking concept in python.

Specially, two asterisk together means that the arguments to the function are accompanied by keywords.

