from typing import TypedDict, Optional, List


class Volunteer(TypedDict):
    id: int
    username: str
    gamma: int
    date_joined: Optional[str]
    is_bot: bool


class Submission(TypedDict):
    id: int
    create_time: Optional[str]
    claimed_by: Optional[int]
    claim_time: Optional[str]
    completed_by: Optional[int]
    complete_time: Optional[str]
    title: Optional[str]
    nsfw: Optional[bool]
    url: Optional[str]
    tor_url: Optional[str]
    content_url: Optional[str]
    subreddit: Optional[str]
    transcription_set: List[int]
    removed_from_queue: bool
    is_dummy: bool


class Transcription(TypedDict):
    id: int
    create_time: Optional[str]
    url: Optional[str]
    submission: int
    author: int
    removed_from_reddit: bool
    post_type: str
    text: Optional[str]
    is_dummy: bool
