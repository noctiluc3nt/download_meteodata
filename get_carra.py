#!/usr/bin/python3

#downloading CARRA reanalysis on model levels

import sys
import cdsapi

c = cdsapi.Client()

c.retrieve("reanalysis-carra-model-levels",
	{
		"variable": ["temperature", "u_component_of_wind","v_component_of_wind","turbulent_kinetic_energy"],
		"model_level": ["1","2","10","20","30","40","50","60"],
		"domain": "west_domain",
		"product_type": "analysis",
		"year": "2021",
		"month": "02",
		"day": "07",
		"time": "00:00",
		"format": "netcdf"
	}, "carra_out.nc")
