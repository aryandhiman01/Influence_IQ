from sqlalchemy.orm import Session

from src.database.connection import SessionLocal
from src.database.models import Comment
from src.cleaning.text_cleaner import clean_text


BATCH_SIZE = 500


def run_cleaning_pipeline():

    db: Session = SessionLocal()

    try:

        total_comments = db.query(Comment).filter(
            Comment.is_cleaned == False
        ).count()

        print("\n========== TEXT CLEANING ==========\n")
        print(f"Total Comments Found : {total_comments}\n")

        cleaned = 0
        batch = 1

        while True:

            rows = (
                db.query(
                    Comment.comment_id,
                    Comment.comment
                )
                .filter(Comment.is_cleaned == False)
                .limit(BATCH_SIZE)
                .all()
            )

            if not rows:
                break

            updates = []

            for row in rows:

                updates.append({

                    "comment_id": row.comment_id,

                    "clean_comment": clean_text(row.comment),

                    "is_cleaned": True

                })

            db.bulk_update_mappings(
                Comment,
                updates
            )

            db.commit()

            cleaned += len(updates)

            print(
                f"✅ Batch {batch} Completed "
                f"({cleaned}/{total_comments})"
            )

            batch += 1

        print("\n========== CLEANING SUMMARY ==========\n")

        print(f"Total Cleaned : {cleaned}")

        print("🎉 Cleaning Completed Successfully!")

    except Exception as e:

        db.rollback()

        print(f"\n❌ Cleaning Error : {e}")

    finally:

        db.close()