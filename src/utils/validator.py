def validate_channel(channel: dict):

    required_keys = [

        "channel_id",

        "channel_name",

        "subscriber_count",

        "video_count"

    ]

    missing = []

    for key in required_keys:

        if key not in channel:

            missing.append(key)

    return missing


def validate_videos(videos: list):

    duplicate_ids = set()

    seen = set()

    for video in videos:

        video_id = video["video_id"]

        if video_id in seen:

            duplicate_ids.add(video_id)

        seen.add(video_id)

    return list(duplicate_ids)


def validate_comments(comments: list):

    empty_comments = 0

    for comment in comments:

        if comment["comment"].strip() == "":

            empty_comments += 1

    return empty_comments