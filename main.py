from src.database.loader import create_tables
from src.pipeline.youtube_pipeline import run_pipeline


def main():

    create_tables()

    run_pipeline()


if __name__ == "__main__":

    main()