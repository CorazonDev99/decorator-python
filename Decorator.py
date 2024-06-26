# Dekorator - bu Pythondagi dizayn namunasi bo'lib,
# u foydalanuvchiga uning tuzilishini o'zgartirmasdan mavjud ob'ektga yangi funksiyalar qo'shish imkonini beradi.

# Oddiy dekoratorlar:
def my_decorator(func):
    def wrapper():
        print("Funktsiya chaqiruvidan oldin qo'shimcha kod")
        func()
        print("Funktsiya chaqiruvidan keyin qo'shimcha kod")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()


#Argumentli dekoratorlar:
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}!")

greet("World")


# Class dekoratorlar:
def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Funksiya {func.__name__}ni chaqirish")
        return func(*args, **kwargs)
    return wrapper

@debug
class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()
print(calc.add(2, 3))



#OOP abstraction
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius manfiy bo'lishi mumkin emas")
        self._radius = value


circle = Circle(5)
print(circle.radius)  # method getter
circle.radius = 10  # method setter
print(circle.radius)

