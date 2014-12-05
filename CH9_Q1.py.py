#Caroline Ball
#GIS501

#Chapter 9-Exercise 1 Bookwork 

import arcpy

from arcpy import env
from arcpy.sa import *
env.workspace = "E:/EsriPress/Python/Data/Exercise09"

#IF statement
if arcpy.CheckExtension("Spatial") == "Available":    
arcpy.CheckOutExtension("Spatial")
elev = arcpy.Raster("elevation")
lc = arcpy.Raster("landcover.tif")
slope = Slope(elev)
aspect = Aspect(elev)
goodslope = ((slope > 5) & (slope < 20))
goodaspect = ((aspect > 150) & (aspect < 270))
goodland = ((lc == 41) | (lc == 42) | (lc ==43))

#Output data
outraster = (goodslope & goodaspect & goodland)
outraster.save("E:/EsriPress/Python/Data/Exercise09/Results/final")
arcpy.CheckInExtension("Spatial")
