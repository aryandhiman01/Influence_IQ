from src.api.youtube_client import youtube


def get_upload_playlist_id(channel_id: str):
    """
    Fetch Upload Playlist ID of a YouTube Channel.
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

        return items[0]["contentDetails"]["relatedPlaylists"]["uploads"]

    except Exception as e:

        print(f"Error fetching playlist ID: {e}")
        return None


def get_channel_videos(
    playlist_id: str,
    max_videos: int = 50
):
    """
    Fetch channel videos along with statistics.
    """

    videos = []

    next_page_token = None

    try:

        while len(videos) < max_videos:

            request = youtube.playlistItems().list(
                part="snippet",
                playlistId=playlist_id,
                maxResults=min(50, max_videos - len(videos)),
                pageToken=next_page_token
            )

            response = request.execute()

            video_ids = []

            snippets = {}

            for item in response.get("items", []):

                snippet = item["snippet"]

                video_id = snippet["resourceId"]["videoId"]

                video_ids.append(video_id)

                snippets[video_id] = snippet

            if video_ids:

                stats_request = youtube.videos().list(
                    part="statistics,contentDetails,snippet",
                    id=",".join(video_ids)
                )

                stats_response = stats_request.execute()

                for video in stats_response.get("items", []):

                    video_id = video["id"]

                    snippet = snippets.get(video_id, {})

                    statistics = video.get("statistics", {})

                    content = video.get("contentDetails", {})

                    videos.append({

                        "video_id": video_id,

                        "title": snippet.get("title"),

                        "description": snippet.get("description"),

                        "published_at": snippet.get("publishedAt"),

                        "thumbnail": snippet.get(
                            "thumbnails",
                            {}
                        ).get(
                            "high",
                            {}
                        ).get(
                            "url"
                        ),

                        "view_count": int(
                            statistics.get(
                                "viewCount",
                                0
                            )
                        ),

                        "like_count": int(
                            statistics.get(
                                "likeCount",
                                0
                            )
                        ),

                        "comment_count": int(
                            statistics.get(
                                "commentCount",
                                0
                            )
                        ),

                        "duration": content.get(
                            "duration"
                        ),

                        "category_id": video.get(
                            "snippet",
                            {}
                        ).get(
                            "categoryId"
                        ),

                        "tags": video.get(
                            "snippet",
                            {}
                        ).get(
                            "tags",
                            []
                        ),

                        "default_language": video.get(
                            "snippet",
                            {}
                        ).get(
                            "defaultLanguage"
                        )

                    })

            next_page_token = response.get("nextPageToken")

            if not next_page_token:
                break

        return videos

    except Exception as e:

        print(f"Error fetching videos: {e}")

        return []