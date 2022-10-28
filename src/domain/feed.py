from dataclasses import dataclass
from datetime import datetime

from src.domain.user import UserEntity


@dataclass
class FeedEntity:
    title: str = None
    link: str = None
    description: str = None
    updated: str = None


@dataclass
class FeedItemEntity:
    title: str = None
    link: str = None
    description: str = None
    published: str = None
    id: str = None


@dataclass
class FeedFollowingEntity:
    user: UserEntity = None
    feed: FeedEntity = None


@dataclass
class FeedItemRead:
    user: UserEntity = None
    feed_item: FeedItemEntity = None
    read_date: datetime = None


@dataclass
class FeedItemFavorite:
    user: UserEntity = None
    feed_item: FeedItemEntity = None


@dataclass
class FeedItemBookmark:
    user: UserEntity = None
    feed_item: FeedItemEntity = None
