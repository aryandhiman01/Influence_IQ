from src.utils.spam_keywords import SPAM_KEYWORDS


def detect_spam(comment: str) -> bool:
    """
    Detect whether a YouTube comment is spam.

    Returns:
        True  -> Spam
        False -> Normal Comment
    """

    if comment is None:
        return False

    comment = comment.strip().lower()

    if comment == "":
        return False

    return any(
        keyword.lower() in comment
        for keyword in SPAM_KEYWORDS
    )