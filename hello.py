def greet():
    name = input("What is your name ? ").strip().title()
    first,second = name.split(" ")
    sayHello(first)


def sayHello(to):
    if to == 'Jonathan': print("Forbidden for seagulls")
    else : print(f"Welcome aboard, {to}")

greet()