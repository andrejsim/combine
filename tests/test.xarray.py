# xarray 
import pandas
import xarray
import netCDF4


for k in dir(xarray): print k

url = '../example/vDTR_JUN_MPI-M-MPI-ESM-LR_rcp85_r1i1p1_SMHI-RCA4_v1_EUR-11_2006-2100.nc'

#print url
#nc_op = netCDF4.Dataset(url,'r')
#print nc_op

# open_dataset required for reading opendap... see http://xarray.pydata.org/en/stable/io.html#io
nc_ds = xarray.open_dataset(url)
print nc_ds


nc_ds.to_netcdf('saved_on_disk.nc')