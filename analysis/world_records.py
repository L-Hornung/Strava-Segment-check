# World records in seconds
# Source: IAAF / official records (as of 2025)
WORLD_RECORDS = {
    100: 9.58,      # 100 m - Usain Bolt
    200: 19.19,     # 200 m - Usain Bolt
    400: 43.03,     # 400 m - Wayde van Niekerk
    800: 100.91,    # 800 m - David Rudisha
    1000: 131.0,    # 1 km - Noah Ngeny
    1500: 206.0,    # 1500 m - Hicham El Guerrouj
    5000: 755.36,   # 5 km - Joshua Cheptegei
    10000: 1571.0   # 10 km - Joshua Cheptegei
}

def interpolate_world_record(distance_m: float) -> float:
    """
    Returns world record time in seconds for any distance.
    Linear interpolation between known records.
    """
    distances = sorted(WORLD_RECORDS.keys())

    if distance_m <= distances[0]:
        return WORLD_RECORDS[distances[0]]

    for i in range(len(distances) - 1):
        d1, d2 = distances[i], distances[i + 1]
        if d1 <= distance_m <= d2:
            t1, t2 = WORLD_RECORDS[d1], WORLD_RECORDS[d2]
            return t1 + (t2 - t1) * ((distance_m - d1) / (d2 - d1))

    # Extrapolation beyond 10 km (very conservative)
    d1 = distances[-2]
    d2 = distances[-1]
    t1, t2 = WORLD_RECORDS[d1], WORLD_RECORDS[d2]
    return t2 + (distance_m - d2) * (t2 - t1) / (d2 - d1)
