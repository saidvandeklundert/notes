class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        """accessor"""
        return self.name

    def set_name(self, name):
        """mutator"""
        self.name = name


class Student:
    def __init__(self, name: str, startingGrade: int = 0):
        self.__name = name
        self.grade = startingGrade

    @property
    def grade(self):
        """
        getter method that returns the grade"""
        return self.__grade

    @grade.setter
    def grade(self, new_grade):
        """
        setter method that allows you to change grade.
        without this you could not change the grade.
        """
        try:
            new_grade = int(new_grade)
        except (TypeError, ValueError) as e:
            raise type(e)("New grade: " + str(new_grade) + ", is an invalid type.")
        if (new_grade < 0) or (new_grade > 100):
            raise ValueError(
                "New grade: " + str(new_grade) + ", must be between 0 and 100."
            )
        self.__grade = new_grade
