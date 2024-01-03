n = int(input("Enter number: "))

def daraja(n):
    if n > 1023 and n < 2048:
        print("10 1024")

    elif n > 511 and n < 1024:
        print("9 512")

    elif n > 255 and n < 512:
        print("8 256")

    elif n > 127 and n < 256:
        print("7 128")

    elif n > 63 and n < 127:
        print("6 64")

    elif n > 2**5 and n < 2**6:
        print("5 32")

    elif n > 15 and n < 33:
        print("4 16")

    elif n > 7 and n < 16:
        print("3 8")

    elif n < 8 and n > 3:
        print("2 4")

    else:
        print("exceeded")


daraja(n)
