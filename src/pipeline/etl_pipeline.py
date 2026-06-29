from src.utils.validator import (
    validate_channel,
    validate_videos,
    validate_comments
)

from src.utils.logger import logger


def run_validation(channel, videos, comments):

    print("\n========== DATA VALIDATION ==========\n")

    missing = validate_channel(channel)

    duplicates = validate_videos(videos)

    empty = validate_comments(comments)

    print(f"Missing Channel Fields : {missing}")

    print(f"Duplicate Videos      : {len(duplicates)}")

    print(f"Empty Comments        : {empty}")

    logger.info("Validation Completed")

    logger.info(f"Missing Fields : {missing}")

    logger.info(f"Duplicate Videos : {len(duplicates)}")

    logger.info(f"Empty Comments : {empty}")