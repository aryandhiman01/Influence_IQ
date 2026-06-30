import re


# ==========================================
# Pre-compiled Regex Patterns
# ==========================================

URL_PATTERN = re.compile(
    r"https?://\S+|www\.\S+"
)

MENTION_PATTERN = re.compile(
    r"@\w+"
)

HASHTAG_PATTERN = re.compile(
    r"#\w+"
)

SPECIAL_CHAR_PATTERN = re.compile(
    r"[^a-z0-9\s]"
)

MULTIPLE_SPACE_PATTERN = re.compile(
    r"\s+"
)


def clean_text(text: str) -> str:
    """
    Clean YouTube comments.

    Steps:
    1. Lowercase
    2. Remove URLs
    3. Remove @mentions
    4. Remove hashtags
    5. Remove emojis
    6. Remove special characters
    7. Remove extra spaces
    """

    if not text:
        return ""

    text = text.lower()

    text = URL_PATTERN.sub("", text)

    text = MENTION_PATTERN.sub("", text)

    text = HASHTAG_PATTERN.sub("", text)

    text = text.encode(
        "ascii",
        "ignore"
    ).decode(
        "ascii"
    )

    text = SPECIAL_CHAR_PATTERN.sub(
        " ",
        text
    )

    text = MULTIPLE_SPACE_PATTERN.sub(
        " ",
        text
    )

    return text.strip()