#!/usr/bin/python3
def uppercase(str):
    new = ""
    for i in range(len(str)):
        if (ord(str[i]) >= 97 and ord(str[i]) <= 122):
            new += chr(ord(str[i]) - 32)
            continue
        new += str[i]
    print("{0}".format(new))
