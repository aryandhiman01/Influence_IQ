from sqlalchemy.orm import Session
from src.database.models import Video


def save_videos(
    db: Session,
    channel_id: str,
    videos: list
):
    """
    Save videos into database.
    """

    if not videos:
        print("❌ No Videos To Save")
        return

    new_objects = []

    for video in videos:

        new_objects.append(

            Video(

                video_id=video["video_id"],

                channel_id=channel_id,

                title=video["title"],

                description=video["description"],

                published_at=video["published_at"],

                thumbnail=video["thumbnail"],

                view_count=int(video["view_count"]),

                like_count=int(video["like_count"]),

                comment_count=int(video["comment_count"]),

                duration=video["duration"],

                category_id=video["category_id"],

                default_language=video["default_language"],

                tags=",".join(video["tags"])
                if video["tags"]
                else None

            )

        )

    db.add_all(new_objects)

    # Flush so videos exist in current transaction
    db.flush()

    print(f"✅ Videos Saved : {len(new_objects)}")