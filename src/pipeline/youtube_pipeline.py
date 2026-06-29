from src.api.channel_service import (
    search_channel,
    get_channel_details
)

from src.api.video_service import (
    get_upload_playlist_id,
    get_channel_videos
)

from src.api.comment_service import (
    get_video_comments
)

from src.pipeline.etl_pipeline import run_validation

from src.database.connection import SessionLocal

from src.repositories.channel_repository import save_channel
from src.repositories.video_repository import save_videos
from src.repositories.comment_repository import save_comments


def run_pipeline():

    db = SessionLocal()

    try:

        # ----------------------------------------
        # Channel Input
        # ----------------------------------------

        channel_name = input("Enter Channel Name: ").strip()

        channel_id = search_channel(channel_name)

        if not channel_id:
            print("❌ Channel Not Found")
            return

        # ----------------------------------------
        # Channel Details
        # ----------------------------------------

        details = get_channel_details(channel_id)

        print("\n========== CHANNEL DETAILS ==========\n")

        for key, value in details.items():
            print(f"{key:<20}: {value}")

        save_channel(db, details)

        print("✅ Channel Ready")

        # ----------------------------------------
        # Upload Playlist
        # ----------------------------------------

        playlist_id = get_upload_playlist_id(channel_id)

        if not playlist_id:
            print("❌ Upload Playlist Not Found")
            return

        print(f"\nUploads Playlist ID : {playlist_id}")

        # ----------------------------------------
        # Videos
        # ----------------------------------------

        videos = get_channel_videos(
            playlist_id,
            max_videos=50
        )

        if not videos:
            print("❌ No Videos Found")
            return

        print("\n========== VIDEOS ==========\n")

        print(f"Total Videos : {len(videos)}\n")

        for index, video in enumerate(videos, start=1):
            print(f"{index}. {video['title']}")

        save_videos(
            db,
            details["channel_id"],
            videos
        )

        # ----------------------------------------
        # Comments
        # ----------------------------------------

        print("\n========== FETCHING COMMENTS ==========\n")

        all_comments = []

        for index, video in enumerate(videos, start=1):

            print(f"[{index}/{len(videos)}] Fetching Comments")

            print(f"Title    : {video['title']}")
            print(f"Video ID : {video['video_id']}")

            comments = get_video_comments(
                video["video_id"],
                max_comments=100
            )

            print(f"Comments Fetched : {len(comments)}")

            print("-" * 70)

            all_comments.extend(comments)

        print(f"\n✅ Total Comments Collected : {len(all_comments)}")

        save_comments(
            db,
            all_comments
        )

        # ----------------------------------------
        # Commit Once
        # ----------------------------------------

        db.commit()

        print("✅ Database Commit Successful")

        # ----------------------------------------
        # Validation
        # ----------------------------------------

        run_validation(
            details,
            videos,
            all_comments
        )

        # ----------------------------------------
        # Summary
        # ----------------------------------------

        print("\n========== PIPELINE SUMMARY ==========\n")

        print(f"Channel Name      : {details['channel_name']}")
        print(f"Videos Stored     : {len(videos)}")
        print(f"Comments Stored   : {len(all_comments)}")

        print("\n🎉 Data Successfully Stored in Neon!")

    except Exception as e:

        db.rollback()

        print(f"\n❌ Pipeline Error : {e}")

    finally:

        db.close()