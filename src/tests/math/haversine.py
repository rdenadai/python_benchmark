# @ALLOWED_VERSIONS: 3.6, 3.7, 3.8, 3.9, 3.10, 3.11, 3.12, 3.13

from math import asin, cos, radians, sin, sqrt


def haversine(lat1: float, lng1: float, lat2: float, lng2: float) -> int:
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    dlat = radians(lat2 - lat1)
    dlon = radians(lng2 - lng1)
    # convert to radians
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    # haversine formula
    a = (sin(dlat / 2) ** 2) + (cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2)
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles
    return int(c * r)


def main():
    data = (
        ({"lat1": -34.83333, "lng1": -58.5166646, "lat2": 49.0083899664, "lng2": 2.53844117956}, 11099),
        ({"lat1": 51.5007, "lng1": 0.1246, "lat2": 40.6892, "lng2": 74.0445}, 5574),
        ({"lat1": 43.2341, "lng1": 0.5463, "lat2": 58.1234, "lng2": 88.9421}, 5967),
        ({"lat1": -84.412977, "lng1": 39.152501, "lat2": -84.412946, "lng2": 39.152505}, 0),
        ({"lat1": -0.116773, "lng1": 51.510357, "lat2": -77.009003, "lng2": 38.889931}, 8585),
    )
    for _ in range(100_000):
        for geo, expected in data:
            result = haversine(**geo)
            assert result == expected, f"{result} != {expected}"
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
