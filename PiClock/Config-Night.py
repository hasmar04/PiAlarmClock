from GoogleMercatorProjection import LatLng
from PyQt4.QtGui import QColor


# LOCATION(S)
# Further radar configuration (zoom, marker location) can be
# completed under the RADAR section
primary_coordinates = -27.574413, 152.883959  # Change to your Lat/Lon

location = LatLng(primary_coordinates[0], primary_coordinates[1])
primary_location = LatLng(primary_coordinates[0], primary_coordinates[1])
noaastream = 'http://www.urberg.net:8000/tim273/edina'
background = 'images/code-wallpaper.png'
squares1 = 'images/squares1-green.png'
squares2 = 'images/squares2-green.png'
icons = 'icons-darkgreen'
textcolor = '#206225'
clockface = 'images/clockface3-darkgreen.png'
hourhand = 'images/hourhand-darkgreen.png'
minhand = 'images/minhand-darkgreen.png'
sechand = 'images/sechand-darkgreen.png'


digital = 1             # 1 = Digtal Clock, 0 = Analog Clock

# Goes with light blue config (like the default one)
digitalcolor = "#154018"
digitalformat = "{0:%H:%M}"  # The format of the time
digitalsize = 250
# The above example shows in this way:
#  https://github.com/n0bel/PiClock/blob/master/Documentation/Digital%20Clock%20v1.jpg
# ( specifications of the time string are documented here:
#  https://docs.python.org/2/library/time.html#time.strftime )

# digitalformat = "{0:%I:%M}"
# digitalsize = 250
#  The above example shows in this way:
#  https://github.com/n0bel/PiClock/blob/master/Documentation/Digital%20Clock%20v2.jpg

usemapbox = 1   # Use Mapbox.com for maps, needs api key (mbapi in ApiKeys.py)
metric = 1  # 0 = English, 1 = Metric
radar_refresh = 10      # minutes
weather_refresh = 30    # minutes
# Wind in degrees instead of cardinal 0 = cardinal, 1 = degrees
wind_degrees = 0

# gives all text additional attributes using QT style notation
# example: fontattr = 'font-weight: bold; '
fontattr = ''

# These are to dim the radar images, if needed.
# see and try Config-Example-Bedside.py
dimcolor = QColor('#103125')
dimcolor.setAlpha(192)

# Language Specific wording
# DarkSky Language code
#  (https://darksky.net/dev/docs under lang=)
Language = "EN"

# The Python Locale for date/time (locale.setlocale)
#  '' for default Pi Setting
# Locales must be installed in your Pi.. to check what is installed
# locale -a
# to install locales
# sudo dpkg-reconfigure locales
DateLocale = ''

# Language specific wording
LPressure = "Pressure "
LHumidity = "Humidity "
LWind = "Wind "
Lgusting = " gusting "
LFeelslike = "Feels like "
LPrecip1hr = " Precip 1hr:"
LToday = "Today: "
LSunRise = "Sun Rise:"
LSet = " Set: "
LMoonPhase = " Moon Phase:"
LInsideTemp = "Inside Temp "
LRain = " Rain: "
LSnow = " Snow: "
Lmoon1 = 'New Moon'
Lmoon2 = 'Waxing Crescent'
Lmoon3 = 'First Quarter'
Lmoon4 = 'Waxing Gibbous'
Lmoon5 = 'Full Moon'
Lmoon6 = 'Waning Gibbous'
Lmoon7 = 'Third Quarter'
Lmoon8 = 'Waning Crecent'

# RADAR
# By default, primary_location entered will be the
#  center and marker of all radar images.
# To update centers/markers, change radar sections below the desired lat/lon as:
# -FROM-
# primary_location,
# -TO-
# LatLng(44.9764016,-93.2486732),
radar1 = {
    'center': primary_location,  # the center of your radar block
    'zoom': 7,  # this is a maps zoom factor, bigger = smaller area
    'style': 'mapbox/satellite-streets-v10',  # optional style (mapbox only)
    'markers': (   # google maps markers can be overlayed
        {
            'location': primary_location,
            'color': 'red',
            'size': 'small',
            'image': 'teardrop-dot',  # optional image from the markers folder
        },          # dangling comma is on purpose.
    )
}


radar2 = {
    'center': primary_location,
    'zoom': 5,
    'markers': (
        {
            'location': primary_location,
            'color': 'red',
            'size': 'small',
        },
    )
}


radar3 = {
    'center': primary_location,
    'zoom': 7,
    'markers': (
        {
            'location': primary_location,
            'color': 'red',
            'size': 'small',
        },
    )
}

radar4 = {
    'center': primary_location,
    'zoom': 5,
    'markers': (
        {
            'location': primary_location,
            'color': 'red',
            'size': 'small',
        },
    )
}
