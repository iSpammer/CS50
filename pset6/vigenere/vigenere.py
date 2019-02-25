from cs50 import get_string
from sys import argv


def main():
    checkin(argv)


def checkin(argv):
    if len(argv) != 2:
        exit("usage 'Python caesar.py n'")
    elif argv[1].isalpha() == False:
        exit("usage 'Python caesar.py n'")
    else:
        userinput = get_string("plaintext: ")
        rotate(userinput, argv[1].lower())


def rotate(s, n):
    j = 0
    for i in range(len(s)):
        if(j >= len(n)):
            j = 0
        key = fetchKey(n[j])
        if s[i].isalpha():
            if ord(s[i]) > 96 and ord(s[i]) < 123:
                x = (ord(s[i]) + key)
                if x > 122:
                    x = x - 26
                s = s[:i] + chr(x) + s[i + 1:]
            else:
                x = (ord(s[i]) + key)
                if x > 90:
                    x = x - 26
                s = s[:i] + chr(x) + s[i + 1:]
            j += 1
    print(f"ciphertext: {s}")


def fetchKey(n):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    return alpha.index(n)


main()