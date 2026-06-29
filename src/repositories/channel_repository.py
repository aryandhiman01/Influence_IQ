from sqlalchemy.orm import Session
from src.database.models import Channel


def save_channel(
    db: Session,
    channel_data: dict
):
    """
    Save or Update Channel.
    """

    existing_channel = db.get(
        Channel,
        channel_data["channel_id"]
    )

    if existing_channel:

        existing_channel.channel_name = channel_data["channel_name"]
        existing_channel.description = channel_data["description"]
        existing_channel.country = channel_data["country"]
        existing_channel.published_at = channel_data["published_at"]
        existing_channel.subscriber_count = int(
            channel_data["subscriber_count"]
        )
        existing_channel.total_views = int(
            channel_data["total_views"]
        )
        existing_channel.video_count = int(
            channel_data["video_count"]
        )

        print("🔄 Channel Updated")

    else:

        new_channel = Channel(

            channel_id=channel_data["channel_id"],

            channel_name=channel_data["channel_name"],

            description=channel_data["description"],

            country=channel_data["country"],

            published_at=channel_data["published_at"],

            subscriber_count=int(
                channel_data["subscriber_count"]
            ),

            total_views=int(
                channel_data["total_views"]
            ),

            video_count=int(
                channel_data["video_count"]
            )

        )

        db.add(new_channel)

        print("✅ Channel Added")

    # Flush so Channel is available immediately
    db.flush()

    print("✅ Channel Saved Successfully")