# Reuirement:
# 1. Cofee shop should be able to order latte, Americano, Capcinao
# 2. App should caluclate oney for erxtra condiment shuch as Mocha, Soya, Cream
# 3. Design a system which doesn't include so many subclasses and anyway we can decorate them at runtime
# Also should handle small, large and medium size where each size varies


import unittest

from app.exception import SizeNotProvidedException
from app.star_bucks_shop import Americano, Capcinao, Cream, Latte, Mocha, Soya, CoffeeSize

class TestCoffeeShop(unittest.TestCase):
    
    def test_order_latte(self):
        latte = Latte()
        self.assertEqual(latte.description(), "Latte ")
        self.assertEqual(latte.cost(CoffeeSize.LARGE), 10)

    def test_order_americano(self):
        americano = Americano()
        self.assertEqual(americano.description(), "Americano ")
        self.assertEqual(americano.cost(CoffeeSize.LARGE), 5)


    def test_order_capcino(self):
        capcino = Capcinao()
        self.assertEqual(capcino.description(), "Capcinao ")
        self.assertEqual(capcino.cost(CoffeeSize.LARGE), 2)


    def test_order_lattice_with_one_condiment(self):
        latte = Latte()
        latte_wih_mocha = Mocha(latte)
        self.assertEqual(latte_wih_mocha.description(), "Latte , Mocha")
        self.assertEqual(latte_wih_mocha.cost(CoffeeSize.LARGE), 15)


    def test_order_lattice_with_more_condiments(self):
        latte = Latte()
        latte_wih_mocha = Mocha(latte)
        latte_wih_mocha_and_soya = Soya(latte_wih_mocha)
        self.assertEqual(latte_wih_mocha_and_soya.description(), "Latte , Mocha, Soya")
        self.assertEqual(latte_wih_mocha_and_soya.cost(CoffeeSize.LARGE), 20)
        latte_wih_mocha_and_soya_and_cream = Cream(latte_wih_mocha_and_soya)
        self.assertEqual(latte_wih_mocha_and_soya_and_cream.description(), "Latte , Mocha, Soya, Cream")
        self.assertEqual(latte_wih_mocha_and_soya_and_cream.cost(CoffeeSize.LARGE), 25)

    def test_order_with_size(self):
        latte = Latte()
        self.assertEqual(latte.cost(CoffeeSize.SMALL), 5)
        self.assertEqual(latte.cost(CoffeeSize.MEDIUM), 7)
        self.assertEqual(latte.cost(CoffeeSize.LARGE), 10)
        capcinao = Capcinao()
        self.assertEqual(capcinao.cost(CoffeeSize.SMALL), 1)
        self.assertEqual(capcinao.cost(CoffeeSize.MEDIUM), 1.5)
        self.assertEqual(capcinao.cost(CoffeeSize.LARGE), 2)
        americano = Americano()
        self.assertEqual(americano.cost(CoffeeSize.SMALL), 2)
        self.assertEqual(americano.cost(CoffeeSize.MEDIUM), 3)
        self.assertEqual(americano.cost(CoffeeSize.LARGE), 5)

    def test_order_with_size_and_condiments(self):
        latte = Latte()
        latte_wih_mocha = Mocha(latte)
        self.assertEqual(latte_wih_mocha.description(), "Latte , Mocha")
        self.assertEqual(latte_wih_mocha.cost(CoffeeSize.SMALL), 7)
        self.assertEqual(latte_wih_mocha.cost(CoffeeSize.MEDIUM), 10)
        self.assertEqual(latte_wih_mocha.cost(CoffeeSize.LARGE), 15)

    def test_multiple_orders(self):
        latte = Latte()
        latte_wih_mocha = Mocha(latte)
        self.assertEqual(latte_wih_mocha.description(), "Latte , Mocha")
        self.assertEqual(latte_wih_mocha.cost(CoffeeSize.SMALL), 7)
        self.assertEqual(latte_wih_mocha.cost(CoffeeSize.MEDIUM), 10)
        self.assertEqual(latte_wih_mocha.cost(CoffeeSize.LARGE), 15)
        latte_second = Latte()
        latte_wih_soya_second = Soya(latte_second)
        self.assertEqual(latte_wih_soya_second.description(), "Latte , Soya")
        self.assertEqual(latte_wih_soya_second.cost(CoffeeSize.SMALL), 6)
        self.assertEqual(latte_wih_soya_second.cost(CoffeeSize.MEDIUM), 9)
        self.assertEqual(latte_wih_soya_second.cost(CoffeeSize.LARGE), 15)


    