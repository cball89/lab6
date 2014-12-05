#Caroline Ball
#GIS501

#Chapter 10-Exercise 1 Bookwork 


import arcpy

from arcpy import env
env.workspace = "E:/EsriPress/Python/Data/Exercise10"

mxd = arcpy.mapping.MapDocument("E:/EsriPress/Python/Data/Exercise10/
Austin_TX.mxd")

#ist the parks                                
df = arcpy.mapping.ListDataFrames(mxd, "Parks")[0]
lyr = arcpy.mapping.ListLayers(mxd, "parks", df)[0]
dflist = arcpy.mapping.ListDataFrames(mxd)

#add layers to a map                                
for dframe in dflist:
if dframe.name <> "Parks":
arcpy.mapping.AddLayer(dframe, lyr)
mxd.save()
del mxd
