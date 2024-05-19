import unittest
from package import Package
from state import Transit, Delivered
from strategy import Standard, Express


class MyTestCase(unittest.TestCase):
    def test_package_singleton(self):
        pkg1 = Package(32)
        pkg2 = Package(45)
        pkg3 = Package(12, Express(), Delivered())
        self.assertEqual(pkg1, pkg2)
        self.assertEqual(pkg1, pkg3)
        self.assertEqual(pkg2, pkg3)

    def test_standard_shipping_cost(self):
        pkg = Package(100)
        self.assertEqual(pkg.get_cost(), 250)

    def test_express_shipping_cost(self):
        pkg = Package(100)
        pkg.update_strategy(Express())
        self.assertEqual(pkg.get_cost(), 350)

    def test_strategy_update(self):
        pkg = Package(0)
        pkg.update_strategy(Express())
        pkg.update_strategy(Standard())
        self.assertTrue(isinstance(pkg.strategy, Standard))
        self.assertFalse(isinstance(pkg.strategy, Express))

    def test_state_update(self):
        pkg = Package(0)
        pkg.update_state(Transit())
        pkg.update_state(Delivered())
        self.assertTrue(isinstance(pkg.state, Delivered))
        self.assertFalse(isinstance(pkg.state, Transit))


if __name__ == '__main__':
    unittest.main()
