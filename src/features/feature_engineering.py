import re


def extract_features(comment: str):

    if not comment:

        return {

            "word_count": 0,
            "character_count": 0,
            "comment_length": "Short",
            "contains_link": False,
            "contains_question": False,
            "contains_exclamation": False

        }

    words = comment.split()

    word_count = len(words)

    character_count = len(comment)

    if word_count < 5:

        length = "Short"

    elif word_count < 20:

        length = "Medium"

    else:

        length = "Long"

    return {

        "word_count": word_count,

        "character_count": character_count,

        "comment_length": length,

        "contains_link": bool(
            re.search(r"http|www", comment)
        ),

        "contains_question": "?" in comment,

        "contains_exclamation": "!" in comment

    }