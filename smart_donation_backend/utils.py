import math

def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of Earth in kilometers

    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad

    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c
    return distance

def find_nearest_ngos(donation_latitude, donation_longitude, max_distance_km=50):
    from ngo.models import NGOProfile # Import here to avoid circular dependency
    eligible_ngos = []
    for ngo in NGOProfile.objects.filter(is_verified=True):
        if ngo.latitude and ngo.longitude:
            distance = haversine_distance(donation_latitude, donation_longitude, ngo.latitude, ngo.longitude)
            if distance <= max_distance_km:
                eligible_ngos.append({'ngo': ngo, 'distance': distance})
    # Sort by distance
    eligible_ngos.sort(key=lambda x: x['distance'])
    return eligible_ngos
