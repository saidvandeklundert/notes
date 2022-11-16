import os
from dataclasses import dataclass
from typing import Union


@dataclass(frozen=True)
class Environment:
    stage: Union[str, None]


ENVIRONMENT = Environment(stage=os.getenv("STAGE"))


def operations() -> str:
    print(ENVIRONMENT.stage)
    if ENVIRONMENT.stage == "PROD":
        return "Doing the things prod"
    elif ENVIRONMENT.stage == "BETA":
        return "Doing the things beta"
    raise ValueError("Unknown environment")
