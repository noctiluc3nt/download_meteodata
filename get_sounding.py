#downloading soundings from University of Wyoming (no quality control)
#old: https://weather.uwyo.edu/upperair/sounding.html
#new: https://weather.uwyo.edu/upperair/bufrraob.shtml

import urllib3
from bs4 import BeautifulSoup
import numpy as np

#station id
#station_id="01004" #Ny-Alesund, Norway
#station_id="01028" #Bjornoya, Norway
#station_id="01010" #Andoya, Norway
#station_id="01241" #Orland, Norway
#station_id="01415" #Stavanger, Norway
#station_id="02836" #Sodankyla, Finland
station_id="10393" #Lindenberg, Germany

#date/time
year="2022"
mon="01"
day="01"
hour="00" #"12"

#download
http=urllib3.PoolManager()
url='http://weather.uwyo.edu/cgi-bin/sounding?region=naconf&TYPE=TEXT%3ALIST&YEAR='+year+'&MONTH='+mon+'&FROM='+day+hour+'&TO='+day+hour+'&STNM='+station_id
response=http.request('GET', url)
soup=BeautifulSoup(response.data.decode('utf-8'),'lxml')
data_text=soup.get_text()
splitted=data_text.split("\n",data_text.count("\n"))

#write output
file_out='{}_{}{}{}-{}.txt'.format(station_id,year,mon,day,hour)
f=open(file_out,'w')
for i in range(np.shape(splitted)[0]):
	f.write(splitted[i]+"\n")
	
f.close()


