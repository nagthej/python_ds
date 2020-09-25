Info: 
1. difference between method and function - method: method is a function that belong to an object. But usually both are same
2. In-place: modify an object in that memory location itself -- does not create new copy
3. placeholders = a place where some value will be put in during execution. EG: print("hello {}".format(name)) OR we can use f' strings --- EG: msg = f'{name}' 
4. TO get what all methods we have access to we can do: dir(var) dir(string) dir(object) ----to get more info, do: print(help(str)), print(help(str.lower))
5. to find datatype do: print(type(object/var)
6. Single = is assignment, double == is comparision 
7. type casting = changing datatype of objects = int(var), str(var)
8. python does not have switch case.... -> use if, elif instead
9. Keeping code 'DRY' means 'dont repeat yourself'... dont have duplicate code... use function to import/call same code







1. Strings

1. Strings are a length of individual characters - can be printed upto some chars (slicing) EG: print(msg[0:4]) OR print(msg[6:])
2. Strings are mutable - value can be changed
3. Difference between single and double quoted string is just that - begin and end of string can be uniqueley identified if there is mix of it in single string EG: "Bobby's world"
4. to find number of chars - len(str)
5. count of words/chars - print(msg.lower()) .upper(),  msg.count('hello') counts hello how many times in 'msg'
6. find word/char at which index - msg.find('world') = returns 6 where 6th index starts world, 
7. Replace string = msg.replace('world', 'universe') --- This wont replace in-place --creates new string which should be assigned to a var and then should print
8. concatenate: msg = 'hello' greet = 'world' print(msg+ " ' +greet)

2. numbers - integers & floats

1. integer is whole number, floats are decimals
2. floor division - do not get decimal point after division, EG: 3//2 = 1 
3. modulus: 3 % 2 gives remainder after division
4. To find power/exponential: 3**2 = 9
5. num += 1(num = num+1)
6. abs(-3) = 3
7. round(3.75) = 4 ......round (3.75, 1) = 3.8
8. 


3. List

1. Holds list of values (objects)
2. len(list) = int length of list
3. print(list[0]) - > list elements can be accessed by index
4. -ve indexes... print(len[-1]) -> prints last item, no need to worry about how many indexes exist to access last item.
5. if tried to access a index not in list? Get a "list index out of range"
6. print(list[0:2]) -> prints 0th, 1st but NOT 2nd, print(list[2:]), print(list[:2])... slicing
7. Add item to list:
list.append(object)
list.insert(0, value) -> insert value at 0th index position
list.extend(newList) -> adds new list items to "list" items at 0th position
8. Remove from list
list.remove(directValue)
list.pop() -> removes last value and we can store the value in a var (useful for stack or queue) OR
list.pop(3) -> pops 3rd element from list
list.reverse() -> reverses list

list.sort() -> sorts in alphabetical order, if numbers its ascending order
list.sort(reverse=True) -> sorts in descending order
All above sorts in-place

To get sorted version without altering original, we can use:
sorted_list = sorted(list)

To get min/max/sum of numbers list: min(list), max(list), sum(list)

To find index of certain value in list -> list.index('value') -> gives index int

To check if value is in list or not -> 'value' in list -> gives True/False

To also have index with what value we are on:
for index, course in enumerate(courses, start=0th):
print(index, course)

To get comma sep strings in output use "join" method:
courses = ['hi', 'hello', 'how']
course_str = ', '.join(courses)
print(course_str) -> hi, hello, how 

courses = ['hi', 'hello', 'how']
course_str = ' -  '.join(courses)
print(course_str) ->  hi - hello - how 

split function:
new_list = course_str.split(' - ')
print(new_list) -> ['hi', 'hello', 'how']

4. Tuples - very similar to lists but not mutable

If you want a list where you know the values wont be changed/should not be changed -> use tuple

tuple = ('history', 'math', 'science')
If tried to change values, Type error: tuple does not support item assignment


5. Sets - values that are unordered and has no duplicates

courses = {'history', 'math', 'science'}
print(courses) -> may print {'math', 'science', 'history'}
Sets throw away duplicates, prints only unique ones
Sets are optimized for checking if a value is in set/list/tuple or not

print(cs_course.intersection(art_course)) -> prints common courses in both course
print(cs_course.difference(art_course)) -> prints cs_courses courses which are not in both art_course
print(cs_course.union(art_course)) -> prints all courses in both course

emtpy_list = [] or list()
empty_tuple = () or tuple()
empty_set = set()
empty_dict = {}

6. dictionary - allows us to work with key, value pairs (hashmaps), key is a unique identifier, value can be any data

keys can be any immutable datatypes, usually it is integers or strings


student = {'name': 'john', 'age': 25, 'courses': ['math', 'cs']}
print(student['name'])
print(student['courses'])

keyError is when you try a key not in dictionary

print(dict.get('name')) -> if tried to access a key not in dict, you will get None instead of keyError
print(dict.get('name', 'Not found in dict'))

student['phone'] = 333-333-3333
student['name'] = 'Jane'

print(student) -> prints updated dict

if youu want to update many keys and values in one shot, use update method
student.update({'name': 'Jane', student['phone']:'333-333-3333'})

delete a specific key and value
del student['age']
print(student)

age = student.pop('age')
print(age) 
print(student) -> removes age from dict also

print(len(student)) -> prints num of keys in dict

print(student.keys())
print(student.value())
print(student.items())

loop through all key values:

for key, value in dict.items():
	print(key, value) -> prints key and value


7. Conditionals and booleans - if, else and elif

==, !=, <, >, <=, >=
object identity = 'is'
and
or
not


language = 'python'
if language == 'python': # Tests for equality
	print('Conditional was True') 

usages:
if user == 'admin' and loogged_in:
	print('true')
if user == 'admin' or loogged_in:
	print('true')
if not loogged_in: # negates logged_in
	print('please log in')


Difference between '==' and 'is' ? -> if we use 'is' then we are checking if they are in same memory location (same object identity)
Eg: 
a = [1,2,3]
b = [1,2,3]
print(a==b) # Returns True as both list have same contents
print(a is b) # Returns False as both list contents are in different memory locations

To print memory locations:
print(id(a))
print(id(b))

To make same memory locations:
a = [1,2,3]
b = a
Now, b contents has same memory locations as a


python detects if values are there in a var/object to Evaluate to False or true:
# False Values:
    # False
    # None
    # Zero(0) of any numeric type
    # Any empty sequence. For example, empty str,list, tuple '', (), [].
    # Any empty mapping. For example, {}.

condition = False

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')





8. Loops and Iterations - For/While Loops

break = completely breaks out of loop
continue = skips that Iteration of loop, continues next Iteration


# Run through a loop specific number of times - use range
for i in range(10): # loops 0 to 9 
	print(i) # prints 0 to 9, but not 10

for i in range(1, 11): # loops 1 to 10
	print(i) # prints 1 to 10, but not 11

x = 0
while x < 10: 
	if x == 5:
		break
	print(x)
	x += 1 # prints 0 to 9


In infinite loop, you can exit out of loop by break statement.



9. functions

#to write empty func
def hello_func():
	pass

print(hello_func)
#To call a func
hello_func()



==========
# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    # year 2017
    # month 2
    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(days_in_month(2017, 2))
===========

What is positional args and kwargs? --------> Basically it allows arbitary(not sure of exact number) number of args...

def student_info(*args, **kwargs):
	print(args)
	print(kwargs)

student_info('Math', 'art', name='john', age=22)


o/p of above program:
('Math', 'art')
{name='john', age=22}

args accept as tuple whatever we supply
kwargs accept as dict whatever we supply

=============

def student_info(*args, **kwargs):
	print(args)
	print(kwargs)

courses = ['Math', 'art']
info = {'name': 'john', 'age': 22}

student_info(courses, info) #Both courses and info goes as list to positional *arg, you wontt get an error, but this is not right type to call
student_info(*courses, **info) #Unpacks the value and passes courses list to *args and info dict to **kwargs

============

10. Import Modules and Exploring The Standard Library


when we import a module python checks various locations, based on sys.path

import sys

print(sys.path)
Gives output of all directories where it looks for module
1st priority: checks same file directory
2nd: PYTHONPATH env variable
3rd: std libraries (/Library/Frameworks/python3InstalltionPath)
4th: site packages for 3rd party packcages


some std libraries:
import random #random.choice(list) gives random item from list
import datetime 
import math #std math ops
import calendar

import os #gives access to underlying OS
os.getcwd() #current working dir
print(os.__file__) #prints location of file in fileSystem --> We can go into that file and see entire python packages in python3.6 folder


=========================================================================== Fundamentals done upto above ====================================================================


=========================================================================== Important usages in python below ====================================================================

1. pip 

#for help with options
pip help 
pip help <cmd>

pip search Pympler #returns package name and descriptioon, if we do not exactly know pkg name do pip search
pip search cassandra

pip list #lists pkg and version
pip list --outdated #To check if latest is available
pip install -Upgrade <pkgName>
pip freeze

pip uninstall <pkgName>
pip install <pkgName>


#if you want to give all your pip pkgs to friend to install in their env
pip freeze > requirements.txt
then, on friend env do
pip install -r requirements.txt #installs all pkgs in their env


#if you wnat to upgrade all pip pkgs to latest version
pip freeze --local | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip install -Upgrade


===================================

2. venv

venv is a way to separate different python env for different , Basically to use different pkg versions that maybe required for different projects


pip list
#above lists all pkgs in global level 

#To install
pip install virtualenv

#First its good to have a main dir to have all venv inside it - all in one place, easy to find all venv
mkdir Environments
cd Environments
ls #empty
virtualenv <AnyNameYourProojectSpecfic> #virtualenv project1_env

source project1_env/bin/activate
> (venv) thats it, now you are in project1 venv... whatever you do pip install here will only be present in project1_env

which python -> path to python you are using within your venv
which pip


> deactivate #to get out of python venv

To delete a venv,
rm -rf project1_env #thats it remove the venv folder

-----

virtualenv -p <pythonVersion2.6> py2.6env #To have python2.6 in this env
virtualenv -p <pythonVersion3> py3env #To have python3 in this env


3. Scoping of variables

'''
LEGB
Local, Enclosing, Global, Built-in
'''

for a in range(2):
    x = 'global {}'.format(a)


def outer():
    # x = 'outer x'
    for b in range(3):
        x = 'outer {}'.format(b)

    def inner():
        # x = 'inner x'
        for c in range(4):
            x = 'inner {}'.format(c)
        print(x)
        print(a, b, c)

    inner()
    print(x)
    print(a, b)

outer()
print(x)
print(a)



4. 















=========================================================================== python OOP programming from below ====================================================================

1. Classes and Instances

why classes?
They allow us to logically group our data and functions in a way that is easy to reuse and easy to build upon

===> The data and functions associated with specific class, we call those as  attributes and methods.... When we say a methods, it is a function associated with a class 















==========

1. Essential Skills Every Well-Rounded Programmer Should Know

1. Git - version control

2. Databases - SQL (web apps, desktop apps, standalone etc)
            - ORM - object relational mapping

            - NoSQL (mongoDB)

3. Commandline - Terminal

4. Unit testing - CI/CD is a plus (Jenkins/TravisCI)

5. Learn multiple programming languages (Hackernoon)

==========

Online resources:

1. youtube
DS and algorthms: MIT open courseware
the new boston
Derek banas = Software design patterns
Computerphile = SQL injection/old videos
Eli the computer guy = networking
Learncode.academy = short/fiitting
levelup tuts = web dev
DevTips = web design
realcsstricks = CSS, web
phpacademy = PHP 
NewCircle training
nextday video 
Conferences/key notes
---------

Websites
1. Khanacademy.org = Math section
2. nodeschool.io = Terminal way of learning programming, download npm and Run
3. codeacademy.com = Web dev
4. edX = also popular
Linux system admin Essential course

5. codeschool.com 
6. treehouse = webdev

----------
Twitter
Great way to follow tech ppl 
1. Guido van Rossum
2. raymondh - python
3. David beazley
4. Follow those in your area


---------

Reddit
1. links to lot of rersources































