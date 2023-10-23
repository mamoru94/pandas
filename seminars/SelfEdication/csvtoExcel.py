import pandas as pd

# Read the CSV file
df = pd.read_csv('C:/Users/a.aleksandrov.CORP/Downloads/exc/newdec.csv')
# Read the excel file
# df = pd.read_excel('C:/Users/a.aleksandrov.CORP/Downloads/exc/Z.xlsx')

# Export to Excel file
df.to_excel('C:/Users/a.aleksandrov.CORP/Downloads/exc/output.xlsx', index=False)
# Export to Excel file
# df.to_csv('C:/Users/a.aleksandrov.CORP/Downloads/exc/output.csv', index=False)
