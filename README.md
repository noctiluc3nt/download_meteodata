# Download meteorological data from different sources

Scripts:
- get_carra.py: downloading CARRA reanalysis on model levels
- get_cryosat2.py: downloading monthly sea ice thickness derived from CryoSat2
- get_era5.py: downloading ERA5 reanalysis on pressure levels
- get_metno.py: downloading station observations from met.no
- get_metno.r: downloading station observations from met.no
- get_sounding.py: downloading soundings (radiosonde) from UWyo
- submit.sh: submit slurm job

Sources:
- Copernicus (via https://cds.climate.copernicus.eu/#!/home)
- DWD (via https://opendata.dwd.de/)
- METno (via https://frost.met.no/index.html)
- UWyo (via https://weather.uwyo.edu/upperair/sounding.html)

Download from THREDDS:
`wget -e robots=off -nH --cut-dirs 4 -nc -r -l5 -A '*.nc' -R 'catalog*' -I /thredds/fileServer/,/thredds/catalog/ 'https://thredds.met.no//thredds/fileServer/aromearcticlatest/archive/arome_arctic_det_2_5km_20221105T15Z.nc` 
<br>
or with Python: see, e.g.: https://github.com/steingod/downloadfromthredds <br><br>


Contact: laura.mack@fu-berlin.de

