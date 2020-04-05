def ReadFile(FileName):
    try:
        with open(FileName, encoding='utf8', errors='ignore') as file:
            list = file.readlines()
    except FileNotFoundError as identifier:
        print("Không tìm thấy file")
    else:
        import numpy as np
        arr = np.array(list)
        return arr
