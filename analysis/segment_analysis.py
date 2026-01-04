from analysis.world_records import interpolate_world_record
from .world_records import WORLD_RECORDS, interpolate_world_record

def analyze_effort(distance_m: float, elapsed_time_s: float) -> dict:
    """
    Analyzes a running segment effort:
    - distance_m: distance in meters
    - elapsed_time_s: time in seconds (KOM)
    Returns:
    {
        "elapsed_time_s": int,
        "pace_s_per_km": float,
        "wr_pace_s_per_km": float,
        "ratio": float,
        "flag": str
    }
    """
    # Athlete's pace
    pace_s_per_km = elapsed_time_s / (distance_m / 1000)

    # Interpolate world record
    wr_time_s = interpolate_world_record(distance_m)
    if wr_time_s is None:
        # Extremely short distance: set flag to "impossible"
        flag = "impossible"
        wr_time_s = elapsed_time_s  # Avoid None
    else:
        ratio = elapsed_time_s / wr_time_s
        if ratio < 0.8:  # faster than 90% WR → impossible
            flag = "impossible"
        else:
            flag = "plausible"


    wr_pace_s_per_km = wr_time_s / (distance_m / 1000)

    return {
        "elapsed_time_s": elapsed_time_s,
        "pace_s_per_km": round(pace_s_per_km, 1),
        "wr_pace_s_per_km": round(wr_pace_s_per_km, 1),
        "ratio": round(elapsed_time_s / wr_time_s, 2) if wr_time_s else None,
        "flag": flag
    }
