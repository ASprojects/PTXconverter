import pandas as pd

df = pd.read_csv('G:/000067_001_EG_PB_H3331_ST10_18.ptx',
                 header=None, skiprows=3, sep=',', error_bad_lines=False, names=list(range(31)))

df.to_csv(r'G:/Test.csv', index=False)

