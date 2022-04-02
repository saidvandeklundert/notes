from abc import ABC, abstractmethod


class Mage(ABC):
    @abstractmethod
    def cast_spell(self) -> str:
        pass


class IceMage(Mage):
    def cast_spell(self) -> str:
        return "blizzard"


class FireMage(Mage):
    def cast_spell(self) -> str:
        return "fireball"


class MageFactory(ABC):
    @abstractmethod
    def get_mage(self) -> Mage:
        pass


class FireMageFactory(MageFactory):
    def get_mage(self) -> FireMage:
        return FireMage()


class IceMageFactory(MageFactory):
    def get_mage(self) -> IceMage:
        return IceMage()


def read_factory(mage_type: str) -> MageFactory:
    mage_factories = {
        "fire": FireMageFactory(),
        "ice": IceMageFactory(),
    }
    return mage_factories[mage_type]


if __name__ == "__main__":
    i = IceMage()
    print(i.cast_spell())
    i = FireMage()
    print(i.cast_spell())

    # now with the factory:
    ice_mage_factory = read_factory("ice")
    ice_mage = ice_mage_factory.get_mage()
    result = ice_mage.cast_spell()
    print(result)

    fire_mage_factory = read_factory("fire")
    fire_mage = fire_mage_factory.get_mage()
    result = fire_mage.cast_spell()
    print(result)
