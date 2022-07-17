from project.beverage.hotbeverage import HotBeverage


class Coffee(HotBeverage):
    MILLILITERS = 50
    PRICE = 2.50

    def __init__(self, name, coffeine: float):
        super().__init__(name, self.PRICE, self.MILLILITERS)
        self.__coffeine = coffeine

    @property
    def coffeine(self):
        return self.__coffeine
