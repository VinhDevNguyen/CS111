# %%
from Function import ReadFile
file =  ReadFile('syllables.txt')

# %%
for index in range(len(file)):
    file[index] = file[index][:-1]

# %%
file[0:5]

# %%
lenght = []
for index_len in range(len(file)):
    lenght.append(len(file[index_len]))

# %%
lenght[0:5]

# %%
import pandas as pd
df = pd.DataFrame(list(zip(file, lenght)), columns =['String', 'Lenght'])

# %%
df

# %%
FirstString = []
for index_First_String in range(len(file)):
    FirstString.append(file[index_First_String][:1])

# %%
FirstString[0:5]

# %%
df = pd.DataFrame(list(zip(file, lenght, FirstString)), columns =['String', 'Lenght', 'First_String'])

# %%
df

# %%
test = ReadFile('input.txt')

# %%
fsdf = df[df["First_String"] == test[0][:1]]

# %%
ldf = fsdf[fsdf["Lenght"] == len(test[0])]

# %%
strdf = df[df["First_String"] == test[0][:1]]