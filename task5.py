x = int(input("Enter any number1:"))
y = int(input("Enter any number2:"))

def days(x,y):
    day = 1
    while x < y:
        x *= 1.1
        day += 1
    print(day)
days(x=x, y=y)

