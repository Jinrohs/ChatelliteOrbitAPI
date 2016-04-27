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

sample:

```

```

response:

```
{
  ResultSet:
}
```
