


class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'

# Test if the worker is initialized with the correct name, salary, and energy
#
# ·#Test if the worker's energy is incremented after the rest method is called
#
# · Test if an error is raised if the worker tries to work with negative energy or equal to 0
#
# · Test if the worker's money is increased by his salary correctly after the work method is called
#
# · Test if the worker's energy is decreased after the work method is called
#
# · Test if the get_info method returns the proper string with correct values

import unittest

class WorkerTests(unittest.TestCase):
    NAME = 'Test Worker'
    SALARY = 1024
    ENERGY = 1

    def setUp(self) -> None:
        self.worker = Worker(self.NAME, self.SALARY, self.ENERGY)

    def test_init_when_valid_props_expect_correct_values(self):
        self.assertEqual(self.NAME, self.worker.name)
        self.assertEqual(self.SALARY, self.worker.salary)
        self.assertEqual(self.ENERGY, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_rest_expect_energy_to_be_incremented(self):
        self.worker.rest()
        self.assertEqual(self.ENERGY + 1, self.worker.energy)

    def test_work_if_energy_is_0_expect_to_raise(self):
        worker = Worker(self.NAME, self.SALARY, 0)
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertIsNotNone(ex)

    def test_work_when_enough_energy_expect_money_to_be_increased_by_salary(self):
        self.worker.work()
        self.assertEqual(self.SALARY, self.worker.money)

    def test_work_when_enough_energy_expect_energy_to_decrement(self):
        self.worker.work()
        self.assertEqual(self.ENERGY - 1, self.worker.energy)

    def test_get_info_expect_correct_result(self):
        actual_info = self.worker.get_info()
        expected_info = f'{self.NAME} has saved {0} money.'

        self.assertEqual(expected_info, actual_info)

