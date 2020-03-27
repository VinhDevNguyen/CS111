def BT2(X):
    temp = 0 # clear temp;
    Z = 0 # clear Z;
    while X != 0: # while X not 0 do
        temp += 1 # clear temo;
        C = 0 # clear C;
        # (Z = Z + temp)
        while temp != 0: # while temp not 0 do
            Z += 1 # incr Z;
            C += 1 # icre C;
            temp -= 1 # decr temp;
        # end;
        while C != 0: # while C not 0 do 
            temp += 1 # incr temp;
            C -= 1 # decr C;
        # end;
        X -= 1 # decr X;
    # end;
    return Z
print(BT2(5)) # = 15