from abc import ABC, abstractmethod
from dataclasses import dataclass
from time import time


class SocialChannel(ABC):
    @abstractmethod
    def post_message(self, message: str) -> None:
        pass

    @property
    @abstractmethod
    def type(self) -> str:
        pass


@dataclass
class YoutubeChannel(SocialChannel):
    followers: int = 100

    def post_message(self, message: str) -> None:
        post_to_youtube(self, message)

    @property
    def type(self) -> str:
        return "youtube"


@dataclass
class FacebookChannel(SocialChannel):
    followers: int = 100

    def post_message(self, message: str) -> None:
        post_to_facebook(self, message)

    @property
    def type(self) -> str:
        return "facebook"


@dataclass
class TwitterChannel(SocialChannel):
    followers: int = 100

    def post_message(self, message: str) -> None:
        post_to_twitter(self, message)

    @property
    def type(self) -> str:
        return "twitter"


@dataclass
class Post:
    message: str
    timestamp: int


def post_to_youtube(channel: SocialChannel, message: str) -> None:
    print(f"{channel.type} channel: {message}")


def post_to_facebook(channel: SocialChannel, message: str) -> None:
    print(f"{channel.type} channel: {message}")


def post_to_twitter(channel: SocialChannel, message: str) -> None:
    print(f"{channel.type} channel: {message}")


def process_schedule(posts: list[Post], channels: list[SocialChannel]) -> None:
    for post in posts:
        for channel in channels:
            if post.timestamp <= time():
                channel.post_message(post.message)


def main() -> None:
    posts = [
        Post(
            "Grandma's carrot cake is available again (limited quantities!)!",
            1568123400,
        ),
        Post("Get your carrot cake now, the promotion ends today!", 1568133400),
    ]
    channels = [
        YoutubeChannel(100),
        FacebookChannel(100),
        TwitterChannel(100),
    ]
    process_schedule(posts, channels)


if __name__ == "__main__":
    main()
