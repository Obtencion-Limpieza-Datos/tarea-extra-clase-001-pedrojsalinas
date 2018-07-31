import pandas as pd
import pandas.io.sql as pd_sql
import sqlite3

#Conexion
conn = sqlite3.connect("database.db")
#lee csv
data = pd.read_csv('data/lugares-turisticos.csv',low_memory=False)
#dataframe to sqlite
data.to_sql('turisticos', conn, if_exists='replace', index=False)
