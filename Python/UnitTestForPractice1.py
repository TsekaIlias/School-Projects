import re
import unittest
from erotima1 import compute 


class TestComputeFunction(unittest.TestCase):
    def test_manual_cases(self):
        self.assertEqual(compute("ΠΟΛΛΑΠΛΑΣΙΑΣΕ(10, 20)"), 200)
        self.assertEqual(compute("ΠΟΛΛΑΠΛΑΣΙΑΣΕ(03, 07)"), 21)
        self.assertEqual(compute("ΠΟΛΛΑΠΛΑΣΙΑΣΕ(50, 50)"), 2500)
        self.assertEqual(compute("ΠΟΛΛΑΠΛΑΣΙΑΣΕ(50, 50)ΠΟΛΛΑΠΛΑΣΙΑΣΕ(02, 03)"), 2506)
        self.assertEqual(compute("ΠΟΛΛΑΠΛΑΣΙΑΣΕ(5,5) ΠΟΛΛΑΠΛΑΣΙΑΣΕ(4,4)"), 25 + 16)
        self.assertEqual(compute("RandomText ΠΟΛΛΑΠΛΑΣΙΑΣΕ(99, 01) End"), 99)
        self.assertEqual(compute("ΠΟΛΛΑΠΛΑΣΙΑΣΕ( 3 , 5 )"), 15)
        self.assertEqual(compute("ΠΟΛΛΑΠΛΑΣΙΑΣΕ(25, 04) ΠΟΛΛΑΠΛΑΣΙΑΣΕ(12, 12)"), 100 + 144)


    def test_file_input(self):
        with open("test_multiplications1.txt", "r", encoding="utf-8") as file:
            content = file.read().strip()

        print("File Content:\n", content)
        matches = re.findall(r"ΠΟΛΛΑΠΛΑΣΙΑΣΕ\((\d{2}), (\d{2})\)", content)
        print("Extracted Multiplications:", matches)

        result = compute(content)
        print("Computed Sum:", result)

        self.assertEqual(result, 1035105)


if __name__ == "__main__":
    unittest.main()
