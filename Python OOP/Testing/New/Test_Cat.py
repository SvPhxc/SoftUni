import unittest
class Cat:
    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')
        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')
        self.sleepy = False



# Cat's size is increased after eating
#
# · Cat is fed after eating
#
# · Cat cannot eat if already fed, raises an error
#
# · Cat cannot fall asleep if not fed, raises an error
#
# · Cat is not sleepy after sleeping
class CatTests(unittest.TestCase):
    NAME = 'Gary'

    def setUp(self) -> None:
        self.cat = Cat(self.NAME)

    def test_eat__increased_size__expect_increased(self):
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_eat__expect_cat_is_fed(self):
        self.cat.eat()
        self.assertEqual(True, self.cat.fed)

    def test_eat__if_cat_is_fed__expect_raise_error(self):
        self.cat.eat()

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertIsNotNone(ex)

    def test_sleep__if_cat_not_fed__expect_raise_error(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertIsNotNone(ex)

    def test_sleep__expect_sleepy_to_be_false(self):
        self.cat.eat()
        self.cat.sleep()

        self.assertEqual(False, self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()