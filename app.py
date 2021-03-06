import pandas as pd
import glob
import time
from config import powitanie, pozegnanie

powitanie()
time.sleep(5)

path = r'D:\Ptx Converter\Zlecenie'
all_files = glob.glob(path + "/*.PTX")

li = []

column_names = []
for i in range(31):
    x = "column " + str(i)
    column_names.append(x)

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=None, skiprows=3, sep=',',
                     error_bad_lines=False, encoding='latin1', names=list(column_names))
    li.append(df)

df = pd.concat(li, axis=0, ignore_index=True)


# for column in df.columns:
#             df[column] = df[column].astype("str")
#                                    .str.normalize('NFKD')
#                                    .str.encode('ascii', errors='ignore')
#                                    .str.decode('utf-8')


df['column 3'] = (df['column 3'].astype("str")
                        .str.normalize('NFKD')
                        .str.encode('ascii', errors='ignore')
                        .str.decode('US-ASCII')
                        .str.replace("ciana", "Sciana")
                        .str.replace("grny", "gorny")
                        .str.replace("Pka", "polka"))

df_req = (df.loc[df['column 0'] == 'PARTS_REQ'])
df_inf = (df.loc[df['column 0'] == 'PARTS_INF'])


# column_names_2 = []
# for i in range(31):
#     x = "column x" + str(i)
#     column_names_2.append(x)
# df_inf.columns = list(column_names_2)


df_inf = df_inf.reset_index(drop=True)
df_req = df_req.reset_index(drop=True)

unnecesary_columns = [0, 1, 4, 35, 36, 37, 48, 61]
for i in range(7, 34):
    unnecesary_columns.append(i)
for i in range(43, 47):
    unnecesary_columns.append(i)
for i in range(51, 59):
    unnecesary_columns.append(i)

column_names2 = ['linia w ptx',
                 'Nazwa',
                 'Dlugosc',
                 'Szerokosc',
                 'Typ',
                 'Numer Zlecenia',
                 'Okleina 1',
                 'Okleina 2',
                 'Okleina 3',
                 'Okleina 4',
                 'Nazwa Zlecenia',
                 'Material',
                 'LP w F5',
                 'CNC1',
                 'CNC2']

if len(df_inf) == len(df_req):
    df_summary = pd.concat([df_req, df_inf], axis=1, ignore_index=True).drop(columns=unnecesary_columns)
    df_final = df_summary.reset_index(drop=True).sort_values(by=3).reset_index(drop=True)
    df_final.columns = column_names2
    df_final.to_excel(r'D:/PTX Converter/Raport.xlsx', index=True)
else:
    print("error")


# if len(df_inf) == len(df_req):
#     df_summary = pd.merge(df_req, df_inf, left_index=True, right_index=True).to_csv(r'G:/df_summary.csv', index=True)

# if len(df_inf) == len(df_req):
#     df_summary = df_req.join(df_inf).to_csv(r'G:/df_summary.csv', index=True)

pozegnanie()
time.sleep(5)