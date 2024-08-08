from abc import ABC, abstractmethod
from enum import Enum

from app.exception import SizeNotProvidedException

class CoffeeSize(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class CoffeeShop(ABC):
    
    @abstractmethod
    def description(self):
        raise NotImplementedError
    
    @abstractmethod
    def cost(self, size: CoffeeSize):
        raise NotImplementedError


class Latte(CoffeeShop):
    def description(self):
        return "Latte "
    
    def cost(self, size: CoffeeSize):

        costs = {
            CoffeeSize.SMALL: 5,
            CoffeeSize.MEDIUM: 7,
            CoffeeSize.LARGE: 10
        }
        return costs.get(size, 0)

class Americano(CoffeeShop):
    def description(self):
        return "Americano "
    
    def cost(self, size: CoffeeSize):

        costs = {
            CoffeeSize.SMALL: 2,
            CoffeeSize.MEDIUM: 3,
            CoffeeSize.LARGE: 5
        }
        return costs.get(size, 0)

class Capcinao(CoffeeShop):

    def description(self):
        return "Capcinao "
    
    def cost(self, size: CoffeeSize):

       costs = {
            CoffeeSize.SMALL: 1,
            CoffeeSize.MEDIUM: 1.5,
            CoffeeSize.LARGE: 2
        }
       return costs.get(size, 0)


class Mocha(CoffeeShop):
    def __init__(self, coffee):
        self.coffee = coffee
    
    def description(self):
        return self.coffee.description() + ", Mocha"
    
    def cost(self, size: CoffeeSize):

        mocha_costs = {
            CoffeeSize.SMALL: 2,
            CoffeeSize.MEDIUM: 3,
            CoffeeSize.LARGE: 5
        }
        return self.coffee.cost(size) + mocha_costs.get(size, 0)

class Cream(CoffeeShop):
    def __init__(self, coffee):
        self.coffee = coffee
    
    def description(self):
        return self.coffee.description() + ", Cream"
    
    def cost(self, size: CoffeeSize):

        cream_costs = {
            CoffeeSize.SMALL: 1,
            CoffeeSize.MEDIUM: 2,
            CoffeeSize.LARGE: 5
        }
        return self.coffee.cost(size) + cream_costs.get(size, 0)
    
class Soya(CoffeeShop):
    def __init__(self, coffee):
        self.coffee = coffee
    
    def description(self):
        return self.coffee.description() + ", Soya"
    
    def cost(self, size: CoffeeSize):

        soya_costs = {
            CoffeeSize.SMALL: 1,
            CoffeeSize.MEDIUM: 2,
            CoffeeSize.LARGE: 5
        }
        return self.coffee.cost(size) + soya_costs.get(size, 0)