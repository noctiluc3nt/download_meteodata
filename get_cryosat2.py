#!/usr/bin/python3

#downloading CryoSat2 ice thickness data (Arctic)

import sys
import cdsapi

c = cdsapi.Client()

c.retrieve("satellite-sea-ice-thickness",
	{
		"version": "2_0",
		"variable": "all",
		"satellite": "cryosat_2",
		"cdr_type": "icdr",
		"year": "2021",
		"month": "02",
		"format": "tgz"
	}, "cyosat2_out.nc")
