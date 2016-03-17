# python
# clipc combine process with dispel4py
# combine two netCDFs
# knmi team
# author: andrej / alessandro
# clipc@knmi.nl
#

#import netCDF4
import xarray  
import netCDF4

import random
import numpy as operator
import wcsrequest
import numpy as np

def defaultCallback(message,percentage):
  print "defaultCallback: "+message



def collect(url):
# print "in collector ",url
  
  # old
  #nc = netCDF4.Dataset(url,'r')
  
  # new
  # data set is loaded into memory
  nc = xarray.open_dataset(url)

  # data set is loaded into memory
  # xarray.decode_cf()
  return nc;



def read(nc):
#print "in read ", str(nc)
  print type(nc)

  nc.load()

  # NOTE: major change between netcdf4 and xarray is that one uses netattrs and the new lib uses attrs()
  #print "ANDREJ ", dir(nc)
  print "ANDREJ ", nc
  print "ANDREJ ", nc.attrs
  print "ANDREJ ", nc.data_vars

  variableName = getTitleNC(nc)
  print "TITLE:",variableName

  v[:] = nc.variables[variableName][:]

  # normalisation
  n = v.max()

  return (v, n)



#def write(nc,outName,des):
def write(url,outName,des):
#print "in preprocess nc is     ",str(nc)
  print "in preprocess output is ",outName
  print "in preprocess des       ",des

  nc =  collect(url)

  variable = getTitleNC(nc)

#  print "in preprocess variable name is " , variable

  nc_combo = copyNetCDF( outName , nc , des )


  return (nc_combo, variable)


def combine(  var1, norm1 , var2 , norm2 , operator_symbol ):
#  print "in preprocess ",var1, " ",norm1
#  print "in preprocess ",var2, " ",norm2

  ops = { "+": operator.add , 
          "-": operator.subtract, 
          "*": operator.multiply, 
          "/": operator.divide  }

# nc_combination , combi_name = combine_two_indecies_netcdf(nc1, nc2, operation, output,callback=callback)
# callback("combo time received: "+str(netCDF4.num2date( nc_combination.variables['time'][0] , nc_combination.variables['time'].units ,calendar='standard')),3)
# parse operator symbol to function
  op_char = operator_symbol
  op_func = ops[op_char]

  combo = op_func( np.divide(var1 , norm1) , np.divide( var2 , norm2) )


  return combo


def postprocess(combi_variable,nc_combo_file): #,operation):

  print "in postprocess ", type(combi_variable)

  nc_combo_file[0].variables[nc_combo_file[1]][:]   =  combi_variable

  print "in postprocess ", type(nc_combo_file[0])

  return nc_combo_file

def getTitleNC(nc_fid):
#  print str(nc_fid)
  var = None
  for k, v in nc_fid.data_vars.iteritems():
    print v.attrs
    if "grid_mapping" in v.attrs.keys():  var = k

  return var


# copy existing netcdf to new file with name
#
def copyNetCDF(name, nc_fid , des ):

  print ""
  print ""
  print nc_fid
  print ""
  #w_nc_fid = netCDF4.Dataset(name, 'w', format='NETCDF4')
  w_nc_fid = nc_fid.to_netcdf()

  #print w_nc_fid

  #w_nc_fid.description = des

  # print "ANDREJDEBUG"
  # print type(w_nc_fid)
  # print type(nc_fid)

  # print ""
  # print "DIMS"
  # print type(nc_fid.dims)
  # for d in nc_fid.dims.items(): print d

  # print ""
  # print "COORDS"
  # print type(nc_fid.coords)
  # for c in nc_fid.coords.items(): print c

  # print ""
  # print "VARS"
  # print type(nc_fid.data_vars)
  # for v in nc_fid.data_vars.items(): print v

  # print ""
  # print "ATTRS"
  # print type(nc_fid.attrs)
  # for a in nc_fid.attrs.items(): print a



  # dims
  #for var_name, dimension in nc_fid.dims:
  # for dim in nc_fid.dims: 
  #   print dim
  #   w_nc_fid.createDimension( dim, len(dimension) if not dimension.isunlimited() else None)

  # # coords

  # # vars
  # for var_name, ncvar in nc_fid.data_vars:

  #   outVar = w_nc_fid.createVariable(var_name, ncvar.datatype, ncvar.dimensions )
  
  #   ad = dict((k , ncvar.attrs[k] ) for k in ncvar.attrs() )

  #   outVar.setncatts(  ad  )

  #   outVar[:] = ncvar[:]

  # # attrs

  # global_vars = dict((k , nc_fid.attrs[k] ) for k in nc_fid.attrs() )
  
  # for k in sorted(global_vars.keys()):
  #   w_nc_fid.setncattr(  k , global_vars[k]  )

  return w_nc_fid
# end copy
