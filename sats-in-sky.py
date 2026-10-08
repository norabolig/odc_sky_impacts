########################################################################
# A.C. Boley (Norabolig)
########################################################################
#
# cc-by-sa 4.0
#
# If used for publication, please cite Boley, Lawler, and Rein et al. 2026 (full DOI coming)
# Produces sky brightness and other distribution plots
#
#
# numpy and sys import and quick definition
import sys
import numpy as np
twopi=2*np.pi
#
########################################################################
# Script control.
########################################################################
#
# First, select the ODC. Valid choices here are "stampede","sunrise", and "sxodc"
# Note, the sxodc takes a while due to the size. Suggest running in VERBOSE=True
# to track progress
ODC_name="sunrise"
HRANG=-6                                    # hours after midnight
LATPLOT=30                                  # latitude of interest
SUNLIT=1                                    #  include only sunlit satellites
TITLE= "Sunrise ODC, DS, 30˚N, 6 p.m."      # what you want your title to be
outfile="sunrise_ODC_ds_30_6pm"             # output nominclature
earthOverviewName="sunrise_Earth_map.png"   # globe output name. See globe controls below
CBAR_FILE_NAME="sunrise_cb.png"
phase_of_year = 0                           # 0 places everything at the December solsice. pi/2 is March equinox
                                            # pi is June solstice, 3pi/2 is September equinox

SUNSYNC_LIMIT = 90   # adjust sunsynchronous for precession. Set to unrealistic value if no adjustment at all
OVAR= 0              # variation of nodes in degrees, relative to centre set by OMEGA_0 (ODC specific)
                      
VERBOSE=False           # if you want a lot of output

ALTMIN_CBAR=500.             # minimum colourbar
ALTMAX_CBAR=1800.            # max colourbar
CB_SELF_ADJUST=True          # Ignore min and max altitude and plot based on distribution
ADD_COLORBAR=False           # plot the colourbar
MAKE_SEPARATE_COLORBAR =True # make separate colorbar
CMAP = "plasma"              # cmap for colourbar

#
########################################################################
# Controls for viewing the globe
########################################################################
#
VIEW_LON = -90.0   # Geographic centre for image
VIEW_SAT = 35.0    # Slightly North of the equator
VIEW_LAT = 35.0    # Compensated for tilt later
SAT_LON = -60      # Adjust effective rotation of Earth
ELMIN=0            # minimum elevation from horizon plotted

# use ifs to work with older python
if ODC_name == "stampede":
    OMEGA_0 = np.radians(102) - phase_of_year  # Local Time of Ascending Node in radians
                                               # Sun is on negative x axis, so use 102 instead of 282
elif ODC_name == "sunrise":
    OMEGA_0 = np.pi/2 - phase_of_year
elif ODC_name == "sxodc":
    OMEGA_0 = np.pi/2 - phase_of_year
else:
    print("Not a valid ODC for this setup. Check selection or modify as necessary")
    sys.exit()

# randomization control
np.random.seed(314)

########################################################################
# Following sets phase_of_year to 0 for December solstice.
# Only change if you know what you are dong
########################################################################
tilt_fac=-1

# Set plot range
lats=np.array([LATPLOT]) # in degrees
hours=np.array([HRANG]) # in hours

# if you need to check
if VERBOSE:
    print(lats)
    print(hours)

########################################################################
# Some further simulation controls
########################################################################

zeta=800*0.2                   # effective brightness
J2=1.08262668e-3
RE_km=6378.137 # km
wprec = 1.99096871e-7 # rad/s
MEarth = 5.97e24    # kg
RE_metre = RE_km*1000 # m
G=6.6743e-11
GM=G*MEarth

au_km=1.496e8
au=au_km*1e3

########################################################################
# Load some libraries
########################################################################

import KeplerTools as KT # this is my library
import numpy as np
import matplotlib.pylab as plt

########################################################################
# That tilt factor noted above is used here
# Basic sim control. "Tilt" is really the solar declination
########################################################################

tilt= np.radians(tilt_fac*23.4) # gotta put it in radians

########################################################################
# This is not intended to be confusing. But a choice was made to place
# the Sun on negative x axis, meaning we need to reverse the sign of the
# "tilt" to work out properly.
########################################################################
tilt*=-1

########################################################################
# Define satellite distrobution
# Number of planets, satellites per plane, inclination, altitude (km)
########################################################################

ICs=[]

# Data Centres

if ODC_name == "stampede":
        ICs.append({'NPLANES':1,'SATPP':645,'INC':98.200000,'ALT':700.000000 })
        ICs.append({'NPLANES':1,'SATPP':645,'INC':98.200000,'ALT':710.000000 })
        ICs.append({'NPLANES':1,'SATPP':645,'INC':98.300000,'ALT':720.000000 })
        ICs.append({'NPLANES':1,'SATPP':645,'INC':98.300000,'ALT':730.000000 })
        ICs.append({'NPLANES':1,'SATPP':645,'INC':98.300000,'ALT':740.000000 })
        ICs.append({'NPLANES':1,'SATPP':645,'INC':98.400000,'ALT':750.000000 })
        ICs.append({'NPLANES':1,'SATPP':645,'INC':98.400000,'ALT':760.000000 })
        ICs.append({'NPLANES':1,'SATPP':645,'INC':98.500000,'ALT':770.000000 })
        ICs.append({'NPLANES':1,'SATPP':645,'INC':98.500000,'ALT':780.000000 })
        ICs.append({'NPLANES':1,'SATPP':645,'INC':98.600000,'ALT':790.000000 })
        ICs.append({'NPLANES':1,'SATPP':645,'INC':98.600000,'ALT':800.000000 })
        ICs.append({'NPLANES':1,'SATPP':645,'INC':98.700000,'ALT':810.000000 })
        ICs.append({'NPLANES':1,'SATPP':645,'INC':98.700000,'ALT':820.000000 })
        ICs.append({'NPLANES':1,'SATPP':645,'INC':98.700000,'ALT':830.000000 })
        ICs.append({'NPLANES':1,'SATPP':645,'INC':98.800000,'ALT':840.000000 })
        ICs.append({'NPLANES':1,'SATPP':645,'INC':98.800000,'ALT':850.000000 })
        ICs.append({'NPLANES':1,'SATPP':645,'INC':98.900000,'ALT':860.000000 })
        ICs.append({'NPLANES':1,'SATPP':645,'INC':98.900000,'ALT':870.000000 })
        ICs.append({'NPLANES':1,'SATPP':645,'INC':99.000000,'ALT':880.000000 })
        ICs.append({'NPLANES':1,'SATPP':645,'INC':99.000000,'ALT':890.000000 })
        ICs.append({'NPLANES':1,'SATPP':645,'INC':99.000000,'ALT':900.000000 })
        ICs.append({'NPLANES':1,'SATPP':645,'INC':99.100000,'ALT':910.000000 })
        ICs.append({'NPLANES':1,'SATPP':645,'INC':99.100000,'ALT':920.000000 })
        ICs.append({'NPLANES':1,'SATPP':645,'INC':99.200000,'ALT':930.000000 })
        ICs.append({'NPLANES':1,'SATPP':645,'INC':99.200000,'ALT':940.000000 })
        ICs.append({'NPLANES':1,'SATPP':645,'INC':99.200000,'ALT':950.000000 })
        ICs.append({'NPLANES':1,'SATPP':645,'INC':99.300000,'ALT':960.000000 })
        ICs.append({'NPLANES':1,'SATPP':645,'INC':99.300000,'ALT':970.000000 })
        ICs.append({'NPLANES':1,'SATPP':645,'INC':99.400000,'ALT':980.000000 })
        ICs.append({'NPLANES':1,'SATPP':645,'INC':99.400000,'ALT':990.000000 })
        ICs.append({'NPLANES':1,'SATPP':650,'INC':99.500000,'ALT':1000.000000 })

elif ODC_name == "sunrise":
        ICs.append({'NPLANES':1,'SATPP':740,'INC':97.400000,'ALT':500.000000 })
        ICs.append({'NPLANES':1,'SATPP':740,'INC':97.400000,'ALT':510.300000 })
        ICs.append({'NPLANES':1,'SATPP':740,'INC':97.500000,'ALT':520.700000 })
        ICs.append({'NPLANES':1,'SATPP':740,'INC':97.500000,'ALT':531.000000 })
        ICs.append({'NPLANES':1,'SATPP':740,'INC':97.600000,'ALT':541.400000 })
        ICs.append({'NPLANES':1,'SATPP':740,'INC':97.600000,'ALT':551.700000 })
        ICs.append({'NPLANES':1,'SATPP':740,'INC':97.700000,'ALT':562.100000 })
        ICs.append({'NPLANES':1,'SATPP':740,'INC':97.700000,'ALT':572.400000 })
        ICs.append({'NPLANES':1,'SATPP':740,'INC':97.700000,'ALT':582.800000 })
        ICs.append({'NPLANES':1,'SATPP':740,'INC':97.800000,'ALT':593.100000 })
        ICs.append({'NPLANES':1,'SATPP':740,'INC':97.800000,'ALT':603.500000 })
        ICs.append({'NPLANES':1,'SATPP':740,'INC':97.900000,'ALT':613.800000 })
        ICs.append({'NPLANES':1,'SATPP':740,'INC':97.900000,'ALT':624.100000 })
        ICs.append({'NPLANES':1,'SATPP':740,'INC':97.900000,'ALT':634.500000 })
        ICs.append({'NPLANES':1,'SATPP':740,'INC':98.000000,'ALT':644.800000 })
        ICs.append({'NPLANES':1,'SATPP':740,'INC':98.000000,'ALT':655.200000 })
        ICs.append({'NPLANES':1,'SATPP':740,'INC':98.100000,'ALT':665.500000 })
        ICs.append({'NPLANES':1,'SATPP':740,'INC':98.100000,'ALT':675.900000 })
        ICs.append({'NPLANES':1,'SATPP':740,'INC':98.100000,'ALT':686.200000 })
        ICs.append({'NPLANES':1,'SATPP':740,'INC':98.200000,'ALT':696.500000 })
        ICs.append({'NPLANES':1,'SATPP':740,'INC':98.200000,'ALT':706.900000 })
        ICs.append({'NPLANES':1,'SATPP':740,'INC':98.300000,'ALT':717.200000 })
        ICs.append({'NPLANES':1,'SATPP':740,'INC':98.300000,'ALT':727.600000 })
        ICs.append({'NPLANES':1,'SATPP':740,'INC':98.300000,'ALT':737.900000 })
        ICs.append({'NPLANES':1,'SATPP':740,'INC':98.400000,'ALT':748.300000 })
        ICs.append({'NPLANES':1,'SATPP':740,'INC':98.400000,'ALT':758.600000 })
        ICs.append({'NPLANES':1,'SATPP':740,'INC':98.500000,'ALT':769.000000 })
        ICs.append({'NPLANES':1,'SATPP':740,'INC':98.500000,'ALT':779.300000 })
        ICs.append({'NPLANES':1,'SATPP':740,'INC':98.600000,'ALT':789.700000 })
        ICs.append({'NPLANES':1,'SATPP':740,'INC':98.600000,'ALT':800.000000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':98.700000,'ALT':810.000000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':98.700000,'ALT':820.200000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':98.700000,'ALT':830.500000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':98.800000,'ALT':840.700000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':98.800000,'ALT':850.900000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':98.900000,'ALT':861.200000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':98.900000,'ALT':871.400000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':99.000000,'ALT':881.600000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':99.000000,'ALT':891.900000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':99.100000,'ALT':902.100000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':99.100000,'ALT':912.300000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':99.200000,'ALT':922.600000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':99.200000,'ALT':932.800000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':99.300000,'ALT':943.000000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':99.300000,'ALT':953.300000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':99.300000,'ALT':963.500000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':99.400000,'ALT':973.700000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':99.400000,'ALT':984.000000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':99.500000,'ALT':994.200000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':99.500000,'ALT':1004.400000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':99.600000,'ALT':1014.600000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':99.600000,'ALT':1024.900000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':99.700000,'ALT':1035.100000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':99.700000,'ALT':1045.300000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':99.800000,'ALT':1055.600000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':99.800000,'ALT':1065.800000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':99.900000,'ALT':1076.000000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':99.900000,'ALT':1086.300000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':100.000000,'ALT':1096.500000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':100.000000,'ALT':1106.700000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':100.000000,'ALT':1117.000000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':100.100000,'ALT':1127.200000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':100.200000,'ALT':1137.400000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':100.200000,'ALT':1147.700000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':100.200000,'ALT':1157.900000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':100.300000,'ALT':1168.100000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':100.300000,'ALT':1178.400000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':100.400000,'ALT':1188.600000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':100.400000,'ALT':1198.800000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':100.500000,'ALT':1209.100000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':100.500000,'ALT':1219.300000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':100.600000,'ALT':1229.500000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':100.600000,'ALT':1239.800000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':100.700000,'ALT':1250.000000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':100.700000,'ALT':1260.000000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':100.800000,'ALT':1270.200000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':100.800000,'ALT':1280.400000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':100.900000,'ALT':1290.600000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':100.900000,'ALT':1300.800000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':101.000000,'ALT':1310.900000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':101.000000,'ALT':1321.100000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':101.100000,'ALT':1331.300000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':101.200000,'ALT':1341.500000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':101.200000,'ALT':1351.700000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':101.300000,'ALT':1361.900000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':101.300000,'ALT':1372.100000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':101.400000,'ALT':1382.300000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':101.400000,'ALT':1392.500000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':101.500000,'ALT':1402.600000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':101.500000,'ALT':1412.800000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':101.600000,'ALT':1423.000000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':101.700000,'ALT':1433.200000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':101.700000,'ALT':1443.400000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':101.800000,'ALT':1453.600000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':101.800000,'ALT':1463.800000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':101.900000,'ALT':1474.000000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':101.900000,'ALT':1484.200000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':102.000000,'ALT':1494.300000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':102.000000,'ALT':1504.500000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':102.100000,'ALT':1514.700000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':102.200000,'ALT':1524.900000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':102.200000,'ALT':1535.100000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':102.300000,'ALT':1545.300000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':102.300000,'ALT':1555.500000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':102.400000,'ALT':1565.700000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':102.400000,'ALT':1575.800000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':102.500000,'ALT':1586.000000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':102.500000,'ALT':1596.200000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':102.600000,'ALT':1606.400000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':102.700000,'ALT':1616.600000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':102.700000,'ALT':1626.800000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':102.800000,'ALT':1637.000000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':102.800000,'ALT':1647.200000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':102.900000,'ALT':1657.400000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':102.900000,'ALT':1667.500000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':103.000000,'ALT':1677.700000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':103.000000,'ALT':1687.900000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':103.100000,'ALT':1698.100000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':103.200000,'ALT':1708.300000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':103.200000,'ALT':1718.500000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':103.300000,'ALT':1728.700000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':103.300000,'ALT':1738.900000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':103.400000,'ALT':1749.100000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':103.400000,'ALT':1759.200000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':103.500000,'ALT':1769.400000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':103.500000,'ALT':1779.600000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':103.600000,'ALT':1789.800000 })
        ICs.append({'NPLANES':1,'SATPP':300,'INC':103.700000,'ALT':1800.000000 })

elif ODC_name == "sxodc":
        ICs.append({'NPLANES':30,'SATPP':333,'INC':32.000000,'ALT':550.000000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':31.300000,'ALT':552.000000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.700000,'ALT':554.000000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':556.000000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':29.300000,'ALT':558.000000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':28.700000,'ALT':560.000000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':28.000000,'ALT':562.000000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':27.300000,'ALT':564.000000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':26.700000,'ALT':566.000000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':26.000000,'ALT':568.000000 })
        ICs.append({'NPLANES':2,'SATPP':4999,'INC':97.700000,'ALT':565.000000 })
        ICs.append({'NPLANES':2,'SATPP':4999,'INC':97.700000,'ALT':567.200000 })
        ICs.append({'NPLANES':2,'SATPP':4999,'INC':97.700000,'ALT':569.400000 })
        ICs.append({'NPLANES':2,'SATPP':4999,'INC':97.700000,'ALT':571.700000 })
        ICs.append({'NPLANES':2,'SATPP':4999,'INC':97.700000,'ALT':573.900000 })
        ICs.append({'NPLANES':2,'SATPP':4999,'INC':97.700000,'ALT':576.100000 })
        ICs.append({'NPLANES':2,'SATPP':4999,'INC':97.700000,'ALT':578.300000 })
        ICs.append({'NPLANES':2,'SATPP':4999,'INC':97.700000,'ALT':580.600000 })
        ICs.append({'NPLANES':2,'SATPP':4999,'INC':97.700000,'ALT':582.800000 })
        ICs.append({'NPLANES':2,'SATPP':4999,'INC':97.700000,'ALT':585.000000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':686.000000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':687.300000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':688.700000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':690.000000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':691.300000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':692.700000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':694.000000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':695.300000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':696.700000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':698.000000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':699.300000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':700.700000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':702.000000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':703.300000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':704.700000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':706.000000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':707.300000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':708.700000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':710.000000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':711.300000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':712.700000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':714.000000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':715.300000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':716.700000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':718.000000 })
        ICs.append({'NPLANES':2,'SATPP':5565,'INC':97.200000,'ALT':707.000000 })
        ICs.append({'NPLANES':2,'SATPP':5565,'INC':97.200000,'ALT':708.800000 })
        ICs.append({'NPLANES':2,'SATPP':5565,'INC':97.200000,'ALT':710.500000 })
        ICs.append({'NPLANES':2,'SATPP':5565,'INC':97.200000,'ALT':712.300000 })
        ICs.append({'NPLANES':2,'SATPP':5565,'INC':97.200000,'ALT':714.000000 })
        ICs.append({'NPLANES':2,'SATPP':5565,'INC':97.200000,'ALT':715.800000 })
        ICs.append({'NPLANES':2,'SATPP':5565,'INC':97.200000,'ALT':717.600000 })
        ICs.append({'NPLANES':2,'SATPP':5565,'INC':97.200000,'ALT':719.300000 })
        ICs.append({'NPLANES':2,'SATPP':5565,'INC':97.200000,'ALT':721.100000 })
        ICs.append({'NPLANES':2,'SATPP':5565,'INC':97.200000,'ALT':722.900000 })
        ICs.append({'NPLANES':2,'SATPP':5565,'INC':97.200000,'ALT':724.600000 })
        ICs.append({'NPLANES':2,'SATPP':5565,'INC':97.200000,'ALT':726.400000 })
        ICs.append({'NPLANES':2,'SATPP':5565,'INC':97.200000,'ALT':728.100000 })
        ICs.append({'NPLANES':2,'SATPP':5565,'INC':97.200000,'ALT':729.900000 })
        ICs.append({'NPLANES':2,'SATPP':5565,'INC':97.200000,'ALT':731.700000 })
        ICs.append({'NPLANES':2,'SATPP':5565,'INC':97.200000,'ALT':733.400000 })
        ICs.append({'NPLANES':2,'SATPP':5565,'INC':97.200000,'ALT':735.200000 })
        ICs.append({'NPLANES':2,'SATPP':5565,'INC':97.200000,'ALT':737.000000 })
        ICs.append({'NPLANES':2,'SATPP':5565,'INC':97.200000,'ALT':738.700000 })
        ICs.append({'NPLANES':2,'SATPP':5565,'INC':97.200000,'ALT':740.500000 })
        ICs.append({'NPLANES':2,'SATPP':5565,'INC':97.200000,'ALT':742.200000 })
        ICs.append({'NPLANES':2,'SATPP':5565,'INC':97.200000,'ALT':744.000000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':946.000000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':947.300000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':948.700000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':950.000000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':951.300000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':952.700000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':954.000000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':955.300000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':956.700000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':958.000000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':959.300000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':960.700000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':962.000000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':963.300000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':964.700000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':966.000000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':967.300000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':968.700000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':970.000000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':971.300000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':972.700000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':974.000000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':975.300000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':976.700000 })
        ICs.append({'NPLANES':30,'SATPP':333,'INC':30.000000,'ALT':978.000000 })
        ICs.append({'NPLANES':2,'SATPP':5770,'INC':99.400000,'ALT':967.000000 })
        ICs.append({'NPLANES':2,'SATPP':5770,'INC':99.400000,'ALT':968.700000 })
        ICs.append({'NPLANES':2,'SATPP':5770,'INC':99.400000,'ALT':970.300000 })
        ICs.append({'NPLANES':2,'SATPP':5770,'INC':99.400000,'ALT':972.000000 })
        ICs.append({'NPLANES':2,'SATPP':5770,'INC':99.400000,'ALT':973.700000 })
        ICs.append({'NPLANES':2,'SATPP':5770,'INC':99.400000,'ALT':975.300000 })
        ICs.append({'NPLANES':2,'SATPP':5770,'INC':99.400000,'ALT':977.000000 })
        ICs.append({'NPLANES':2,'SATPP':5770,'INC':99.400000,'ALT':978.700000 })
        ICs.append({'NPLANES':2,'SATPP':5770,'INC':99.400000,'ALT':980.300000 })
        ICs.append({'NPLANES':2,'SATPP':5770,'INC':99.400000,'ALT':982.000000 })
        ICs.append({'NPLANES':2,'SATPP':5770,'INC':99.400000,'ALT':983.700000 })
        ICs.append({'NPLANES':2,'SATPP':5770,'INC':99.400000,'ALT':985.300000 })
        ICs.append({'NPLANES':2,'SATPP':5770,'INC':99.400000,'ALT':987.000000 })
        ICs.append({'NPLANES':2,'SATPP':5770,'INC':99.400000,'ALT':988.700000 })
        ICs.append({'NPLANES':2,'SATPP':5770,'INC':99.400000,'ALT':990.300000 })
        ICs.append({'NPLANES':2,'SATPP':5770,'INC':99.400000,'ALT':992.000000 })
        ICs.append({'NPLANES':2,'SATPP':5770,'INC':99.400000,'ALT':993.700000 })
        ICs.append({'NPLANES':2,'SATPP':5770,'INC':99.400000,'ALT':995.300000 })
        ICs.append({'NPLANES':2,'SATPP':5770,'INC':99.400000,'ALT':997.000000 })
        ICs.append({'NPLANES':2,'SATPP':5770,'INC':99.400000,'ALT':998.700000 })
        ICs.append({'NPLANES':2,'SATPP':5770,'INC':99.400000,'ALT':1000.300000 })
        ICs.append({'NPLANES':2,'SATPP':5770,'INC':99.400000,'ALT':1002.000000 })

else:
        print("Enter your ODC ICs")
        sys.exit()

lats = np.radians(np.array(lats)) # convert to rad
hang = hours*twopi/24. # convert to rad for solar hour angle
if VERBOSE:
    print("Latitude bin size {}˚ and hour bin size {} hr".format( np.degrees(lats[1]-lats[0]),((hang[1]-hang[0])*24/twopi)  ))

# rotation fun time. Place observer at a reference location and then rotate
xobs0 = RE_metre*1
yobs0 = 0.
zobs0 = 0.

# these will be x-y-z positions for lighted (xl) and all (xa) satellites
xl=[]
yl=[]
zl=[]
xa=[]
ya=[]
za=[]

# used for satellite count output
count = np.zeros( (len(lats),len(hang)))

# helper functions
def precess(a_km):
    '''Calculate inclination needed for sunsyncronous orbits given altitude)'''
    mmot = np.sqrt(GM/(1000*a_km)**3)
    return np.arccos(  -2*wprec*(a_km/RE_km)**2/(3*J2*mmot))
    
def RotateZ(x,y,z,a):
    xp = x*np.cos(a)-y*np.sin(a)
    yp = x*np.sin(a)+y*np.cos(a)
    return xp,yp,z

def RotateY(x,y,z,a):
    xp=x*np.cos(a)+z*np.sin(a)
    zp=-x*np.sin(a)+z*np.cos(a)
    return xp,y,zp
    
def airMass(ele):
    ''' Airmass function Kasten and Young 1989'''
    z = 90-ele
    X = 1/(np.cos(np.radians(z)) + 0.50572*(6.07995+90-z)**(-1.6364))
    return X


#
########################################################################
# Now look through ICs and place satellites
########################################################################
#
evenodd=0
for ic in ICs:
   nplanes=ic['NPLANES']
   nsat=ic['SATPP']
   ntot=nplanes*nsat
   sma = (ic['ALT']+RE_km)/au_km # will put it back into metres
   if VERBOSE:
       print("Number of sats {}".format(nsat))
       print(ic['INC'],np.degrees(precess(sma*au_km)))
   ic_use = ic['INC']

   for iplane in range(nplanes):
        if ic_use > SUNSYNC_LIMIT:
            ic_use = np.degrees(precess(sma*au_km))
            if evenodd==0:
                Omega = OMEGA_0  # iplane*dplane+dplane_ran
                if ODC_name == "stampede": evenodd=0
                else: evenodd=1
            else:
                Omega = OMEGA_0 + np.pi
                evenodd=0
        else:
            Omega = np.random.uniform()*2*np.pi
        if OVAR > 0: Omega+=np.radians(OVAR)*(1-2*np.random.uniform(0,1))
        if VERBOSE: print("Plane Omega {} rad and evenodd {}".format(Omega,evenodd))
        for ilocal in range(nsat):

              manom = np.array(2*np.pi*np.random.uniform(0,1))
              x0,y0,z0,vx,vy,vz = KT.getXYZVVV(manom,sma,0,0,Omega,np.radians(ic_use),m0=MEarth,m1=0.)
              x0*=au  # putting back into metres
              y0*=au
              z0*=au

              x_tmp,y_tmp,z_tmp= RotateY(x0,y0,z0,tilt) # rotating satellites to compensate for solar declination
              x,y,z= RotateZ(x_tmp,y_tmp,z_tmp,phase_of_year) # rotating satellites to compensate for solar declination
              xa.append(x)
              ya.append(y)
              za.append(z)
              OK=1
              if np.sqrt(y*y+z*z)<RE_metre:   # are they in shadow?
                if x > 0: OK=0
              if OK:
                xl.append(x)    # these are sunlit
                yl.append(y)
                zl.append(z)


print("Total number of sats placed is {}".format(len(xa)))
print("Total number of illuminated satellites is {}".format(len(xl)))

xl=np.array(xl)
yl=np.array(yl)
zl=np.array(zl)

if not SUNLIT:
    xl=np.array(xa)    # sometimes, we do not care whether they are sunlit
    yl=np.array(ya)
    zl=np.array(za)

########################################################################
# Now define the pole and rotate it to the phase of year
########################################################################

pole_tmp = np.array(RotateY(0,0,1,tilt))
pole = np.array(RotateZ(pole_tmp[0],pole_tmp[1],pole_tmp[2],phase_of_year))

#
########################################################################
# Step through latitudes and hours, rotate the observer, and view sky
# This is built from a previous loop, but we only go through the loop
# once by design. So it remains a snapshot. But I am keeping the loop
# for now because it could be advantageous for changes down the road
########################################################################
#
for ilat,lat in enumerate(lats):
    # again, need to reverse sign of lat tilt so positive latitude lifts up
    # put observer at desired latitude
    xobs1,yobs1,zobs1 = RotateY(xobs0,yobs0,zobs0,-lat)
    if VERBOSE: print("Pole is ",pole)
    for ihr,hr in enumerate(hang):
        azarr_deg=[]
        altarr_deg=[]
        phaseArray=[]
        mags=[]
        # move observer by rotation of hours from midnight
        xobs2,yobs2,zobs2= RotateZ(xobs1,yobs1,zobs1,hr-phase_of_year)
        # need to compensate for solar declination (due to distribution of satellites)
        xobs3,yobs3,zobs3= RotateY(xobs2,yobs2,zobs2,tilt)
        xobs,yobs,zobs = np.array(RotateZ(xobs3,yobs3,zobs3,phase_of_year))

        satx =xl-xobs
        saty =yl-yobs
        satz =zl-zobs
            
        obslen = np.sqrt(xobs**2+yobs**2+zobs**2) # vector length for observer
                                                  # if altitude added not necessarily RE_metre
        satlen = np.sqrt(satx**2+saty**2+satz**2) # range of satellite
        dotprod = xobs*satx+yobs*saty+zobs*satz # used below for altitude
        obspos = np.array([xobs,yobs,zobs]) # observer position vector
        obspos_unit = obspos/obslen

        # here we make lots of projections
        
        # sun is on the -x axis. Just unit vector
        sunpos=np.array([-1,0,0])
        
        # python vector gymnastics for vector operations
        satstack = np.column_stack((satx,saty,satz))

        satpos_unit=satstack*1
        satpos_unit[:,0]=satstack[:,0]/satlen[:]
        satpos_unit[:,1]=satstack[:,1]/satlen[:]
        satpos_unit[:,2]=satstack[:,2]/satlen[:]
        
        # negative of observerxpole gives east
        east = np.cross(-obspos_unit,pole)
        # north will be normal to east and obspos
        north = np.cross(obspos_unit,east)
        #
        # first get a normal to the observer and satellite-observer unit vectors
        # And then get the azimuth vector by finding the cross of that
        # and the observer vector
        #
        satcross = np.cross(obspos_unit,satpos_unit)
        azvec = -np.cross(obspos_unit,satcross)
          
        # But to know the angle of the azimuth vector, we need to know
        # the azimuth relative to north and east, which breaks directional ambiguity
        # so project onto north and east and then arctan2 it
        # paranoid about being unit vectors
        az_ncv = np.inner(north,azvec)/(np.linalg.norm(north)*np.linalg.norm(azvec))
        az_ecv = np.inner(east,azvec)/(np.linalg.norm(east)*np.linalg.norm(azvec))
        azarr_deg = np.degrees(np.arctan2(az_ecv,az_ncv))
        
        # fix wrapping
        flag = azarr_deg < 0
        azarr_deg[flag]+=360

        # get the satellite phase angle as seen by the observer
        phaseArray = np.pi - np.arccos(np.inner(satpos_unit,sunpos))

        # altitude is easy now. Just angle between observer and satellite
        # which is actually zenith angle. So subtract from 90
        try:
           angle_rad = np.abs(np.arccos(dotprod/(obslen*satlen)))
           altarr_deg=(90-np.degrees(angle_rad))
        except:
           print("Strange. Zenith angle not found")
           print("Recovering by skipping")
           print("Check dotprod {} and obslen {} and satlen {}".format(dotprod,obslen,satlen))
           continue

# now have frozen the quantities from the last loop
   
# lambertian sphere approximation
mags = -26.77 -2.5*np.log10( 2*zeta/(3*np.pi**2)*( (np.pi-phaseArray)*np.cos(phaseArray)+np.sin(phaseArray)) )+5*np.log10(satlen) + 0.15*airMass(altarr_deg)

# Experimental for now
Flux = 300*10**(0.4*(-26.77-mags))  # This should calibrate for V band
totalflux = np.sum(Flux[altarr_deg>0])
if VERBOSE: print("(Experimental. Needs to be vetted. Total flux {} W/m^2".format(totalflux))

##########################################################
# count satellites in the sky
##########################################################

flag = mags[altarr_deg>0] < 5
print("Total satellites in sky (above 0 deg) with mag < 5 is {}".format(np.sum(flag)))

flag = altarr_deg > ELMIN

print("Total above {} deg {}".format(ELMIN,np.sum(flag)))

v7=0
v6=0
v5=0
v4=0
v3=0
v2=0
v1=0
v0=0

for i in range(len(mags)):
    if not flag[i]: continue
    if mags[i] < 7: v7+=1
    if mags[i] < 6: v6+=1
    if mags[i] < 5: v5+=1
    if mags[i] < 4: v4+=1
    if mags[i] < 3: v3+=1
    if mags[i] < 2: v2+=1
    if mags[i] < 1: v1+=1
    if mags[i] < 0: v0+=1

print("N V < 7: {}".format(v7))
print("N V < 6: {}".format(v6))
print("N V < 5: {}".format(v5))
print("N V < 4: {}".format(v4))
print("N V < 3: {}".format(v3))
print("N V < 2: {}".format(v2))
print("N V < 1: {}".format(v1))
print("N V < 0: {}".format(v0))


##########################################################
# Plot some projections for a sanity check
# These plots are not saved
##########################################################


plt.figure()
plt.title("X-Z Sunlit Satellite Projection")
plt.scatter(xl/RE_metre,zl/RE_metre,s=1)
plt.xlabel("x [RE]")
plt.ylabel("z [RE]")
plt.xlim([-1.4,1.4])
plt.ylim([-1.4,1.4])

fig=plt.figure()
plt.title("X-Y Sunlit Satellite Projection")
plt.xlabel("x [RE]")
plt.ylabel("y [RE]")
plt.scatter(xl/RE_metre,yl/RE_metre,s=1)
plt.xlim([-1.4,1.4])
plt.ylim([-1.4,1.4])

##########################################################
# Plot Cartesian sky map
##########################################################


fig=plt.figure()
plt.title(TITLE)
plt.xlabel("Azimuth [deg]")
plt.ylabel("Altitude [deg]")
plt.scatter(azarr_deg[flag],altarr_deg[flag],s=0.5,c="black")
plt.savefig(outfile+"_altaz.png")

##########################################################
# Plot sky map with polar projection
##########################################################

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.set_rlim(90,0)
ax.set_facecolor('gray')
cb=ax.scatter(azarr_deg[flag]*np.pi/180,altarr_deg[flag],s=0.5,c=mags[flag],cmap='hot_r',vmin=0,vmax=8)
cbar=plt.colorbar(cb,pad=0.1)
cbar.set_label("Magnitude V (LSM)")
ax.set_rticks([10,20,30,40,50,60,70,80,90],labels=[])  # Less radial ticks
ax.set_theta_zero_location("N")
ax.set_theta_direction(1)
ax.set_title(TITLE)
ax.grid(True)
plt.savefig(outfile+".png",dpi=300)

ax.grid(True)

##########################################################
# Plot Mollweide total sky projection (above and below horizon)
##########################################################

import cartopy.crs as ccrs
from cartopy.mpl.ticker import LatitudeFormatter, LongitudeFormatter
import matplotlib.ticker as mticker

fig=plt.figure(figsize=[15,8])
ax=plt.axes(projection=ccrs.Mollweide())
ax.set_global()
gl=ax.gridlines(draw_labels=True,xlocs=[-180,-120, -60, 0, 60, 120,180], ylocs=[-75,-60,-45, -30, -15, 0, 15, 30, 45, 60, 75])


standard_lat_formatter = LatitudeFormatter()
def custom_lat_labels(value, pos):
    if abs(value-15) < 0.1:return "15˚"
    elif value==30:return "30˚"
    elif value==45:return "45˚"
    elif value==60:return "60˚"
    elif value==75:return "75˚"
    elif abs(value+15)<0.1:return "-15˚"
    elif value==-30:return "-30˚"
    elif value==-45:return "-45˚"
    elif value==-60:return "-60˚"
    elif value==-75:return "-75˚"
    else:
        return standard_lat_formatter(value)

standard_lon_formatter = LongitudeFormatter()
def custom_lon_labels(value, pos):
    if value==-180:return "0˚"
    elif value==-120:return "60˚"
    elif value==-60:return "120˚"
    elif value==0:return "180˚"
    elif value==60:return "240˚"
    elif value==120:return "300˚"
    elif value==180:return "360˚"
    else:
        return standard_lon_formatter(value)



poly = ax.scatter(azarr_deg,altarr_deg,s=0.1,transform=ccrs.PlateCarree(central_longitude=180),c='blue',alpha=0.75)

gl.yformatter = mticker.FuncFormatter(custom_lat_labels)
gl.xformatter = mticker.FuncFormatter(custom_lon_labels)

plt.title(TITLE)
plt.savefig(outfile+"_mollweide.png")


##########################################################
# Plot satellites around Earth for perspective
# Assembled and modified from lots of examples
##########################################################


# Convert perspective center to radians
lambda_0 = np.radians(VIEW_LON)
lambda_sat = np.radians(SAT_LON)
phi_sat_0 = np.radians(VIEW_SAT)
phi_lat_0 = np.radians(VIEW_LAT)

from mpl_toolkits.mplot3d import Axes3D
import urllib.request
from PIL import Image

def project_orthographic(lon_rad, lat_rad, radius, lambda_0, phi_0):
    """
    Transforms spherical coordinate parameters into 2D plane coordinates (x_p, y_p)
    using an Orthographic Projection matrix centered at (lambda_0, phi_0).
    Also returns a visibility mask for points on the front hemisphere.
    """
    # Angular distance component from perspective center
    cos_c = np.sin(phi_0) * np.sin(lat_rad) + np.cos(phi_0) * np.cos(lat_rad) * np.cos(lon_rad - lambda_0)
    
    # 2D Planar positions scaled by radius
    x_p = radius * np.cos(lat_rad) * np.sin(lon_rad - lambda_0)
    y_p = radius * (np.cos(phi_0) * np.sin(lat_rad) - np.sin(phi_0) * np.cos(lat_rad) * np.cos(lon_rad - lambda_0))
    z_p = radius * (np.cos(phi_0) * np.sin(lat_rad) - np.sin(phi_0) * np.cos(lat_rad) * np.sin(lon_rad - lambda_0))
    
    # cos_c >= 0 flags points located on the visible front face of the hemisphere
    visible_mask = (cos_c >=0) + (np.sqrt(x_p**2 + y_p**2) >= RE_km )
    return x_p, y_p, z_p, visible_mask


# Convert satellite inputs to spherical components first
# Need to position the satellites back to something that works with the map

xlp,ylp,zlp= RotateZ(xl,yl,zl,-phase_of_year)
xl,yl,zl= RotateY(xlp,ylp,zlp,-tilt)
xlm,ylm,zlm= RotateZ(xl,yl,zl,phase_of_year)
 
sat_r = np.sqrt(xlm*xlm + ylm*ylm + zlm*zlm) # values in metres
sat_lon_rad = np.arctan2(ylm, xlm)
sat_lat_rad = np.arcsin(zlm / sat_r)
sat_r_km=sat_r/1e3 # put into km

# Transform satellite vectors into flat planar components
sat_xp, sat_yp, sat_zp, sat_visible = project_orthographic(sat_lon_rad, sat_lat_rad, sat_r_km, lambda_sat, phi_sat_0)
calculated_altitudes = sat_r_km - RE_km


##########################################################
# Download earth map for overlaying with image
# Modified from example code produced by Gemini
##########################################################

url = "https://eoimages.gsfc.nasa.gov/images/imagerecords/73000/73909/world.topo.bathy.200412.3x5400x2700.jpg"
print("Processing Orthographic background transformation...")
try:
    with urllib.request.urlopen(url) as response:
        img = Image.open(response).resize((720, 360))
        bm = np.array(img) / 255.0
except Exception as e:
    print(f"Texture load failed ({e}). Falling back to solid circle backdrop.")
    bm = None

# Create a flattened mesh grid matching the map pixel points
lons = np.linspace(-180, 180, 720) * np.pi / 180
lats = np.linspace(90, -90, 360) * np.pi / 180  # Inverted to match image row index direction
lons_grid, lats_grid = np.meshgrid(lons, lats)

# Project map pixels into orthogonal space
map_xp, map_yp, map_zp, map_visible = project_orthographic(lons_grid, lats_grid, RE_km, lambda_0, phi_lat_0)


# final image
fig, ax = plt.subplots(figsize=(10, 10),layout="tight")

# Draw the projected texture background
if bm is not None:
    # Blend texture with visibility mask to create a clean circle boundary disk
    # Behind-horizon map pixels are masked to transparent RGBA sequences
    rgba_map = np.zeros((360, 720, 4))
    rgba_map[..., :3] = bm
    rgba_map[..., 3] = map_visible.astype(float)
    
    # Use pcolormesh to draw the warped map array seamlessly
    ax.pcolormesh(map_xp, map_yp, rgba_map, shading='auto', zorder=1)
else:
    # Fallback shaded disk representation if download fails
    earth_disk = plt.Circle((0, 0), RE_km, color="royalblue", alpha=0.7, zorder=1)
    ax.add_patch(earth_disk)

# Plot space background horizon edge line
horizon_outline = plt.Circle((0, 0), RE_km, color="white", fill=False, linewidth=1, linestyle="--", alpha=0.3, zorder=2)
ax.add_patch(horizon_outline)

# Filter out behind-the-earth satellites so they don't show through continents
visible_xp = sat_xp[sat_visible]
visible_yp = sat_yp[sat_visible]
visible_zp = sat_zp[sat_visible]
visible_alts = calculated_altitudes[sat_visible]

sorted_indices = np.argsort(visible_zp)

# Scatter plot the remaining foreground satellites
if CB_SELF_ADJUST==True:
    ALTMIN_CBAR=visible_alts.min()
    ALTMAX_CBAR=visible_alts.max()
    
scatter = ax.scatter(
    visible_xp[sorted_indices],
    visible_yp[sorted_indices],
    #c="red",
    c=visible_alts[sorted_indices],
    cmap=CMAP,
    s=20,
    vmin=ALTMIN_CBAR,vmax=ALTMAX_CBAR,
    edgecolor="black",
    linewidth=0.1,
    zorder=3
)

if ADD_COLORBAR==True:
    from mpl_toolkits.axes_grid1 import make_axes_locatable
    section = make_axes_locatable(ax)
    cax = section.append_axes("right",size="3%",pad=0.1)
    fig.colorbar(scatter,cax=cax,label="Altitude [km]")#,orientation="horizontal")
    
# Figure Formatting
max_view_range = 9000
ax.set_xlim(-max_view_range, max_view_range)
ax.set_ylim(-max_view_range, max_view_range)
ax.set_aspect('equal')
ax.axis('off')
plt.savefig(earthOverviewName)
    
if MAKE_SEPARATE_COLORBAR==True:
    import matplotlib.colors as mcolors
    import matplotlib.cm as cm
    fig,ax=plt.subplots(figsize=(6,1))
    norm = mcolors.Normalize(vmin=ALTMIN_CBAR,vmax=ALTMAX_CBAR)
    mappable = cm.ScalarMappable(norm=norm,cmap=CMAP)
    cbar=fig.colorbar(mappable,cax=ax,orientation="horizontal")
    cbar.ax.tick_params(labelsize=14)
    cbar.set_label('Altitutde [km]',size=14)
    plt.tight_layout()
    plt.savefig(CBAR_FILE_NAME)


plt.show()
