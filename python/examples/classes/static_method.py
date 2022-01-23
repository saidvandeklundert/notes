"""
A static method that uses the class namespace, but does not take self or cls.

Static methods cannot access self or cls either.

Can think of it as an associated function.

Could be used to group functions together, or make it explicit that a func does not operate on an instance or the class.
"""


class RelatedFunc:
    @staticmethod
    def narrator_says_hi():
        print("narrator says hi!")

    @staticmethod
    def narrator_says_by():
        print("narrator says by!")


RelatedFunc.narrator_says_hi()
RelatedFunc.narrator_says_by()