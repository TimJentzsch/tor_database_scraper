from datetime import datetime
from typing import TypedDict, Optional, List


class Volunteer(TypedDict):
    id: int
    username: str
    gamma: int
    date_joined: Optional[str]
    is_bot: bool


class Submission(TypedDict):
    id: int
    create_time: datetime
    claimed_by: Optional[int]
    claim_time: Optional[str]
    completed_by: Optional[int]
    complete_time: Optional[str]
    title: Optional[str]
    nsfw: Optional[bool]
    url: Optional[str]
    tor_url: Optional[str]
    content_url: Optional[str]
    transcription_set: List[int]
    removed_from_queue: bool


class Transcription(TypedDict):
    id: int
    submission: int
    author: int
    create_time: str
    url: Optional[str]
    text: str
    removed_from_reddit: bool