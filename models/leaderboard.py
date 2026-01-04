from dataclasses import dataclass

@dataclass
class LeaderboardEntry:
    athlete_name: str
    athlete_id: int
    activity_id: int
    elapsed_time: int
    moving_time: int
    average_speed: float
