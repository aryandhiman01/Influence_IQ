from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from sqlalchemy import (
    String,
    Text,
    BigInteger,
    Integer,
    Boolean,
    ForeignKey
)


class Base(DeclarativeBase):
    pass


# =====================================================
# CHANNEL TABLE
# =====================================================

class Channel(Base):

    __tablename__ = "channels"

    channel_id: Mapped[str] = mapped_column(String, primary_key=True)

    channel_name: Mapped[str] = mapped_column(String(255), nullable=False)

    description: Mapped[str] = mapped_column(Text)

    country: Mapped[str | None] = mapped_column(String(100), nullable=True)

    published_at: Mapped[str] = mapped_column(String)

    subscriber_count: Mapped[int] = mapped_column(BigInteger)

    total_views: Mapped[int] = mapped_column(BigInteger)

    video_count: Mapped[int] = mapped_column(Integer)


# =====================================================
# VIDEO TABLE
# =====================================================

class Video(Base):

    __tablename__ = "videos"

    video_id: Mapped[str] = mapped_column(String, primary_key=True)

    channel_id: Mapped[str] = mapped_column(
        ForeignKey("channels.channel_id"),
        nullable=False
    )

    title: Mapped[str] = mapped_column(String(500))

    description: Mapped[str] = mapped_column(Text)

    published_at: Mapped[str] = mapped_column(String)

    thumbnail: Mapped[str] = mapped_column(Text)

    # ---------- Statistics ----------

    view_count: Mapped[int] = mapped_column(
        BigInteger,
        default=0
    )

    like_count: Mapped[int] = mapped_column(
        BigInteger,
        default=0
    )

    comment_count: Mapped[int] = mapped_column(
        BigInteger,
        default=0
    )

    # ---------- Metadata ----------

    duration: Mapped[str] = mapped_column(
        String(50)
    )

    category_id: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True
    )

    default_language: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True
    )

    tags: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )


# =====================================================
# COMMENT TABLE
# =====================================================

class Comment(Base):

    __tablename__ = "comments"

    comment_id: Mapped[str] = mapped_column(
        String,
        primary_key=True
    )

    video_id: Mapped[str] = mapped_column(
        ForeignKey("videos.video_id"),
        nullable=False
    )

    author: Mapped[str] = mapped_column(
        String(255)
    )

    comment: Mapped[str] = mapped_column(
        Text
    )

    clean_comment: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    likes: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    published_at: Mapped[str] = mapped_column(
        String
    )

    # -----------------------------
    # NLP Pipeline
    # -----------------------------

    is_cleaned: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    is_spam: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    is_spam_checked: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    sentiment: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True
    )

    is_sentiment_checked: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    contains_abusive_language: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )