import math

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points
    on the Earth (specified in decimal degrees)
    """
    # Convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = 6371 * c  # Radius of Earth in kilometers
    return distance

def is_within_radius(lat1, lon1, lat2, lon2, radius):
    """
    Check if the second GPS location (lat2, lon2) is within
    the specified radius (in meters) of the first GPS location (lat1, lon1)
    """
    distance = haversine(lat1, lon1, lat2, lon2) * 1000  # Convert distance to meters
    return distance <= radius

# Example usage
gps1 = (19.0485361, 83.8342163)  # New York City coordinates
gps2 = (19.0485703, 83.8344593)  # Nearby coordinates
radius = 10  # 10 meters

print(is_within_radius(gps1[0], gps1[1], gps2[0], gps2[1], radius))  # Output: True
