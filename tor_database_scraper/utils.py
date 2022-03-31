import re
from typing import Tuple, Optional

HEADER_REGEX = re.compile(
    r"^\s*\*(?P<format>\w+)\s*Transcription:?(?:\s*(?P<type>[^\n*]+))?\*", re.IGNORECASE
)

# If one of the words on the right is included in the post type,
# take the word on the left as post type.
POST_TYPE_SIMPLIFICATION_MAP = {
    "Twitter": ["Twitter"],
    "Facebook": ["Facebook"],
    "Tumblr": ["Tumblr"],
    "Reddit": ["Reddit"],
    "Photograph": ["Picture", "Photo"],
    "Review": ["Review"],
    "YouTube": ["YouTube", "You Tube"],
    "Code": ["Code", "Program"],
    "Chat": ["Chat", "Message", "Discord", "Email", "E-Mail"],
    "Meme": ["Meme"],
    "Comic": ["Comic"],
    "Social Media": ["Social Media"],
    "Image": ["Image"],
    "Video": ["Video"],
    "Text": ["Text"],
}


def _get_post_format_and_type(text: Optional[str]) -> Tuple[str, Optional[str]]:
    """Determine the format and type of the transcription."""
    if text is None:
        return "Post", None

    parts = text.split("---")

    if len(parts) < 3:
        # Malformed transcription
        return "Post", None

    header = parts[0]

    match = HEADER_REGEX.search(header)
    if match is None:
        # Malformed header
        return "Post", None

    tr_format = match.group("format")
    if tr_format:
        tr_format = tr_format.strip()
    tr_type = match.group("type")
    if tr_type:
        tr_type = tr_type.strip()

    return tr_format, tr_type


def get_simplified_post_type(text: Optional[str]) -> str:
    """Get a simplified post type, grouping together multiple types."""
    post_format, post_type = _get_post_format_and_type(text)
    post_type = post_type or post_format

    # Simplify the post type into common groups
    for simple_type, words in POST_TYPE_SIMPLIFICATION_MAP.items():
        for word in words:
            if word.casefold() in post_type.casefold():
                return simple_type

    return post_type


def extract_subreddit(url: Optional[str]) -> Optional[str]:
    if url is None or "reddit.com" not in url:
        return None

    parts = url.split("/")

    if len(parts) < 5:
        return None

    return parts[4]
