from temperature_utils import convert_temperature
import unittest

class TestTemperatureConversion(unittest.TestCase):

    def test_invalid(self):
        self.assertRaises(ValueError, convert_temperature, -111, 'C', 'F')

    def test_valid(self):
        test_cases = [((273, 'K',), (0.2, 'C')),
                      ((-20, 'C'), (-30, 'F')),
                      ((340, 'F'), (901.39, 'K'))]

        for test_case in test_cases:
            ((from_val, from_unit), (to_val, to_unit)) = test_case
            result = convert_temperature(from_val, from_unit, to_unit)
            self.assertAlmostEqual(to_val, result)

    def test_no_conversion(self):
        t = 33.33
        result = convert_temperature(t, 'C', 'C')
        self.assertTrue(result is t)

    def test_incorrect_units(self):
        self.assertRaises(ValueError, convert_temperature, 0, 'C', 'R')
        self.assertRaises(ValueError, convert_temperature, 0, 'N', 'K')

unittest.main()