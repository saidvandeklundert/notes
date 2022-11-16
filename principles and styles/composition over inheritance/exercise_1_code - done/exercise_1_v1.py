"""
You just landed a job at "SocialOverlord", a company developing a SaaS product allowing you to write and schedule posts to a variety of social networks.

The whole backend is written in Python (yay!), but unfortunately, the person you're replacing didn't know classes exist (ehrm...) and so they used tuples to represent all the data in the system (not so yay...). Here's a code example:
"""
from time import time

from dataclasses import dataclass

# each social channel has a type
# and the current number of followers

# SocialChannel = tuple[str, int]


@dataclass
class SocialChannel:
    type: str
    followers: int


# each post has a message and the timestamp when it should be posted
# Post = tuple[str, int]


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


f_dict = {
    "youtube": post_to_youtube,
    "facebook": post_to_facebook,
    "twitter": post_to_twitter,
}


def post_a_message(channel: SocialChannel, message: str) -> None:

    f_dict[channel.type](channel, message)


def process_schedule(posts: list[Post], channels: list[SocialChannel]) -> None:
    for post in posts:

        for channel in channels:
            if post.timestamp <= time():
                f_dict[channel.type](channel, post.message)


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


"""
a) From tuples to classes

Refactor this code so that it uses classes instead of tuples to represent social channels and posts. 
As a starting point, use the code download for this exercise.
b) Improving the post_a_message function

The post_a_message function isn't great. The if-statement has to check for each different type of social network 
and then call a different method. If you want to add support for a new social network, you'll need to add an extra elif part, 
making the code harder and harder to read.

Implement a new version of the code that uses abstraction to solve the problem.

Bonus challenge: is there a solution that doesn't need abstraction?
"""
