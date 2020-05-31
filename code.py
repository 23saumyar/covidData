import pandas as pd

file_path = "SDGData.xlsx"
df = pd.read_excel(file_path, encoding='utf-16')
print(df)
df.to_dict()
print(df)
countriesConstant = {} #{country:{density:100,Hospital Beds:100, Senior Population:.5,	Arrivals - Tourism:100,	Population Below Poverty Line:50}}

