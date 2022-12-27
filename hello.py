def main():
    name = input("What is your name ? ")
    save_name(name)


def save_name(name):
    file = open("names.txt","w")
    file.write(name)
    file.close()


main()