from sqlalchemy.orm import sessionmaker


def create_engine():
    pass


class UnitOfWork:
    def __init__(self):
        self.session_maker = sessionmaker(bind=create_engine("sqlite://orders.db"))

    def __enter__(self):
        """
        Defines the operations that must be undertaken when entering the context.
        """
        self.session = self.session_maker()
        return self

    def __exit__(self, exc_type, exc_val, traceback):
        """
        Defines the operations that must be undertaken when exiting the context.

        The exit() method captures any exceptions raised during the execution
        of the context through three parameters in it's method signature:
        - exc_type: captures the type of exception raised
        - exc_val: value bound to the exception (usually the error message)
        - traceback: a traceback object that can be used to pinpoint where
          the exception took place.

        """
        if exc_type is not None:
            self.rollback()
            self.session.close()
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()


with UnitOfWork() as uow:
    repo = Repo()
    orders_service = OrdersService(repo)
    orders_service.place_order(order_details)
    uow.commit()
