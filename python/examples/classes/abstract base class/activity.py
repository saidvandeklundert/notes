from abc import ABC, abstractclassmethod
from typing import List, Union, Callable


# define the standard task to be implemented:
class Step(ABC):
    def __call__(self) -> None:
        self.run_work_items()

    @abstractclassmethod
    def run_work_items(self) -> List[Callable]:
        """Runs tasks."""


# define the standard body of work:
class WorkFlow(ABC):
    """Something that runs one or more tasks"""

    @abstractclassmethod
    def get_steps(self) -> List[Union[List[Step], Step]]:
        """Runs tasks."""


if __name__ == "__main__":
    # implement a SpeakerTask:
    class SpeakerStep(Step):
        def run_work_items(self) -> List[Callable]:
            return [self.say_something()]

        def say_something(self):
            print("something the speaker did!")

    # implement a PreacherTask:
    class PreacherStep(Step):
        def run_work_items(self) -> List[Callable]:
            return [self.say_something()]

        def say_something(self):
            print("something the preacher did!")

    # Implement CustomWork:
    class CustomWork(WorkFlow):
        name = "CustomWork"

        def get_steps(self):
            print(f"executing {self.name}")
            return [SpeakerStep(), PreacherStep()]

    # Execute the class:
    custom_work_instance = CustomWork()
    # generate a work list:
    work_list = custom_work_instance.get_steps()
    # execute the work (dispatched to Lambda's):
    for job in work_list:
        job()
