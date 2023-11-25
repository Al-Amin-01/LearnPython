try:
    num=int(input("enter a number:"))
    print(num)
    x=10/0
except ValueError:
    print("invalid input")
except ZeroDivisionError:
    print("divided by zero") 