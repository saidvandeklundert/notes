import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


class DescriptorClass:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        logger.info(
            "Call: %s.__get__(%r, %r)", self.__class__.__name__, instance, owner
        )
        print(type(self), type(instance), type(owner))
        return instance


class ClientClass:
    descriptor = DescriptorClass()


if __name__ == "__main__":
    client = ClientClass()
    client.descriptor
