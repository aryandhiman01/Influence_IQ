from src.database.loader import create_tables

from src.pipeline.youtube_pipeline import run_pipeline
from src.pipeline.cleaning_pipeline import run_cleaning_pipeline
from src.pipeline.spam_pipeline import run_spam_pipeline
from src.pipeline.sentiment_pipeline import run_sentiment_pipeline
from src.pipeline.abusive_pipeline import run_abusive_pipeline


def main():

    create_tables()

    while True:

        print("\n" + "=" * 50)
        print("              INFLUENCE IQ")
        print("=" * 50)

        print("1. Fetch YouTube Data")
        print("2. Clean Comments")
        print("3. Detect Spam")
        print("4. Sentiment Analysis")
        print("5. Detect Abusive Language")
        print("6. Run Complete Pipeline")
        print("7. Exit")

        choice = input("\nEnter Choice : ").strip()

        if choice == "1":

            run_pipeline()

        elif choice == "2":

            run_cleaning_pipeline()

        elif choice == "3":

            run_spam_pipeline()

        elif choice == "4":

            run_sentiment_pipeline()

        elif choice == "5":

            run_abusive_pipeline()

        elif choice == "6":

            run_pipeline()

            run_cleaning_pipeline()

            run_spam_pipeline()

            run_sentiment_pipeline()

            run_abusive_pipeline()

        elif choice == "7":

            print("\n👋 Exiting InfluenceIQ...")

            break

        else:

            print("\n❌ Invalid Choice. Please Try Again.")


if __name__ == "__main__":

    main()