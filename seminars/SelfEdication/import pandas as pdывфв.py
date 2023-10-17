import pandas as pd

data = {"op": "K", "pk": {"NKVT": "0", "NVAG": 0, "DATE_DEPARTURE": "2020-01-25"}, "ts": "2020-01-25T16:03:10.422+03:00", "data": {"IDE": 0, "TEO": None, "TID": "0", "GKPR": 0, "GKPT": "0", "KCEH": 0, "KDSM": 0, "KDST": 0, "TARF": 0.0, "VESV": 0.0, "TARFE": None, "TARFP": None, "VESDO": 0.0, "TARFDL": None, "VOZNOP": None, "ST_TIME": None, "TARFDLP": None, "DATE_ARR": None, "COST_CONT": None, "NKVT_FULL": "0", "RATE_CONT": None, "COST_TRUCK": None, "DATE_STAMP": "2000-01-27 11:00:00", "RATE_TRUCK": None, "ROUTE_SIGN": 0, "CLIENT_CODE": None, "COST_TRUCK_P": None, "DATE_ACCFACT": None, "DATE_DELIVERY": None, "CONTAINER_CODE": None, "CONTAINER_NUMBER": None, "DATVRM_DEPARTURE": "2999-08-24 17:51:00", "INSIDE_INVOICE_NUMBER": None}

df = pd.DataFrame.from_dict(data, orient='index').T
print(df)