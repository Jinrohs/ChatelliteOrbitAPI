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
|time|Greenwich Mean Time.|
|ids|Comma separated NORAD satellite catalog IDs. If not given, information about all satellites in `satelite_nums` list will return.|

sample:

```

```

response:

```
{
  ResultSet:
}
```

- for NodeJS server

|parameter|description|
|:--|:--|
|start|Greenwich Mean Time (start).|
|end|Greenwich Mean Time (end).|
|ids|Comma separated NORAD satellite catalog IDs. If not given, information about all satellites in `satelite_nums` list will return.|

sample:

```

```

response:

```
{
  ResultSet:
}
```
