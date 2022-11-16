from dataclasses import dataclass
from time import time
from typing import Callable


@dataclass
class SocialChannel:
    type: str
    followers: int


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


MessageSender = Callable[[SocialChannel, str], None]

POSTING_FUNCTIONS: dict[str, MessageSender] = {
    "youtube": post_to_youtube,
    "facebook": post_to_facebook,
    "twitter": post_to_twitter,
}


def process_schedule(posts: list[Post], channels: list[SocialChannel]) -> None:
    for post in posts:
        for channel in channels:
            if post.timestamp <= time():
                POSTING_FUNCTIONS[channel.type](channel, post.message)


def main() -> None:
    posts = [
        Post(
            "Grandma's carrot cake is available again (limited quantities!)!",
            1568123400,
        ),
        Post("Get your carrot cake now, the promotion ends today!", 1568133400),
    ]
    channels = [
        SocialChannel("youtube", 100),
        SocialChannel("facebook", 100),
        SocialChannel("twitter", 100),
    ]
    process_schedule(posts, channels)


if __name__ == "__main__":
    main()
