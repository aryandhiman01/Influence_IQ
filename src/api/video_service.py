from src.api.youtube_client import youtube


def get_upload_playlist_id(channel_id: str):
    """
    Fetch the Uploads Playlist ID of a YouTube channel.

    Args:
        channel_id (str): Unique YouTube Channel ID

    Returns:
        str | None
    """

    try:

        request = youtube.channels().list(
            part="contentDetails",
            id=channel_id
        )

        response = request.execute()

        items = response.get("items", [])

        if not items:
            return None

        playlist_id = (
            items[0]
            ["contentDetails"]
            ["relatedPlaylists"]
            ["uploads"]
        )

        return playlist_id

    except Exception as e:

        print(f"Error : {e}")

        return None


def get_channel_videos(playlist_id: str, max_results: int = 50):
    """
    Fetch latest videos from Upload Playlist.

    Args:
        playlist_id (str)
        max_results (int)

    Returns:
        list
    """

    try:

        request = youtube.playlistItems().list(
            part="snippet",
            playlistId=playlist_id,
            maxResults=max_results
        )

        response = request.execute()

        videos = []

        for item in response.get("items", []):

            snippet = item["snippet"]

            videos.append({

                "video_id": snippet["resourceId"]["videoId"],

                "title": snippet["title"],

                "published_at": snippet["publishedAt"],

                "description": snippet["description"],

                "thumbnail": snippet["thumbnails"]["high"]["url"]

            })

        return videos

    except Exception as e:

        print(f"Error : {e}")

        return []