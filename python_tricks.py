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
