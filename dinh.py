# this python file to check whether wrong - label image has been saved in database

import requests
import psycopg2


conn = psycopg2.connect(" dbname=mariana user=postgres password=5432 ")
cur = conn.cursor()

query = f"SELECT * FROM retrain;"

cur.execute(query)

data = cur.fetchall()[-1]

wrong_label = data[1]

image_path = data[2]

print(wrong_label,image_path,sep='\n')

conn.close()