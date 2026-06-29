from sqlalchemy.orm import Session
from src.database.models import Comment


def save_comments(
    db: Session,
    comments: list
):
    """
    Save comments into database.
    """

    if not comments:
        print("❌ No Comments To Save")
        return

    new_objects = []

    for comment in comments:

        new_objects.append(

            Comment(

                comment_id=comment["comment_id"],

                video_id=comment["video_id"],

                author=comment["author"],

                comment=comment["comment"],

                likes=int(comment["likes"]),

                published_at=comment["published_at"],

                is_cleaned=False,

                sentiment=None,

                is_spam=False,

                contains_abusive_language=False

            )

        )

    db.add_all(new_objects)

    # Flush so comments are staged in current transaction
    db.flush()

    print(f"✅ Comments Saved : {len(new_objects)}")