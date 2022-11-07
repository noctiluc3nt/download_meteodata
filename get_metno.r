#downloading observations from met.no
#based on: https://frost.met.no/r_example.html

library(jsonlite)
library(tidyr)

client_id=""

station="SN18700"
elements=c("air_temperature","air_pressure_sea_level","cloud_base_height", "precipitation_amount","wind_speed","wind_from_direction")
time=c("2022-11-04/2022-11-05")

#url to frost
endpoint=paste0("https://",client_id,"@frost.met.no/observations/v0.jsonld")
url = paste0(
    endpoint, "?",
    "sources=", station,
    "&referencetime=", time,
    "&elements=", elements
)
#request
xs = try(fromJSON(URLencode(url),flatten=T))

#check
if (class(xs) != 'try-error') {
    df = unnest(xs$data)
    print("Data retrieved from frost.met.no!")
} else {
    print("Error: the data retrieval was not successful!")
}

