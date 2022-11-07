#!/usr/bin/python3

#downloading hourly ERA5 reanalysis on pressure levels

import sys
import cdsapi

c = cdsapi.Client()

c.retrieve("reanalysis-era5-pressure-levels",
	{
		"variable": ["geopotential", "temperature", "potential_vorticity", "vorticity", "u_component_of_wind","v_component_of_wind","vertical_velocity", "specific_humidity","specific_cloud_liquid_water_content","specific_cloud_ice_water_content"],
		"pressure_level": ["500","300"],
		"product_type": "reanalysis",
		"year": "2021",
		"month": "02",
		"day": "07",
		"time": ["00:00","06:00","12:00","18:00"],
		"area": "80.00/-40.00/30.00/20.00",
		"format": "netcdf"
	}, "era5_out.nc")
