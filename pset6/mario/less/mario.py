from cs50 import get_int


def main():
    n = get_positive_int("Height :")
    build(n)


def get_positive_int(s):
    n = get_int(s)
    while True:
        if n > 0 and n < 9:
            return n
        n = get_int(s)


def build(n):
    for i in range(n):
        j = n-(i+1)
        x = n-j
        while j > 0:
            print(" ", end="")
            j -= 1
        while x > 0:
            print("#", end="")
            x -= 1
        print()


main()