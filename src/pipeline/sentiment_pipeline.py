from sqlalchemy.orm import Session

from src.database.connection import SessionLocal
from src.database.models import Comment

from src.sentiment.sentiment_analyzer import detect_sentiment


BATCH_SIZE = 100


def run_sentiment_pipeline():

    db: Session = SessionLocal()

    try:

        total_comments = db.query(Comment).count()

        print("\n========== SENTIMENT ANALYSIS ==========\n")

        print(f"Total Comments : {total_comments}\n")

        processed = 0

        positive = 0
        neutral = 0
        negative = 0

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

                sentiment = detect_sentiment(
                    comment.clean_comment
                )

                if sentiment == "Positive":
                    positive += 1

                elif sentiment == "Negative":
                    negative += 1

                else:
                    neutral += 1

                updates.append(

                    {

                        "comment_id": comment.comment_id,

                        "sentiment": sentiment,

                        "is_sentiment_checked": True

                    }

                )

            db.bulk_update_mappings(
                Comment,
                updates
            )

            db.commit()

            # Fresh connection after every batch
            db.close()
            db = SessionLocal()

            processed += len(comments)

            print(

                f"✅ Batch {batch} Completed "

                f"({processed}/{total_comments})"

            )

            offset += BATCH_SIZE

            batch += 1

        print("\n========== SENTIMENT SUMMARY ==========\n")

        print(f"Positive : {positive}")

        print(f"Neutral  : {neutral}")

        print(f"Negative : {negative}")

        print("\n🎉 Sentiment Analysis Completed!")

    except Exception as e:

        db.rollback()

        print(e)

    finally:

        db.close()