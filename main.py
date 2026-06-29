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

from src.utils.file_handler import save_json


channel_name = input("Enter Channel Name : ")

channel_id = search_channel(channel_name)

if not channel_id:
    print("❌ Channel Not Found")
    exit()

# -----------------------------
# Channel Details
# -----------------------------

details = get_channel_details(channel_id)

save_json(
    details,
    "data/raw/channels",
    f"{channel_name.lower().replace(' ','_')}.json"
)

print("\n========== CHANNEL DETAILS ==========\n")

for key, value in details.items():
    print(f"{key:<20}: {value}")

# -----------------------------
# Playlist
# -----------------------------

playlist_id = get_upload_playlist_id(channel_id)

print("\nUploads Playlist ID :")
print(playlist_id)

# -----------------------------
# Videos
# -----------------------------

videos = get_channel_videos(playlist_id)

save_json(
    videos,
    "data/raw/videos",
    f"{channel_name.lower().replace(' ','_')}_videos.json"
)

print("\n========== LATEST VIDEOS ==========\n")

for index, video in enumerate(videos, start=1):
    print(f"{index}. {video['title']}")

# -----------------------------
# Comments
# -----------------------------

if videos:

    first_video = videos[0]

    print("\n========== FIRST VIDEO ==========\n")

    print(f"Video Title : {first_video['title']}")
    print(f"Video ID    : {first_video['video_id']}")

    comments = get_video_comments(first_video["video_id"])

    save_json(
        comments,
        "data/raw/comments",
        f"{channel_name.lower().replace(' ','_')}_comments.json"
    )

    print("\n========== COMMENTS ==========\n")
    print(f"Total Comments Fetched : {len(comments)}\n")

    for index, comment in enumerate(comments, start=1):

        print(f"{index}. {comment['author']}")
        print(comment["comment"])
        print("-" * 60)