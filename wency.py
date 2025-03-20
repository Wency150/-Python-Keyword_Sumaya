import math
from random import randint

def check_even_odd(num):
    if num % 2 == 0:
        return True
    else:
        return False

class ExampleClass:
    def __init__(self, value):
        self.value = value

    def divide(self, divisor):
        try:
            assert divisor != 0, "Divisor cannot be zero!"
            return self.value / divisor
        except AssertionError as error:
            print("Assertion Error:", error)
            return None
        except Exception as e:
            print("An error occurred:", e)
            return None
        finally:
            print("Division attempt completed.")

def check_conditions(a, b):
    if a and b:
        return "Both are True"
    elif a or b:
        return "At least one is True"
    else:
        return "Both are False"

def loop_demo():
    for i in range(5):
        if i == 2:
            continue
        print("For loop iteration:", i)
        if i == 4:
            break
    
    count = 0
    while count < 3:
        print("While loop count:", count)
        count += 1
    pass

square = lambda x: x * x

global_var = "Global Variable"

def outer_function():
    nonlocal_var = "Outer Variable"
    
    def inner_function():
        nonlocal nonlocal_var
        global global_var
        nonlocal_var = "Modified Nonlocal"
        global_var = "Modified Global"
    
    inner_function()
    print(nonlocal_var)

numbers = [1, 2, 3, 4]
del numbers[0]

with open("example.txt", "w") as file:
    file.write("This is an example file.")

def generator_example():
    for i in range(3):
        yield i

if __name__ == "__main__":
    num = randint(1, 100)
    print(f"Number {num} is even? {check_even_odd(num)}")
    
    obj = ExampleClass(10)
    print("Result of division:", obj.divide(2))
    
    print(check_conditions(True, False))
    
    loop_demo()
    
    print("Square of 5:", square(5))
    
    outer_function()
    
    print("Modified global variable:", global_var)
    
    gen = generator_example()
    print("Generator output:", list(gen))
