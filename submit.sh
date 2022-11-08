#!/bin/bash

#SBATCH --partition=cipI
#SBATCH --ntasks=1
#SBATCH --job-name=download_data

module load python
pip3 install cdsapi

python3 get_era5.py
#python3 get_carra.py

