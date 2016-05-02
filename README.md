# satellite-orbit

## about this component

This component is an API which provides clients with information of satellites' orbits: cartesian coordinates(x, y, z), ratitude, longitude, and altitude.
We get Two Line Element (TLE) from [Space-Track](https://www.space-track.org/auth/login) to calculate real time orbits of satellites.

## setup server

Space-Track account is needed.

```
$ python tle_server.py <Space-Track_username> <Space-Track_password>
```

## APIs

- for NLP server

|parameter|description|
|:--|:--|
|time|Unix Time [sec].|
|ids|Comma separated NORAD satellite catalog IDs. If not given, information about all satellites in `satelite_nums` list will return.|

sample:

```
$ curl "http://localhost:5000/lat_lng_alt?time=12345&ids=33492,29479"
```

response:

```
{
  "ResultSet": {
    "29479": {
      "altitude": 682.2460894496262, 
      "latitude": -67.94018615133484, 
      "longitude": 167.11730592671972, 
      "time": 12345
    }, 
    "33492": {
      "altitude": 648.3852645763782, 
      "latitude": 35.11919259933271, 
      "longitude": -90.26321704426184, 
      "time": 12345
    }
  }
}
```





- for NodeJS server

|parameter|description|
|:--|:--|
|start|Unix Time [sec] (start).|
|end|Unix Time [sec] (end).|
|ids|Comma separated NORAD satellite catalog IDs. If not given, information about all satellites in `satelite_nums` list will return.|

sample:

```
$ curl "http://localhost:5000/xyz?start=10000&end=11000&ids=29479"
```

response:

```
{
  "ResultSet": {
    "29479": [
      [
        0, 
        5670304.7111105882, 
        -1918001.813063388, 
        3741367.3925690977
      ], 
      [
        300, 
        6299467.423111964, 
        -2677256.4376479867, 
        1710999.8427912241
      ], 
      [
        600, 
        6274377.238417713, 
        -3183208.9513072441, 
        -489333.24048025132
      ], 
      [
        900, 
        5610305.3535219645, 
        -3357364.5889085378, 
        -2640077.3814529576
      ]
    ]
  }
}
```
