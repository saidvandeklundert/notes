import os


def operations() -> str:
    if os.getenv("STAGE") == "PROD":
        return "Doing the things prod"
    elif os.getenv("STAGE") == "BETA":
        return "Doing the things beta"
    return "default"
