from string import Template
import functools # used to add metadate to wrapped function # noqa
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
    return lambda x: x + n # the lambda captures the n parameter's value


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



