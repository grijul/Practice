import math

# task 1


class Number:
    def __init__(self):
        self.num = None

    def input(self):
        while True:
            try:
                self.num = int(input("Input number"))
                break
            except ValueError:
                print("Enter integer number")

    def output(self):
        print(self.num)


# task 2

class Children:
    def __init__(self):
        self.name = None
        self.surname = None
        self.second_name = None
        self.age = None

    def set_data(self):
        self.name = input("Input name")
        self.surname = input("Input surname")
        self.second_name = input("Input second name")
        self.age = input("Input age")

    def data_output(self):
        print(self.name, self.surname, self.second_name, self.age)


child_one = Children
child_one.set_data(child_one)
child_one.data_output(child_one)
child_two = Children
child_two.set_data(child_two)
child_two.data_output(child_two)


# Task 3


class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        result = self.a + self.b
        print("Addition:", result)

    def multiplication(self):
        result = self.a * self.b
        print("Multiplication:", result)

    def division(self):
        if self.b != 0:
            result = self.a / self.b
            print("Division:", result)
        else:
            print("Error: division by 0")

    def subtraction(self):
        result = self.a - self.b
        print("Subtraction:", result)


math_operations = Math(10, 5)
math_operations.addition()
math_operations.multiplication()
math_operations.division()
math_operations.subtraction()


# Task 4


class Numbers:
    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3

    def display_numbers(self):
        print(f"Variables: {self.var1}, {self.var2}, {self.var3}")

    def modify_numbers(self, new_var1, new_var2, new_var3):
        self.var1 = new_var1
        self.var2 = new_var2
        self.var3 = new_var3
        print("Variables modified successfully.")

    def sum_of_numbers(self):
        return self.var1 + self.var2 + self.var3

    def max_number(self):
        return max(self.var1, self.var2, self.var3)


numbers_instance = Numbers(5, 8, 3)

numbers_instance.display_numbers()

numbers_instance.modify_numbers(10, 15, 7)
numbers_instance.display_numbers()

sum_result = numbers_instance.sum_of_numbers()
print(f"Sum of numbers: {sum_result}")

max_result = numbers_instance.max_number()
print(f"Maximum number: {max_result}")


# Task 5


class Student:
    def __init__(self, name="Ivan", age=18, groupNumber=212):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getGroupNumber(self):
        return self.groupNumber

    def setNameAge(self, new_name, new_age):
        self.name = new_name
        self.age = new_age

    def setGroupNumber(self, new_group_number):
        self.groupNumber = new_group_number


student1 = Student()
student2 = Student("Alice", 20, 215)
student3 = Student("Bob", 19, 207)
student4 = Student("Eva", 22, 201)
student5 = Student("Charlie", 21, 209)

print(f"Student 1: {student1.getName()}, {student1.getAge()}, Group {student1.getGroupNumber()}")
print(f"Student 2: {student2.getName()}, {student2.getAge()}, Group {student2.getGroupNumber()}")
print(f"Student 3: {student3.getName()}, {student3.getAge()}, Group {student3.getGroupNumber()}")
print(f"Student 4: {student4.getName()}, {student4.getAge()}, Group {student4.getGroupNumber()}")
print(f"Student 5: {student5.getName()}, {student5.getAge()}, Group {student5.getGroupNumber()}")

student1.setNameAge("John", 25)
student1.setGroupNumber(210)

student2.setNameAge("Mia", 22)
student2.setGroupNumber(208)

print("\nAfter modifications:")
print(f"Student 1: {student1.getName()}, {student1.getAge()}, Group {student1.getGroupNumber()}")
print(f"Student 2: {student2.getName()}, {student2.getAge()}, Group {student2.getGroupNumber()}")


# Task 6

class Soda:
    def __init__(self, additive=None):
        self.additive = additive

    def show_my_drink(self):
        if self.additive:
            print(f"Газировка и {self.additive}")
        else:
            print("Обычная газировка")


soda1 = Soda()
soda1.show_my_drink()

soda2 = Soda("лимон")
soda2.show_my_drink()


# Task 7


class Car:
    def __init__(self, color, car_type, year):
        self.color = color
        self.car_type = car_type
        self.year = year
        self.engine_status = False

    def start_engine(self):
        if not self.engine_status:
            self.engine_status = True
            print("Автомобиль заведен")
        else:
            print("Автомобиль уже заведен")

    def stop_engine(self):
        if self.engine_status:
            self.engine_status = False
            print("Автомобиль заглушен")
        else:
            print("Автомобиль уже заглушен")

    def set_year(self, new_year):
        self.year = new_year
        print(f"Год выпуска автомобиля изменен на {new_year}")

    def set_type(self, new_type):
        self.car_type = new_type
        print(f"Тип автомобиля изменен на {new_type}")

    def set_color(self, new_color):
        self.color = new_color
        print(f"Цвет автомобиля изменен на {new_color}")


car1 = Car(color="Синий", car_type="Седан", year=2020)

car1.start_engine()
car1.set_year(2022)
car1.set_type("Внедорожник")
car1.set_color("Красный")
car1.stop_engine()


# Task 8


def call_counter(method):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        result = method(*args, **kwargs)
        print(f"Employee {wrapper.calls}: {result}")
        return result

    wrapper.calls = 0
    return wrapper

class Employee:
    def __init__(self):
        self.name = None
        self.surname = None
        self.num = None
        self.salary = None

    def set_data(self, name, surname, num: int, sal: float):
        self.name = name
        self.surname = surname
        self.num = num
        self.salary = sal

    @call_counter
    def employee_data(self):
        print(f"Name: {self.name}, Surname: {self.surname}, "
              f"Number: {self.num}, Salary: {self.salary}")


emp1 = Employee
emp1.set_data(emp1, "Sergey", "Bebrin", 69420, 400.0)

emp2 = Employee
emp2.set_data(emp2, "Anton", "Karr", 2167, 500)


# Task 9


class Rectangle:
    def __init__(self, width, height):
        self.set_width(width)
        self.set_height(height)

    def set_width(self, width):
        if width > 0:
            self.width = width
        else:
            raise ValueError("Width must be greater than zero.")

    def set_height(self, height):
        if height > 0:
            self.height = height
        else:
            raise ValueError("Height must be greater than zero.")

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


class Circle:
    def __init__(self, radius, center_x=0, center_y=0):
        self.set_radius(radius)
        self.set_center(center_x, center_y)

    def set_radius(self, radius):
        if radius > 0:
            self.radius = radius
        else:
            raise ValueError("Radius must be greater than zero.")

    def set_center(self, center_x, center_y):
        self.center_x = center_x
        self.center_y = center_y

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_circumference(self):
        return 2 * math.pi * self.radius


rectangle = Rectangle(width=5, height=8)
print(f"Rectangle Area: {rectangle.calculate_area()}")
print(f"Rectangle Perimeter: {rectangle.calculate_perimeter()}")

circle = Circle(radius=3, center_x=2, center_y=4)
print(f"Circle Area: {circle.calculate_area()}")
print(f"Circle Circumference: {circle.calculate_circumference()}")

# Task 11


class Time:
    def __init__(self, h: int, min: int, s: int):
        if h in range(0, 24):
            self.hours = h
        else:
            print("hours should be in range 0-23")
        if min in range(0, 60):
            self.minutes = min
        else:
            print("minutes should be in range 0-59")
        if s in range(0, 60):
            self.seconds = s
        else:
            print("seconds should be in range 0-59")

    def print_time(self):
        print(f"{self.hours} hours, {self.minutes} minutes, {self.seconds} seconds")

    def meridiem_time(self):
        if self.hours in range(1, 12):
            print(f"{self.hours} a.m., {self.minutes} minutes, {self.seconds} seconds")
        elif self.hours == 0:
            print(f"{12} a.m., {self.minutes} minutes, {self.seconds} seconds")
        elif self.hours == 12:
            print(f"{12} p.m., {self.minutes} minutes, {self.seconds} seconds")
        else:
            print(f"{self.hours - 12} p.m., {self.minutes} minutes, {self.seconds} seconds")


h1 = Time(0, 23, 59)
h1.print_time()
h1.meridiem_time()
h2 = Time(23,59,59)
h2.print_time()
h2.meridiem_time()
h3 = Time(12,59,30)
h3.print_time()
h3.meridiem_time()
h4 = Time(13,23,30)
h4.print_time()
h4.meridiem_time()
h5 = Time (6,23,39)
h5.print_time()
h5.meridiem_time()