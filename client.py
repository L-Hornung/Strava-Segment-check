import requests
import time
import logging

BASE_URL = "https://www.strava.com/api/v3"

logger = logging.getLogger(__name__)

class StravaClient:
    """
    Client for interacting with the Strava API v3.
    Handles authentication and rate limit management.
    """
    def __init__(self, access_token: str):
        self.headers = {
            "Authorization": f"Bearer {access_token}"
        }

    def _get(self, url: str, params: dict = None, return_headers: bool = False):
        """
        Internal GET request handler with rate limit management.
        Automatically waits if Strava returns HTTP 429 (Too Many Requests).
        """
        while True:
            try:
                resp = requests.get(url, headers=self.headers, params=params)
                # Rate limit headers
                limit_header = resp.headers.get("X-RateLimit-Limit", "0,0")
                usage_header = resp.headers.get("X-RateLimit-Usage", "0,0")
                reset_time = int(resp.headers.get("X-RateLimit-Reset", 60))
                limit_short, limit_long = [int(x) for x in limit_header.split(",")]
                usage_short, usage_long = [int(x) for x in usage_header.split(",")]
                if resp.status_code == 429:
                    logger.warning(f"HTTP 429: Rate limit exceeded! {usage_short}/{limit_short} (15min), {usage_long}/{limit_long} (day). Waiting {reset_time} seconds...")
                    time.sleep(reset_time)
                    continue
                resp.raise_for_status()
                if return_headers:
                    return resp.json(), resp.headers
                return resp.json()
            except requests.exceptions.RequestException as e:
                logger.error(f"Request failed: {e}")
                return {}

    def get_segment(self, segment_id: int):
        """
        Retrieve details for a specific segment.
        """
        url = f"{BASE_URL}/segments/{segment_id}"
        return self._get(url)
