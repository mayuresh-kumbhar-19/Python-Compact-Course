from math import pi


def task1_area_of_circle():
    """Task 1: Calculate the area of a circle."""
    r = float(input("Input the radius of the circle : "))
    print(
        "The area of the circle with radius "
        + str(r)
        + " is: "
        + str(pi * r ** 2)
    )


def task2_variables():
    """Task 2: Declare variables, check their types, and output them."""
    zahl = 10
    kommazahl = 10.5
    text = "Hello, World!"
    wahrheitswert = True

    print("zahl:", zahl, "| type:", type(zahl))
    print("kommazahl:", kommazahl, "| type:", type(kommazahl))
    print("text:", text, "| type:", type(text))
    print("wahrheitswert:", wahrheitswert, "| type:", type(wahrheitswert))


def task3_type_conversion():
    """Task 3: Convert different data types and output the results."""
    integer_value = 10
    float_value = 10.5
    string_number = "20"

    integer_to_float = float(integer_value)
    float_to_integer = int(float_value)
    integer_to_string = str(integer_value)
    string_to_integer = int(string_number)
    integer_to_boolean = bool(integer_value)

    print("Integer to float:", integer_to_float)
    print("Float to integer:", float_to_integer)
    print("Integer to string:", integer_to_string)
    print("String to integer:", string_to_integer)
    print("Integer to boolean:", integer_to_boolean)


def task4_factorial():
    """Task 4: Calculate the factorial of a number."""
    n = int(input("Input a number to calculate its factorial: "))

    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    print("The factorial of", n, "is:", factorial)


if __name__ == '__main__':
    print("Python Compact Programming - Week 1 Tasks")
    print("------------------------------------------")

    task1_area_of_circle()
    print()

    task2_variables()
    print()

    task3_type_conversion()
    print()

    task4_factorial()
