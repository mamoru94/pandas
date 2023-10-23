import pandas as pd
import psycopg2

# Connect to the database
conn = psycopg2.connect(database="etl", user="etl", password="password", host="localhost", port="5432")

# Read the Excel file into a pandas dataframe
df = pd.read_excel("C:/Users/a.aleksandrov.CORP/Downloads/0000l3transportdbnlmktogr1.xlsx")
df = pd.info()
# Insert the dataframe into the database
#df.to_sql(name="loaderexcel", con=conn, if_exists="replace", index=False)

# Close the database connection
conn.close()