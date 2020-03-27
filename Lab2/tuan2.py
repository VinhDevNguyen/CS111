def main():
    import pandas as pd 
    import numpy as np

    syllables=pd.read_csv('syllables.txt',header=None)
    bao=pd.read_csv('bao2.txt',header=None)
    syllables = np.asarray(syllables)
    bao = np.asarray(bao)
    for index in range(0,len(bao)):
        bao[index][0] = bao[index][0].upper()
    no_dupes = [x for n, x in enumerate(bao) if x not in bao[:n]]
    count = 0
    for language_Index in range(0, syllables.shape[0]):
        for no_dupes_Index in range(0, len(no_dupes)):
            if syllables[language_Index][0] == no_dupes[no_dupes_Index][0]:
                count = count + 1
    print(count)

import time
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))