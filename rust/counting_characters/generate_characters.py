import random, string


with open("characters.txt", "w") as f:
    for x in range(250000):
        f.write(
            "".join(
                random.choice(
                    string.ascii_uppercase + string.ascii_lowercase + string.digits
                )
                for _ in range(80)
            )
            + "\n"
        )
