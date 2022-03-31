from datetime import datetime
from typing import Optional
import pytz

from tor_database_scraper.types import Volunteer, Submission


def _parse_datetime(time: Optional[datetime]) -> Optional[str]:
    return time.astimezone(pytz.utc).isoformat() if time else None


def parse_volunteer(
    v_id: int, username: str, gamma: Optional[int], date_joined: datetime, is_bot: bool
) -> Volunteer:
    return {
        "id": v_id,
        "username": username,
        "gamma": gamma if gamma is not None else 0,
        "date_joined": _parse_datetime(date_joined),
        "is_bot": is_bot,
    }


def parse_submission(
    s_id,
    create_time,
    url,
    tor_url,
    content_url,
    title,
    nsfw,
    removed_from_queue,
    claimed_by,
    claim_time,
    completed_by,
    complete_time,
) -> Submission:
    return {
        "id": s_id,
        "create_time": _parse_datetime(create_time),
        "url": url,
        "tor_url": tor_url,
        "content_url": content_url,
        "title": title,
        "nsfw": nsfw,
        "removed_from_queue": removed_from_queue,
        "claimed_by": claimed_by,
        "claim_time": _parse_datetime(claim_time),
        "completed_by": completed_by,
        "complete_time": _parse_datetime(complete_time),
    }
