import datetime
import pprint
import heapq
from collections import deque
from collections import Counter
import array
from types import MappingProxyType
from collections import ChainMap
from collections import defaultdict
import collections
import json
from collections import namedtuple
from string import Template
import functools # used to add metadate to wrapped function # noqa
import copy  # used for the deepcopy function to deep copy objects and collections # noqa
dct1 = {"a": 1, "b": 2}
dct2 = {"b": 3, "c": 4}

print(dct1)
print(dct2)
print({**dct1, **dct2})


def apply_discount(product, discount):
    price = int(product['price']*(1.0 - discount))
    assert 0 <= price <= product['price']
    return price


shoes = {'name': 'Fancy Shoes', 'price': 14900}
apply_discount(shoes, 0.25)
# apply_discount(shoes, 2.0)
print('worked')

# assert( 1 == 2, 'This should fail.') # always evaluates to true when passed in a tuple  # noqa
# assert 1 == 2, 'This should fail.'

names = [
    'Alice',
    'Bob',
    'Dilbert',  # note we can leave a trailing comma so we don't need to remove 2 lines if we remove 'Dilbert' # noqa
]

print("Hello %s" % "Ruben")

print("%s , %s" % ("Mr.", "Pierich"))  # old style string formatting
print('Hey {name}, your last name is {last}'.format(name="Ruben", last="Pierich"))  # new style formatting # noqa

a = 5
b = 10
print(f'Five plus ten is {a + b}')  # newest style string interpolation
# if format strings are user-supplied use Template STring to avoid security issues  # noqa
templ_string = 'Hey $name, there is error!'
print(Template(templ_string).substitute(name="Ruben"))


def bark(str):
    return str.upper()


print(bark("Ruth works out"))

print(list(map(bark, ['hello', 'hey', 'hi'])))
print(list(map(bark, ['hello', 'hey', 'hi'])))


# nested functions
def speak(text):
    def whisper(t):
        return t.lower() + '...'
    return whisper(text)


print(speak('Hello, World'))


# inner functions can capter lexical scope of their parent functions
def make_adder(n):
    def add(x):
        return x + n
    return add


plus_3 = make_adder(3)
plus_5 = make_adder(5)

print(plus_3(4))
print(plus_5(4))


# can make an Object callable - acts like a function but it isn't a function
class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return self.n + x


plus_6 = Adder(6)
print(plus_6(5))

print(callable(plus_6))  # see if object is callable (has __call__ method)

add = lambda x, y: x + y  # implicit return statement # noqa
print(add(5, 10))

# use lambda to sort a list of tuples
tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]
print(sorted(tuples, key=lambda x: x[1]))

print(sorted(range(-5, 6), key=lambda x: x * x))


# lambdas are lexical closures
def make_adder(n):
    return lambda x: x + n  # the lambda captures the n parameter's value


# possibly shouldn't use lambdas as they can make the code harder to read
# think a few minutes if you can write the code without the lambda function
plus_2 = make_adder(2)
print(plus_2(7))

# list comprehension
lst = [x for x in range(16) if x % 2 == 0]
print(lst)


# decorators
def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper


@uppercase
def greet():
    return 'Hello!'


print(greet())


def strong(func):
    def wrapper():
        original_result = func()
        return "<strong>" + original_result + "</strong>"
    return wrapper


def em(func):
    def wrapper():
        original_result = func()
        return "<em>" + original_result + "</em>"
    return wrapper


@strong
@em
def greet():
    return "Ruben"


print(greet())


def uppercase(func):
    @functools.wraps(func) #  recomended to use so debuging is easier and funcs retain their names and docstrings and others # noqa
    def wrapper():
        return func().upper()
    return wrapper


@uppercase
def greet():
    """Return a friendly greeting."""
    return 'Hello!'


# greet retains its' naem and doc string because of the @functools.wraps(func) called in the uppercase decorator above # noqa
print(greet.__name__)
print(greet.__doc__)


def foo(required, *args, **kwargs):
    print(required)
    if args:           # additional positional arguments (tuple)
        print(args)
    if kwargs:         # keyword argumets (dictionary)
        print(kwargs)


def print_vector(x, y, z):
    print("<", x, ",", y, ",", z, ">")


genexpr = (x * x for x in range(3))
print_vector(*genexpr)  # unpacking an iterable - can use for tuples and lists as well  # noqa

dict_vec = {'y': 0, 'z': 1, 'x': 1} # note the names of the keys match the print_vector param names # noqa
print_vector(**dict_vec)            # use a dictionary to input the params

print_vector(*dict_vec)  # this will use the keys as values in the order they are declared # noqa

# a function that doesn't return anything actually returns None

a = [1, 2, 3]
b = a
print(a == b)  # true
print(a is b)  # true - they point to the same object

# crate an identical copy of a
c = list(a)
print(a == c)  # true - they "look" the same
print(a is c)  # false - they are not the sam objects


# implement at least the __repr__ function because the interpreter will fall back on it for no __str__ method  # noqa
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return (f'{self.__class__.__name__}('f'{self.color!r}, {self.mileage!r})') # noqa


my_car = Car('blue', 100)
print(my_car)


def deco(func):
    def wrapper(*args):
        print(args)
    return wrapper


@deco
def testit(a, b, c):
    pass


testit("a", "b", "z")

original_list = [1, 2, 3]
original_dict = {"a": 1, "b": 2}
original_set = {"a", "b"}

# use factory functions to clone existing collections
#   this only creates shallow copies though -doesn't work for objects
new_list = list(original_list)
new_dict = dict(original_dict)
new_set = set(original_set)

xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = list(xs)  # make a shallow copy

print(xs)
print(ys)

xs.append(['new sublist'])
print(xs)
print(ys)

xs[1][0] = 'X'  # both xs and ys are effected because of the shallow copying
print(xs)
print(ys)

xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
zs = copy.deepcopy(xs)
# both look identical but they are not.  They are deep copies of one another

xs[1][0] = 'X'  # this won't affect the deep copy zs
print(xs)
print(zs)

sc = copy.copy(xs) # perform a shallow copy - explicitly for communicating to user # noqa


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x!r}, {self.y!r})'


a = Point(23, 42)
b = copy.copy(a)  # shallow copy

print(a)
print(a is b)


class Rectangle:
    def __init__(self, topleft, bottomright):
        self.topleft = topleft
        self.bottomright = bottomright

    def __repr__(self):
        return (f'Rectangle({self.topleft!r}, 'f'{self.bottomright!r})')


rect = Rectangle(Point(0, 1), Point(5, 6))
srect = copy.copy(rect)  # shallow copy

print(rect)
print(srect)
print(rect is srect)

srect.topleft.x = 999
print(rect)
print(srect)

drect = copy.deepcopy(srect)
drect.topleft.x = 222
print(drect)
print(rect)
print(srect)

#  tuples are immutable
Car = namedtuple('Car', 'color mileage')  # a named touple

# or

Car = namedtuple('Car', [
    'color',
    'mileage',
])


my_car = Car('red', 3812.4)
print(my_car.color)
print(my_car.mileage)

# can access a named-tuple by index too
print(my_car[0])

# tuple unpacking works for functions with tuples
print(*my_car)


# you can exted named tuples like a normal class
class MyCarWithMethods(Car):
    def hexcolor(self):
        if self.color == 'red':
            return '#ff0000'
        else:
            return '#000000'


c = MyCarWithMethods('red', 1234)
print(c.hexcolor())

# adding a field to a named tuble
ElectricCar = namedtuple('ElectricCar', Car._fields + ('charge',))

e = ElectricCar('red', 1234, 45.0)
print(e)

print(e._asdict())
print(json.dumps(my_car._asdict()))

print(my_car._replace(color='blue')) # lets us change some of the values in the named tuple # noqa

new_car = Car._make(['red', 999])  # use _make to create a new named tuple
print(new_car)

diction = {x: x * x for x in range(6)}  # dictionary comprehension
print(diction)

# dictionaries must only have hashable keys like strings, numbers, or tuples that are hashable as keys  # noqa

# collections.OrderedDict # remembers the insertion order of keys

d = collections.OrderedDict(one=1, two=2, three=3)
print(d)

d['four'] = 4
print(d)

print(d.keys())

# collections.defaultdict - return default values for missing keys
dd = defaultdict(list)

dd['dogs'].append('Rufus')
dd['dogs'].append('kathrin')
dd['dogs'].append('Mr Sniffles')

print(dd['dogs'])

# collections.ChainMap - search multiple dictionaries as a single mapping
chain = ChainMap(dct1, dct2)
print(chain)

print(chain['b'])

writable = {'one': 1, 'two': 2}
read_only = MappingProxyType(writable)  # create a read only dictionary

print(read_only['one'])

writable['one'] = 99  # unwrapped dictionary is writable
print(read_only['one'])

arr = array.array('f', (1.0, 1.5, 2.0, 2.5))  # arrays hold values with the samedatatype and are more space efficient than lists  # noqa

print(arr[1])
print(arr)

# arrays are mutable
arr[1] = 23.0
print(arr)

# can't do this:  arrp1[ = 'hello' because arrays only hold all the same data type # noqa

arr = 'abcd'
print(arr[1])

# can't update a string - they are immutable
# arr[1] = 'e'
# del arr[1] # can't do

lst = list('abcd')  # strings can be unpacked to a list
print(lst)

vowels = {'a', 'e', 'i', 'o', 'u'}  # a set
squares = {x * x for x in range(10)}  # set comprehension

#  to create an empty set you must use the set() construtor as {} makes an empty dictionary  # noqa
print('e' in vowels)

vowels.add('x')
print(vowels)

vwls = frozenset(vowels)  # this set cannot be modified
#  vwls.add("p")  # can't do to frozen set (or delete)
print(vwls)

inventory = Counter() #  this set will keep track of our items and how many are in the set  # noqa


loot = {'sword': 1, 'bread': 3}
inventory.update(loot)
print(inventory)

more_loot = {'sword': 1, 'apple': 1}
inventory.update(more_loot)
print(inventory)

# be careful with the multiset

#  prints the num of unique items
print(len(inventory))
#  print sum of item counts (values
print(sum(inventory.values()))

# simple built-in stacks
s = []
s.append('Ruth')
s.append('is')
s.append('Married')

print(s.pop())
print(s.pop())
print(s.pop())

#  this is a stack
s = deque()
s.append('eat')
s.append('sleep')
s.append('code')

print(s)

print(s.pop())
print(s.pop())
print(s.pop())


# don't use a list for an actual Queue - it is slow in python

q = []

# list based binary heap
heapq.heappush(q, (2, 'code'))
heapq.heappush(q, (1, 'eat'))
heapq.heappush(q, (3, 'sleep'))

while q:
    next_item = heapq.heappop(q)
    print(next_item)


emails = {
        'Bob': 'bob%example.com',
        'Alice': 'alice@example.com',
        }

for name, email in emails.items():
    print(f'{name} -> {email}')
start = 0
stop = 10
step = 2
for i in range(start, stop, step):
    print(i)

# general template for  alist comprehension
# values = [expression for item in collection]

even_squares = [x * x for x in range(10) if x % 2 == 0]

print(even_squares)

set_comprehension = {x * x for x in range(-9, 10)}
print(set_comprehension)

dictionary_comprehension = {x: x * x for x in range(5)}
print(dictionary_comprehension)

lst = [1, 2, 3, 4, 5]
print(lst)

print(lst[1:3:1])  # upper bound is always excluded

print(lst[::2])  # get every other value from list

print(lst[::-1])  # get list in reverse order #  stick with liste.reverse() method  # noqa
# or reversed

del lst[:] # delete all  values in a list #  updates list and all its' references  # noqa

lst.clear()  # also deletes all values ina list  # python 3


lst = [1, 2, 3, 4, 5]
lst[:] = [7, 8, 9]
print(lst)


class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value

# this will loop forever and return 'HEllo'
# repeater = Repeater('HEllo')
# for item in repeater:
#    print(item)


my_list = [1, 2, 3]
iterator = iter(my_list)

next(iterator)
next(iterator)
next(iterator)

#  next(iterator)  # raises a StopIteration exception

# we can use generators to implement iterators easier


def repeater(value):
    while True:
        yield value


# Usage ofr a repeater
# for x in repeater('Hi'):
#    print(x)

# Generator expressions
iterator = ('Hello' for i in range(3))  # can't be reused
for x in iterator:
    print(x)

iterator = ('Hello' for i in range(3))
print(list(iterator))  # not a list comprehension!!!

# this iterator yeilds the squares of the even numbers between 0 and 9 #  noqa
even_squares = (x * x for x in range(10) if x % 2 == 0)

for x in even_squares:
    print(x)

# implement an in-line iterator
for x in ('Bom dia' for i in range(3)):
    print(x)

print(sum(x * 2 for x in range(10)))


def integers():
    for i in range(1, 9):
        yield i


def squared(seq):
    for i in seq:
        yield i * i


iterator_chain = squared(integers())
print(list(iterator_chain))


def negated(seq):
    for i in seq:
        yield -i


chain = negated(squared(integers()))

print(list(chain))


integers = range(8)
squared = (i * i for i in integers)
negated = (-i for i in squared)

print(list(negated))


# default values for dictionaries
name_for_user = {
        10: "Ruthy",
        20: "Ruby",
        30: "Lena",
        }

print(name_for_user.get(40, 'some default value'))


mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}

# use the json.dumps method to pretty print a dictionary
#    - this technize only works for dict, list, tuple, str, int, float, bool, and None  # noqa
#    - doesn't work for sets or all keyword
print(json.dumps(mapping, indent=4, sort_keys=True))
#   doesn't work with unicode

# this next function works on any datatypes
pprint.pprint(mapping)

i# in a repl session use teh following to reduce the number of options  # noqa
[_ for _ in dir(datetime) if 'date' in _.lower()]

# to get more help in a repl on a method/function/etc use
# help(datetime)
