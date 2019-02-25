from cs50 import get_string
from sys import argv


def main():
    words = checkIn()
    bleep(get_string("What message would you like to censor? \n"), words)


def checkIn():
    if len(argv) != 2:
        print("Usage: python bleep.py dictionary")
        exit(1)
    else:
        with open(argv[1]) as f:
            content = f.readlines()
        return [x.strip() for x in content]


def bleep(msgs, ban):
    s = ""
    msgs = msgs.split(" ")
    for msg in msgs:
        if msg.lower() in ban:
            for i in range(len(msg)):
                s = s + "*"
            s = s + " "
        else:
            s = s + str(msg)+" "
    print(s)


if __name__ == "__main__":
    main()
