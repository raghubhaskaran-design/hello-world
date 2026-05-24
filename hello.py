try:
    a = 5
    b = 0
    c = a / b
    print(c)
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This block will always execute.")