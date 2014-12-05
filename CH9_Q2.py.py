#Caroline Ball
#GIS501

#Chapter 9-Exercise 2 Bookwork


import arcpy

from arcpy import env
out_path = "E:/EsriPress/Python/Data/Exercise09"
env.workspace = out_path

#list rasters
rasterlist = arcpy.ListRasters()

arcpy.CreatePersonalGDB_management(out_path + "/Results", "myrasters.
gdb")

# statement for raster                                   
for raster in rasterlist:
desc = arcpy.Describe(raster)
rname = desc.baseName
                                   
outraster = out_path + "/Results/myrasters.gdb/" + rname                                   
arcpy.CopyRaster_management(raster, outraster)
