"""
AI & MACHINE LEARNING - BASICS
Beginner-friendly Python practice file

Based on the topics in the accompanying learning notes.
Run with: python ai_ml_basics.py

Choose an exercise from the menu to practise Python basics.
"""
# 1. INTRODUCTION TO AI, ML AND DEEP LEARNING
# Artificial Intelligence (AI): The broad field of making machines
# perform tasks that normally require human intelligence.
# Machine Learning (ML): A subset of AI where computers learn patterns
# from data instead of being programmed with every rule.
# Deep Learning (DL): A subset of ML that uses neural networks with
# multiple layers to learn complex patterns.
# Relationship: AI contains ML, and ML contains Deep Learning.


def show_ai_ml_dl_examples():
    print("\nAI example: A voice assistant responding to your question.")
    print("ML example: An email system learning to identify spam.")
    print("DL example: A neural network recognising objects in images.")
# 2. VARIABLES AND DATA TYPES

def variables_and_data_types():
    name = "Mohammed"       # string
    age = 21                # integer
    cgpa = 6.58             # float
    is_student = True       # boolean

    print("\nName:", name)
    print("Age:", age)
    print("CGPA:", cgpa)
    print("Is student:", is_student)

    print("\nData types:")
    print(type(name))
    print(type(age))
    print(type(cgpa))
    print(type(is_student))
# 3. INPUT AND OUTPUT

def input_output():
    name = input("\nEnter your name: ")
    print("Hello,", name, "! Welcome to Python.")
# 4. CONDITIONS (IF-ELSE)

def check_adult():
    age = int(input("\nEnter your age: "))

    if age >= 18:
        print("You are an adult.")
    else:
        print("You are a minor.")


def check_even_or_odd():
    number = int(input("\nEnter a number: "))

    if number % 2 == 0:
        print(number, "is even.")
    else:
        print(number, "is odd.")
# 5. LOOPS

def for_loop_example():
    print("\nNumbers from 1 to 10:")
    for number in range(1, 11):
        print(number)


def while_loop_example():
    print("\nCountdown:")
    number = 5

    while number >= 1:
        print(number)
        number -= 1

    print("Finished!")
# 6. LISTS

def list_example():
    fruits = ["apple", "banana", "mango"]

    print("\nOriginal list:", fruits)
    print("First fruit:", fruits[0])

    fruits.append("orange")
    print("After adding orange:", fruits)

    fruits.remove("banana")
    print("After removing banana:", fruits)

    print("All fruits:")
    for fruit in fruits:
        print(fruit)


# ============================================================
# 7. FUNCTIONS
# ============================================================

def greet(name):
    return "Hello, " + name + "!"


def function_example():
    name = input("\nEnter your name: ")
    message = greet(name)
    print(message)
# 8. BEGINNER PYTHON PROGRAMS

def add_two_numbers():
    first = float(input("\nEnter first number: "))
    second = float(input("Enter second number: "))
    print("Sum =", first + second)


def multiplication_table():
    number = int(input("\nEnter a number: "))

    for i in range(1, 11):
        print(number, "x", i, "=", number * i)


def count_vowels():
    text = input("\nEnter a word or sentence: ").lower()
    vowels = "aeiou"
    count = 0

    for character in text:
        if character in vowels:
            count += 1

    print("Number of vowels:", count)


def factorial():
    number = int(input("\nEnter a non-negative integer: "))

    if number < 0:
        print("Factorial is not defined for negative numbers.")
        return

    result = 1
    for i in range(1, number + 1):
        result *= i

    print("Factorial =", result)


def simple_calculator():
    first = float(input("\nEnter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    second = float(input("Enter second number: "))

    if operator == "+":
        print("Result =", first + second)
    elif operator == "-":
        print("Result =", first - second)
    elif operator == "*":
        print("Result =", first * second)
    elif operator == "/":
        if second != 0:
            print("Result =", first / second)
        else:
            print("Cannot divide by zero.")
    else:
        print("Invalid operator.")
# 9. PRACTICE MENU

EXERCISES = {
    "1": ("AI, ML and DL examples", show_ai_ml_dl_examples),
    "2": ("Variables and data types", variables_and_data_types),
    "3": ("Input and output", input_output),
    "4": ("Adult check (if-else)", check_adult),
    "5": ("Even or odd", check_even_or_odd),
    "6": ("For loop", for_loop_example),
    "7": ("While loop", while_loop_example),
    "8": ("Lists", list_example),
    "9": ("Functions", function_example),
    "10": ("Add two numbers", add_two_numbers),
    "11": ("Multiplication table", multiplication_table),
    "12": ("Count vowels", count_vowels),
    "13": ("Factorial", factorial),
    "14": ("Simple calculator", simple_calculator),
}


def main():
    while True:
        print("\n" + "=" * 45)
        print("       AI & ML - PYTHON BASICS")
        print("=" * 45)

        for number, (title, _) in EXERCISES.items():
            print(f"{number}. {title}")

        print("0. Exit")

        choice = input("\nChoose an exercise: ").strip()

        if choice == "0":
            print("Keep practising. Happy coding!")
            break

        exercise = EXERCISES.get(choice)

        if exercise:
            title, function = exercise
            print(f"\n--- {title} ---")
            function()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
