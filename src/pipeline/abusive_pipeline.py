from sqlalchemy.orm import Session

from src.database.connection import SessionLocal
from src.database.models import Comment

from src.abusive.abusive_detector import detect_abusive


BATCH_SIZE = 100


def run_abusive_pipeline():

    db: Session = SessionLocal()

    try:

        total_comments = db.query(Comment).count()

        print("\n========== ABUSIVE LANGUAGE DETECTION ==========\n")

        print(f"Total Comments : {total_comments}\n")

        processed = 0
        abusive_count = 0
        batch = 1
        offset = 0

        while True:

            comments = (

                db.query(Comment)

                .order_by(Comment.comment_id)

                .offset(offset)

                .limit(BATCH_SIZE)

                .all()

            )

            if not comments:
                break

            updates = []

            for comment in comments:

                abusive = detect_abusive(
                    comment.clean_comment
                )

                if abusive:
                    abusive_count += 1

                updates.append(

                    {

                        "comment_id": comment.comment_id,

                        "contains_abusive_language": abusive,

                        "is_abusive_checked": True

                    }

                )

            db.bulk_update_mappings(
                Comment,
                updates
            )

            db.commit()

            db.close()
            db = SessionLocal()

            processed += len(comments)

            print(
                f"✅ Batch {batch} Completed "
                f"({processed}/{total_comments})"
            )

            offset += BATCH_SIZE

            batch += 1

        print("\n========== ABUSIVE SUMMARY ==========\n")

        print(f"Total Comments : {total_comments}")

        print(f"Abusive        : {abusive_count}")

        print(f"Clean          : {total_comments - abusive_count}")

        print("\n🎉 Abusive Language Detection Completed!")

    except Exception as e:

        db.rollback()

        print(e)

    finally:

        db.close()