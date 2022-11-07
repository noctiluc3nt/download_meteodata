#!/bin/bash

#SBATCH --partition=cipI
#SBATCH --ntasks=1
#SBATCH --job-name=download_data

module load python

python3 get_era5.py


