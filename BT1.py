def Multiple(X, Z=0):
    Y = 0
    temp = 0
    while X != 0:
        Y += 1
        temp += 1
        X -= 1
    while temp != 0:
        X += 1
        temp -= 1

    while X != 0:
        W = 0
        while Y != 0:
            Z += 1
            W += 1
            Y -= 1
        while W != 0:
            Y += 1
            W -= 1
        X -= 1
    return Z

def main():
    print(Multiple(5))
if __name__ == "__main__":
    main()
