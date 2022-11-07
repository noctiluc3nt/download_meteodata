#downloading observations from met.no
#based on: https://frost.met.no/python_example.html

import requests
import pandas as pd

client_id="" #client id from frost

station="SN18700"
elements=["air_temperature","air_pressure_sea_level","cloud_base_height", "precipitation_amount","wind_speed","wind_from_direction"]
time=["2022-11-04/2022-11-05"]


endpoint="https://frost.met.no/observations/v0.jsonld"

request=requests.get(endpoint, {
	"sources": station,
	"referencetime":time,
	"elements":elements,
	}, auth=(client_id,""))

json=request.json()
data=json["data"]

df = pd.DataFrame()
for i in range(len(data)):
    row = pd.DataFrame(data[i]['observations'])
    row['referenceTime'] = data[i]['referenceTime']
    row['sourceId'] = data[i]['sourceId']
    df = df.append(row)

df = df.reset_index()
