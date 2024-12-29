def main():
    print_column(5)
    print_row(3)


def print_column(height):
    print("#\n" * height, end="")


def print_row(width):
    print("?" * width)

main()