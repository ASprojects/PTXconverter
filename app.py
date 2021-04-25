import pandas as pd
import glob

path = r'G:\Convert'
all_files = glob.glob(path + "/*.PTX")

li = []

column_names = []
for i in range(31):
    x = "column " + str(i)
    column_names.append(x)

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=None, skiprows=3, sep=',',
                     error_bad_lines=False, names=list(column_names))
    li.append(df)

df = pd.concat(li, axis=0, ignore_index=True)

df_req = (df.loc[df['column 0'] == 'PARTS_REQ'])
df_inf = (df.loc[df['column 0'] == 'PARTS_INF'])


# column_names_2 = []
# for i in range(31):
#     x = "column x" + str(i)
#     column_names_2.append(x)
# df_inf.columns = list(column_names_2)


df_inf = df_inf.reset_index(drop=True)
df_req = df_req.reset_index(drop=True)

unnecesary_columns = [0, 1, 4, 61]
for i in range(7, 33):
    unnecesary_columns.append(i)
for i in range(43, 47):
    unnecesary_columns.append(i)
for i in range(51, 59):
    unnecesary_columns.append(i)

if len(df_inf) == len(df_req):
    df_summary = pd.concat([df_req, df_inf], axis=1, ignore_index=True).drop(columns=unnecesary_columns)
    df_summary.sort_values(by=3).reset_index(drop=True).to_excel(r'G:/df_summary.xlsx', index=True)
else:
    print("error")


# if len(df_inf) == len(df_req):
#     df_summary = pd.merge(df_req, df_inf, left_index=True, right_index=True).to_csv(r'G:/df_summary.csv', index=True)

# if len(df_inf) == len(df_req):
#     df_summary = df_req.join(df_inf).to_csv(r'G:/df_summary.csv', index=True)
