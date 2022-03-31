from datetime import datetime
from typing import Optional
import pytz

from tor_database_scraper.types import Volunteer, Submission, Transcription


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
    s_id: int,
    create_time: datetime,
    url: Optional[str],
    tor_url: Optional[str],
    content_url: Optional[str],
    title: Optional[str],
    nsfw: Optional[bool],
    removed_from_queue: bool,
    claimed_by: Optional[int],
    claim_time: Optional[datetime],
    completed_by: Optional[int],
    complete_time: Optional[datetime],
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


def parse_transcription(
    t_id: int,
    create_time: Optional[datetime],
    url: Optional[str],
    submission: int,
    author: int,
    removed_from_reddit: bool,
    text: str,
) -> Transcription:
    return {
        "id": t_id,
        "create_time": _parse_datetime(create_time),
        "url": url,
        "submission": submission,
        "author": author,
        "removed_from_reddit": removed_from_reddit,
        "text": text,
    }
