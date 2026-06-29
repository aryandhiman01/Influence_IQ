from src.api.youtube_client import youtube


def get_video_comments(video_id: str, max_results: int = 100):
    """
    Fetch top comments of a YouTube video.

    Args:
        video_id (str): YouTube Video ID
        max_results (int): Number of comments to fetch

    Returns:
        list
    """

    try:

        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=max_results,
            textFormat="plainText"
        )

        response = request.execute()

        comments = []

        for item in response.get("items", []):

            snippet = item["snippet"]["topLevelComment"]["snippet"]

            comments.append({

                "comment_id": item["snippet"]["topLevelComment"]["id"],

                "author": snippet["authorDisplayName"],

                "comment": snippet["textDisplay"],

                "likes": snippet["likeCount"],

                "published_at": snippet["publishedAt"]

            })

        return comments

    except Exception as e:

        print(f"Error : {e}")

        return []