def count():
    x = int(input("What does x equals to ? "))
    y = int(input("What does y equals to ? "))
    compare(x,y)

def compare(a,b):
    if a > b:
        print("a is bigger than b")
    elif a < b:
        print("b is bigger than a")
    else:
        print("a is equal to b")

count()