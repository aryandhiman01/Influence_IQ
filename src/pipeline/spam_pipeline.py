from sqlalchemy.orm import Session

from src.database.connection import SessionLocal
from src.database.models import Comment

from src.cleaning.spam_detector import detect_spam


BATCH_SIZE = 500


def run_spam_pipeline():

    db: Session = SessionLocal()

    try:

        total_comments = db.query(Comment).count()

        print("\n========== SPAM DETECTION ==========\n")
        print(f"Total Comments : {total_comments}\n")

        processed = 0
        spam_count = 0
        batch = 1
        offset = 0

        while True:

            print(f"\nLoading Batch {batch}...")

            comments = (
                db.query(Comment)
                .order_by(Comment.comment_id)
                .offset(offset)
                .limit(BATCH_SIZE)
                .all()
            )

            print(f"Fetched : {len(comments)}")

            if not comments:
                break

            for i, comment in enumerate(comments, start=1):

                if i % 100 == 0:
                    print(f"Processed {i}/{len(comments)}")

                spam = detect_spam(comment.clean_comment)

                comment.is_spam = spam
                comment.is_spam_checked = True

                if spam:
                    spam_count += 1

            print("Committing batch...")

            db.commit()

            print("Commit Done")

            processed += len(comments)

            print(f"✅ Batch {batch} Completed ({processed}/{total_comments})")

            offset += BATCH_SIZE
            batch += 1

        print("\n========== SPAM SUMMARY ==========\n")

        print(f"Total Comments : {total_comments}")
        print(f"Spam Comments  : {spam_count}")
        print(f"Normal Comments: {total_comments - spam_count}")

        print("\n🎉 Spam Detection Completed Successfully!")

    except Exception as e:

        db.rollback()

        print(e)

    finally:

        db.close()