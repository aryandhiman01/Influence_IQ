from sqlalchemy.orm import Session

from src.database.connection import SessionLocal
from src.database.models import Comment

from src.features.feature_engineering import extract_features


BATCH_SIZE = 100


def run_feature_pipeline():

    db: Session = SessionLocal()

    try:

        total = db.query(Comment).count()

        print("\n========== FEATURE ENGINEERING ==========\n")

        print(f"Total Comments : {total}\n")

        offset = 0
        batch = 1
        processed = 0

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

                feature = extract_features(

                    comment.comment

                )

                feature["comment_id"] = comment.comment_id

                feature["is_feature_engineered"] = True

                updates.append(feature)

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

                f"({processed}/{total})"

            )

            offset += BATCH_SIZE

            batch += 1

        print("\n🎉 Feature Engineering Completed!")

    except Exception as e:

        db.rollback()

        print(e)

    finally:

        db.close()