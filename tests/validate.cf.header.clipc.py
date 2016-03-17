# validate cf-convention header
import netCDF4
import numpy as np

# KNMI clipc
# author: andrej
# clipc@knmi.nl

url1 =  'http://opendap.knmi.nl/knmi/thredds/dodsC/CLIPC/tier1_indicators/icclim_cerfacs/TNn/MPI-M-MPI-ESM-LR_rcp85_r1i1p1_SMHI-RCA4_v1/TNn_OCT_MPI-M-MPI-ESM-LR_rcp85_r1i1p1_SMHI-RCA4_v1_EUR-11_2006-2100.nc'

nc1 = netCDF4.Dataset(url1,'r')

# test if ncattrs is on global attribute list.
for k in nc1.ncattrs():
	print k , ": " , nc1.getncattr(k)