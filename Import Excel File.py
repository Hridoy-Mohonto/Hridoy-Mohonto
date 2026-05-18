import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
df = pd.read_excel(r"C:\Users\Hridoy Mohonto\Downloads\sold.xlsx")
print(df)