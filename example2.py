# python
from clipc_combine_process import clipc_combine_process 
from clipc_combine_process import serve_netcdf
from os.path import expanduser
home = expanduser("~")
# this does not work as it is contains a header for the WMS process..self.
wcs_url1 = 'https://climate4impact.eu/impactportal/ImpactService?source=http://opendap.knmi.nl/knmi/thredds/dodsC/CLIPC/tier1_indicators/icclim_cerfacs/CDD/MPI-M-MPI-ESM-LR_rcp45_r1i1p1_SMHI-RCA4_v1/CDD_JAN_MPI-M-MPI-ESM-LR_rcp45_r1i1p1_SMHI-RCA4_v1_EUR-11_2006-2100.nc'
wcs_url2 = 'https://climate4impact.eu/impactportal/ImpactService?source=http://opendap.knmi.nl/knmi/thredds/dodsC/CLIPC/tier1_indicators/icclim_cerfacs/CDD/MPI-M-MPI-ESM-LR_rcp45_r1i1p1_SMHI-RCA4_v1/CDD_MAR_MPI-M-MPI-ESM-LR_rcp45_r1i1p1_SMHI-RCA4_v1_EUR-11_2006-2100.nc'
time1 = 'current' #None
time2 = 'current' #None

# this does not work as it is contains a header for the WMS process..self.
#wcs_url1 = 'http://climate4impact.eu/impactportal/ImpactService?source=http://opendap.knmi.nl/knmi/thredds/dodsC/CLIPC/tier1_indicators/icclim_cerfacs/CDD/MPI-M-MPI-ESM-LR_rcp45_r1i1p1_SMHI-RCA4_v1/CDD_JAN_MPI-M-MPI-ESM-LR_rcp45_r1i1p1_SMHI-RCA4_v1_EUR-11_2006-2100.nc'
#wcs_url2 = 'http://climate4impact.eu/impactportal/ImpactService?source=http://opendap.knmi.nl/knmi/thredds/dodsC/CLIPC/tier1_indicators/icclim_cerfacs/CDD/MPI-M-MPI-ESM-LR_rcp45_r1i1p1_SMHI-RCA4_v1/CDD_MAR_MPI-M-MPI-ESM-LR_rcp45_r1i1p1_SMHI-RCA4_v1_EUR-11_2006-2100.nc'
wcs_url1 =	'http://climate4impact.eu/impactportal/ImpactService?source=http://opendap.knmi.nl/knmi/thredds/dodsC/CLIPC/tier1_indicators/icclim_cerfacs/vDTR/MPI-M-MPI-ESM-LR_rcp45_r1i1p1_SMHI-RCA4_v1-SMHI-DBS43-MESAN-1989-2010/vDTR_OCT_MPI-M-MPI-ESM-LR_rcp45_r1i1p1_SMHI-RCA4_v1-SMHI-DBS43-MESAN-1989-2010_EUR-11_2006-2100.nc'
wcs_url2 =  'http://climate4impact.eu/impactportal/ImpactService?source=http://opendap.knmi.nl/knmi/thredds/dodsC/CLIPC/tier1_indicators/icclim_cerfacs/TNn/MPI-M-MPI-ESM-LR_rcp85_r1i1p1_SMHI-RCA4_v1/TNn_OCT_MPI-M-MPI-ESM-LR_rcp85_r1i1p1_SMHI-RCA4_v1_EUR-11_2006-2100.nc'

bbox = '-40,20,60,50' #None
time1 = '2010-10-16T00:00:00Z' #None
time2 = '1989-09-16T00:00:00' #None
certfile = home+'/certs/creds.pem'

nc1 , nc2 , nc_combo = clipc_combine_process.combine_two_indecies_wcs(wcs_url1, 
	wcs_url2,  
	"*" , 
	"normnone" , 
	"normminmax" , 
	bbox , time1 , 
	time2 , 
	'wcs_nc1.nc' , 
	'wcs_nc2.nc', 
	'wcs_combine.nc' ,
	certfile=certfile )

serve_netcdf.visualise(nc1, nc2, nc_combo)




