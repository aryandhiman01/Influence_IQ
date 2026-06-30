from src.utils.abusive_keywords import ABUSIVE_KEYWORDS


def detect_abusive(comment: str) -> bool:
    """
    Detect abusive language using keyword matching.
    """

    if not comment:
        return False

    comment = comment.lower()

    for keyword in ABUSIVE_KEYWORDS:

        if keyword in comment:

            return True

    return False