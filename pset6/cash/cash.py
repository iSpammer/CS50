from cs50 import get_float


def main():
    n = checkin("Change owed: ")
    print(cash(n*100))


def checkin(s):
    while True:
        n = get_float(s)
        if n > 0:
            return n


def cash(n):
    i = 0
    while n >= 25:
        n -= 25
        i += 1
    while n >= 10:
        n -= 10
        i += 1
    while n >= 5:
        n -= 5
        i += 1
    while n >= 1:
        n -= 1
        i += 1
    return i


main()