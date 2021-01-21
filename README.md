# Python-OOP-Tutorial1

This is a very simple code with the goal to practice some of the important object oriented program in python. The main goals are summarized below:

- Defining class to take arbitrary number of arguments
- Representation of instances,
- Inheritance,
- Be able to work with  `__dic__`  as a dictionary that keep track of attributes of instances,
- Sorting dictionaries and define costumize sort method for dictionaries using Lambda expressions.


## The first step: defining class Box 
In order to define an instance of class Box as a "box" in this example, we just consider the point at the top left of the box and the point at the bottom right of the box.

The idea of class Box is to initialize instances of Box either by specifying the x and y coordinates of top-left point and down-right point (in this case four entries), or passing the points top-left and down-right as tuples (in this case two entries). Also we want to enter the entries or arguments by a specific order:

1. If we have four arguments to enter, first we pass the x,y coordinates of top-left point as `x1`,`y1`, and then we enter the x,y coordinated of the down-right point as `x2`,`y2`. For instance, in our code the instance box is defined as: `box=Box(x1=2,x2=3,y1=1,y2=4)`, and we want to have a representation of the instance with the right ordering of coordinates which means: box is represented by: `(2,1) (2,4)`.

2. In the other way, we should be able to intialize the instance box by passing simply points `p1` and `p2` to the class. For example, `box = Box(p1=(2,3),p2=(1,4))` and the printing result should be: box is represented by `(2,3) (1,4)`. 

Note that, in both cases it does not matter in which order we are going to enter the arguments. As long as we use the write keywords for the arguments (x1, x2, y1, y2 or p1 , p2) for representation we always should have the coordinated of the first point and then the coordinated of second point.

To do so, we have used the prefix operators `**` in the definition of `__init__` method of class Box. Using such operators in the argument section of a function, specifies that there are an arbitrary number of arguments that can come in. In fact, the prefix asterisk operator, do a kind of unpacking process over the data entered to the function. For more information about it take a look at the unpacking concept in [here](https://www.python-course.eu/python3_passing_arguments.php). Specially, two asterisk together means that the arguments to the function are accompanied by keywords.

In the code `**coordinates` signals to the `__init__` method that there are an arbitrary number of arguments which are accompanied by the keywords. As we know, the `__dict__` dictionary is responsible to keep track of all of the attributs of instances of class, so one way to specify the attributes of the class is to update the `__dict__` for each instance which is created. This is why I have used `self.__dict__.update(**coordinates)` in the init method.

Also since we assume two modes for entering the arguments (either four arguments or two arguments to be entered), we have considered two conditional statements to manage each one of the cases. In this stage, it is important to note that the variable `coordinates` itself is a dictionary with keys as the keywords entered as arguments and values as the paremeters. For instance, if we initialize the instance `box`using `box=Box(x1=2,x2=3,y1=1,y2=4)` it creates the dictionary `coordinates={'x1': 2, 'x2': 3, 'y1': 1, 'y2': 4}`. So, in the first conditional statements, when there are four arguments we assume that their keywords should be `x1`,`x2`,`y1` and `y2` as indicated in `keyorder`. I do the same for the case that the number of entered arguments are two: `len(coordinates)==2`.

Since the main idea is to represent the instances with a specific order of coordinates (for instance when there are four arguments first I want to represent x1,y1 and then x2 and y2), I have pre-specify the ordering in the list `keyorder` and costumize the sorted method of the dictionary using the lambda expressions:


Since the main idea is to represent the instances with a specific order of coordinates (for instance when there are four arguments first I want to represent x1,y1 and then x2 and y2), I have pre-specify the ordering in the list `keyorder` and costumize the sorted method of the dictionary using the lambda expressions :
`type(self).sortedDic=dict(sorted(self.__dict__.items(), key = lambda i: keyorder.index(i[0])))`. 

This expression simply emphasize that the goal is to sort members of `self.__dict__.items() ` using the index of the first element `i[0]` of item `i` in the list `keyorder`.

The same explanations of valid for the second conditional statement where two arguments are entered to initialize the instance.

## Second step: representation of the instances

In python the method `__str__` is used to have a used-friendly representation of the objects in python. In our specific example this user friendly representation obtained by simply illustrating the coordinates of the points related to instance `box`. In our example, since the number of entered arguments are varied, we manage each one of them using conditional statements. Specially, for the case we have four arguments I have used a format string to position x-coordinate and y-coordinate of each point into an ordered pair `(  ,  )`. By sorting `__dict__` I have got another dictionary `sortedDic` in which the keys are ordered as `{'x1': arg1, 'y1': arg2,'x2': arg3 ,'y2':arg4}`. The challenging part here is that I need every time to pass through two of the consecutinve keys in the dictionary and put them in their right place using the format string. There are different ways to do that, the way that I used is one of the simplest ways that can come to mind. First I have defined a list `temp` which is an ordered list of the keys in the dictionary. Then using a for loop I pass through each element of the list, and at each step I copy the next key  in the variable j using `j=temp[temp.index(i)+1]` (the key is to use +1).in this case I will have for example the key `'x1'` in the variable `i` and the key `y1` in variable `j`. Using the conditional `if i==j` at each iteration I pass the key which is previously copied to variable `j`, in this case after the first iteration where `i` has the value `x1`, in the second iteration it takes the value of `x2`.

## Third step: Inheritance

The last part of the code is a simple inheritance example with the same notions of the last two steps. So I am not going to explain it in detail. However the challenging part in this section is that the class TextBox has an extra attribute text that should be somehow manage it. The idea is that class TextBox is exactly the same as class Box however it includes a text message. Therefore, The attributes of an instance of TextBox should be managed in the init method of class Box, and the attribute text should be treated in the class textbox, this is why in the init method of class TextBox I first verify if there is a text has been passed as a argument to the class TextBox or not (`if "text" in arguments.keys()`) is this is the case, I make a deepcopy of the `arguments` in another dictionary `argument`, and pop the item with the key `'text'` from the `argument`. In fact this is a pre-preparation phase for the `argument` in order to prepate it (by removing "text") and send it to init method of class Box. Note to the use of deepcopy in this example. If we use the shallow copy and just write `argument=arguments` we will lose the attribute text after doing pop on `argument` (because it will be removed from `arguments`) as well.
