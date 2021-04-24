import pandas as pd
import glob

path = r'G:\Convert'
all_files = glob.glob(path + "/*.PTX")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=None, skiprows=3, sep=',', error_bad_lines=False, names=list(range(31)))
    li.append(df)

df = pd.concat(li, axis=0, ignore_index=True)

df.to_csv(r'G:/Test.csv', index=False)