from cs50 import get_string
from sys import argv


def main():
    checkin(argv)
    n = int(argv[1])


def checkin(argv):
    if len(argv) != 2:
        exit("usage 'Python caesar.py n'")
    elif argv[1].isalpha():
        exit("usage 'Python caesar.py n'")
    else:
        n = int(argv[1])
        while n > 26:
            n = n - 26
        userinput = get_string("plaintext: ")
        rotate(userinput, n)


def rotate(s, n):
    for i in range(len(s)):
        if s[i].isalpha():
            if ord(s[i]) > 96 and ord(s[i]) < 123:
                x = (ord(s[i]) + n)
                if x > 122:
                    x = x - 26
                s = s[:i] + chr(x) + s[i + 1:]
            else:
                x = (ord(s[i]) + n)
                if x > 90:
                    x = x - 26
                s = s[:i] + chr(x) + s[i + 1:]

    print(f"ciphertext: {s}")


main()