from src.api.youtube_client import youtube


def get_video_comments(
    video_id: str,
    max_comments: int = 100
):
    """
    Fetch top-level comments with pagination.
    """

    comments = []

    next_page_token = None

    try:

        while len(comments) < max_comments:

            request = youtube.commentThreads().list(
                part="snippet",
                videoId=video_id,
                maxResults=min(100, max_comments - len(comments)),
                textFormat="plainText",
                pageToken=next_page_token
            )

            response = request.execute()

            for item in response.get("items", []):

                snippet = item["snippet"]["topLevelComment"]["snippet"]

                comments.append({

                    "comment_id": item["snippet"]["topLevelComment"]["id"],

                    "video_id": video_id,

                    "author": snippet["authorDisplayName"],

                    "comment": snippet["textDisplay"],

                    "likes": snippet["likeCount"],

                    "published_at": snippet["publishedAt"]

                })

            next_page_token = response.get("nextPageToken")

            if not next_page_token:
                break

        return comments

    except Exception as e:

        print(f"Error fetching comments: {e}")

        return []