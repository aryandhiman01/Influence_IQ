from src.api.youtube_client import youtube


def search_channel(channel_name: str):
    """
    Search YouTube channel by name and return Channel ID.
    """

    request = youtube.search().list(
        part="snippet",
        q=channel_name,
        type="channel",
        maxResults=1
    )

    response = request.execute()

    items = response.get("items", [])

    if not items:
        return None

    return items[0]["snippet"]["channelId"]


def get_channel_details(channel_id: str):
    """
    Fetch detailed information about a YouTube channel.
    """

    request = youtube.channels().list(
        part="snippet,statistics",
        id=channel_id
    )

    response = request.execute()

    items = response.get("items", [])

    if not items:
        return None

    channel = items[0]

    return {
        "channel_id": channel["id"],
        "channel_name": channel["snippet"]["title"],
        "description": channel["snippet"]["description"],
        "country": channel["snippet"].get("country"),
        "published_at": channel["snippet"]["publishedAt"],
        "subscriber_count": channel["statistics"].get("subscriberCount"),
        "total_views": channel["statistics"].get("viewCount"),
        "video_count": channel["statistics"].get("videoCount")
    }