from datetime import datetime
from typing import Optional
import pytz

from tor_database_scraper.types import Volunteer


def _parse_datetime(time: Optional[datetime]) -> Optional[str]:
    return time.astimezone(pytz.utc).isoformat() if time else None


def parse_volunteer(
    id: int, username: str, gamma: Optional[int], date_joined: datetime, is_bot: bool
) -> Volunteer:
    return {
        "id": id,
        "username": username,
        "gamma": gamma if gamma is not None else 0,
        "date_joined": _parse_datetime(date_joined),
        "is_bot": is_bot,
    }
