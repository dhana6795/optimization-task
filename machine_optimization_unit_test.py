
import machine_optimization
import unittest
from mock import patch

class TestOptimization(unittest.TestCase):
    def setUp(self):
        self.unit_price = {'10xl': 2820, '2xl': 450, '4xl': 774, '8xl': 1400, 'l': 120, 'xl': 230}
        self.cost_per_unit = {'10xl': 8.8125, '2xl': 11.25, '4xl': 9.675, '8xl': 8.75, 'l': 12.0, 'xl': 11.5}
        self.desired_capacity = 500
        self.output = [{'total_cost': '$120', 'region': 'new_york', 'machines': [('l', 1)]}, {'total_cost': '$110', 'region': 'china', 'machines': [('l', 1)]}, {'total_cost': '$140', 'region': 'india', 'machines': [('l', 1)]}]
    
    @patch('__builtin__.input')
    def test_main(self, params):
         self.assertEqual(machine_optimization.main(), self.output)
    
    def test_roundup(self):
        self.assertEqual(machine_optimization.roundup(14), 20)
    
    def test_find_low_cost_machine(self):
        number_of_min_machine_needed, min_machine, achieved_capacity_now = machine_optimization.find_low_cost_machine(self.unit_price, self.cost_per_unit, self.desired_capacity)
        self.assertEqual(number_of_min_machine_needed, 3)
        self.assertEqual(min_machine,'8xl')
        self.assertEqual(achieved_capacity_now, 480)

if __name__ == '__main__':
    unittest.main()

