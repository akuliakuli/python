def main():
    name = input("What is your name ? ")
    save_name(name)


def save_name(name):
    file = open("names.txt","a")
    file.write(f"{name}\n")
    file.close()


main()