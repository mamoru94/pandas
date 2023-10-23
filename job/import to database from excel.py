import pandas as pd
from sqlalchemy import create_engine
engine=create_engine('postgresql+psycopg2://etl:password@localhost:5432/etl')
with pd.ExcelFile('C:/Users/a.aleksandrov.CORP/Downloads/0000l3transportdbnlmktogr2.xlsx') as xls:
	df=pd.read_excel(xls)
	df.to_sql(name='exp_table',con=engine,if_exists='append',index=False)