def Multiple(X): 
    Z = 0 # clear Z
    Y = 0 # clear Y
    temp = 0 # Clear temp
    # Y = X
    while X != 0: # while X not 0 do
        Y += 1 # incr Y
        temp += 1 # incr temp
        X -= 1 # decr X
    while temp != 0: # while temp not 0 do
        X += 1 # incr X
        temp -= 1 # decr temp
    # Z = X * Y
    while X != 0: # while X not 0 do
        W = 0 # clear W
        while Y != 0: # while Y not 0 do
            Z += 1 # incr Z
            W += 1 # incr W
            Y -= 1 # decr Y
        while W != 0: # while W not 0 do
            Y += 1 # incr Y
            W -= 1 # decr W
        X -= 1 # decr X
    return Z

def main():
    print(Multiple(5))
if __name__ == "__main__":
    main()
