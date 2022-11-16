"""
You just landed a job at "SocialOverlord", a company developing a SaaS product allowing you to write and schedule posts to a variety of social networks.

The whole backend is written in Python (yay!), but unfortunately, the person you're replacing didn't know classes exist (ehrm...) and so they used tuples to represent all the data in the system (not so yay...). Here's a code example:
"""
from time import time

# each social channel has a type
# and the current number of followers
SocialChannel = tuple[str, int]

# each post has a message and the timestamp when it should be posted
Post = tuple[str, int]


def post_to_youtube(channel: SocialChannel, message: str) -> None:
    type, followers = channel
    print(f"{type} channel: {message}")


def post_to_facebook(channel: SocialChannel, message: str) -> None:
    type, followers = channel
    print(f"{type} channel: {message}")


def post_to_twitter(channel: SocialChannel, message: str) -> None:
    type, followers = channel
    print(f"{type} channel: {message}")


def post_a_message(channel: SocialChannel, message: str) -> None:
    type, followers = channel
    if type == "youtube":
        post_to_youtube(channel, message)
    elif type == "facebook":
        post_to_facebook(channel, message)
    elif type == "twitter":
        post_to_twitter(channel, message)


def process_schedule(posts: list[Post], channels: list[SocialChannel]) -> None:
    for post in posts:
        message, timestamp = post
        for channel in channels:
            if timestamp <= time():
                post_a_message(channel, message)


def main() -> None:
    posts = [
        (
            "Grandma's carrot cake is available again (limited quantities!)!",
            1568123400,
        ),
        ("Get your carrot cake now, the promotion ends today!", 1568133400),
    ]
    channels = [
        ("youtube", 100),
        ("facebook", 100),
        ("twitter", 100),
    ]
    process_schedule(posts, channels)


if __name__ == "__main__":
    main()


"""
a) From tuples to classes

Refactor this code so that it uses classes instead of tuples to represent social channels and posts. As a starting point, use the code download for this exercise.
b) Improving the post_a_message function

The post_a_message function isn't great. The if-statement has to check for each different type of social network and then call a different method. If you want to add support for a new social network, you'll need to add an extra elif part, making the code harder and harder to read.

Implement a new version of the code that uses abstraction to solve the problem.

Bonus challenge: is there a solution that doesn't need abstraction?
"""