# -*- coding: utf-8 -*-


import json
import time
from tle_calculator import TLECalculator
from datetime import datetime

print datetime.now().strftime('%Y/%m/%d %H:%M:%S')

tle = json.loads("""
{
      "APOGEE": "405.444", 
      "ARG_OF_PERICENTER": "66.0858", 
      "BSTAR": "6.4654e-05", 
      "CLASSIFICATION_TYPE": "U", 
      "COMMENT": "GENERATED VIA SPACETRACK.ORG API", 
      "ECCENTRICITY": "0.0001882", 
      "ELEMENT_SET_NO": "999", 
      "EPHEMERIS_TYPE": "0", 
      "EPOCH": "2016-04-22 14:29:07", 
      "EPOCH_MICROSECONDS": "829376", 
      "FILE": "2024236", 
      "INCLINATION": "51.6458", 
      "INTLDES": "98067A", 
      "MEAN_ANOMALY": "321.3", 
      "MEAN_MOTION": "15.54307507", 
      "MEAN_MOTION_DDOT": "0", 
      "MEAN_MOTION_DOT": "3.83e-05", 
      "NORAD_CAT_ID": "25544", 
      "OBJECT_ID": "1998-067A", 
      "OBJECT_NAME": "ISS (ZARYA)", 
      "OBJECT_NUMBER": "25544", 
      "OBJECT_TYPE": "PAYLOAD", 
      "ORDINAL": "1", 
      "ORIGINATOR": "JSPOC", 
      "PERIGEE": "402.891", 
      "PERIOD": "92.645", 
      "RA_OF_ASC_NODE": "335.2834", 
      "REV_AT_EPOCH": "99633", 
      "SEMIMAJOR_AXIS": "6782.303", 
      "TLE_LINE0": "0 ISS (ZARYA)", 
      "TLE_LINE1": "1 25544U 98067A   16113.60356284  .00003830  00000-0  64654-4 0  9999", 
      "TLE_LINE2": "2 25544  51.6458 335.2834 0001882  66.0858 321.3000 15.54307507996337"
    }
""")

cal = TLECalculator(tle)
#cal.calculate_ra_dec(time.time()-32400)
cal.calculate_ra_dec(time.time())
#cal.calculate_ra_dec(time.time()+32400)
print ""


"""
http://www.infra.kochi-tech.ac.jp/takagi/Geomatics/5Estimation2.pdf
の通りの結果が出る
"""

tle_2 = json.loads("""
      {"ARG_OF_PERICENTER": "14.7699", 
      "ECCENTRICITY": "0.0001679", 
      "EPOCH": "2006-04-30 17:20:48", 
      "INCLINATION": "98.2104", 
      "MEAN_ANOMALY": "345.3549", 
      "MEAN_MOTION": "14.59544429", 
      "MEAN_MOTION_DDOT": "0", 
      "MEAN_MOTION_DOT": "0.00000232", 
      "PERIGEE": "402.891", 
      "PERIOD": "92.645", 
      "RA_OF_ASC_NODE": "195.1270"}
""")

cal = TLECalculator(tle_2)
t = int(time.mktime(time.strptime("2006-05-15 11:00:00", "%Y-%m-%d %H:%M:%S")))
cal.calculate_ra_dec(t)


tle_3 = json.loads(
    """{
              "APOGEE": "703.499",
              "ARG_OF_PERICENTER": "99.6931",
              "BSTAR": "3.1643e-05",
              "CLASSIFICATION_TYPE": "U",
              "COMMENT": "GENERATED VIA SPACETRACK.ORG API",
              "ECCENTRICITY": "0.0001434",
              "ELEMENT_SET_NO": "999",
              "EPHEMERIS_TYPE": "0",
              "EPOCH": "2016-04-22 19:57:49",
              "EPOCH_MICROSECONDS": "891680",
              "FILE": "2024416",
              "INCLINATION": "98.1894",
              "INTLDES": "13008A",
              "MEAN_ANOMALY": "260.443",
              "MEAN_MOTION": "14.57121887",
              "MEAN_MOTION_DDOT": "0",
              "MEAN_MOTION_DOT": "9.8e-07",
              "NORAD_CAT_ID": "39084",
              "OBJECT_ID": "2013-008A",
              "OBJECT_NAME": "LANDSAT 8",
              "OBJECT_NUMBER": "39084",
              "OBJECT_TYPE": "PAYLOAD",
              "ORDINAL": "1",
              "ORIGINATOR": "JSPOC",
              "PERIGEE": "701.469",
              "PERIOD": "98.824",
              "RA_OF_ASC_NODE": "184.265",
              "REV_AT_EPOCH": "16984",
              "SEMIMAJOR_AXIS": "7080.619",
              "TLE_LINE0": "0 LANDSAT 8",
              "TLE_LINE1": "1 39084U 13008A   16113.83182745  .00000098  00000-0  31643-4 0  9994",
              "TLE_LINE2": "2 39084  98.1894 184.2650 0001434  99.6931 260.4430 14.57121887169841"
            }"""
)


cal = TLECalculator(tle_3)
#cal.calculate_ra_dec(time.time()-32400)
cal.calculate_ra_dec(time.time())

