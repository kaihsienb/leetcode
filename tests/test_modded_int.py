import unittest

from common.modded_int import ModdedInt


class TestModdedInt(unittest.TestCase):
    def test_basic_ops(self):
        M7 = ModdedInt(7)
        a = M7(3)
        b = M7(5)

        self.assertEqual((a + b).val, (3 + 5) % 7)
        self.assertEqual((a - b).val, (3 - 5) % 7)
        self.assertEqual((a * b).val, (3 * 5) % 7)

    def test_int_ops(self):
        M7 = ModdedInt(7)
        a = M7(3)

        self.assertEqual((a + 5).val, (3 + 5) % 7)
        self.assertEqual((5 + a).val, (5 + 3) % 7)
        self.assertEqual((a * 2).val, (3 * 2) % 7)

    def test_pow(self):
        M7 = ModdedInt(7)
        a = M7(3)

        self.assertEqual((a**2).val, (3**2) % 7)

    def test_mismatched_mod(self):
        M7 = ModdedInt(7)
        M5 = ModdedInt(5)
        a = M7(3)
        b = M5(3)

        with self.assertRaises(ValueError):
            c = a + b


if __name__ == "__main__":
    unittest.main()
