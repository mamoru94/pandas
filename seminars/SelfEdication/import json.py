import json
import psycopg2
import pandas as pd
# Connect to the PostgreSQL database
conn = psycopg2.connect(database="etl", user="etl", password="password", host="localhost", port="5432")
# Создание курсора
cur = conn.cursor()

data = {"op": "U", "pk": {"NKVT": "99992509", "NVAG": 54901715, "DATE_DEPARTURE": "2023-09-25"}, "ts": "2023-09-25T16:03:10.422+03:00", "data": {"IDE": 0, "TEO": 0, "TID": "19620230925160309374534", "GKPR": 421034, "GKPT": "220", "KCEH": 60, "KDSM": 1, "KDST": 592100, "TARF": 0.0, "VESV": 0.0, "TARFE": 0, "TARFP": 0, "VESDO": 0.0, "TARFDL": 0, "VOZNOP": 0, "ST_TIME": 0, "TARFDLP": 0, "DATE_ARR": 0, "COST_CONT": 0, "NKVT_FULL": "99992509", "RATE_CONT": 0, "COST_TRUCK": 0, "DATE_STAMP": "2023-09-25 16:03:00", "RATE_TRUCK": 0, "ROUTE_SIGN": 5, "CLIENT_CODE": 0, "COST_TRUCK_P": 0, "DATE_ACCFACT": 0, "DATE_DELIVERY": 0, "CONTAINER_CODE": 0, "CONTAINER_NUMBER": 0, "DATVRM_DEPARTURE": "2023-09-25 15:59:00", "INSIDE_INVOICE_NUMBER": 0}}
data = { "op": data["op"], "ts": data["ts"], **data["pk"], **data["data"]}

 

# создание view на основе данных
view_data = []
for d in data:
    view_data.append((d['id'], d['name'], d['description']))


cur.close()
conn.close()