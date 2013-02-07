import unittest
import simpatico


class TestNaming(unittest.TestCase):
    def test_good(self):
        f = 'tests/files/goodNaming.c'
        errors = simpatico.check(f)
        self.assertEqual(errors, [])

    def test_bad(self):
        f = 'tests/files/bad_naming.c'
        errors = simpatico.check(f)
        expected = [(f, 1, "NAMING", "File Naming Error: " + f),
                    (f, 5, "NAMING", "#define Naming Error: Pi"),
                    (f, 7, "NAMING", "Type Naming Error: struct bobStruct"),
                    (f, 13, "NAMING", "Type Naming Error: Bad_Struct"),
                    (f, 15, "NAMING", "Variable Naming Error: A"),
                    (f, 16, "NAMING", "Variable Naming Error: a_char"),
                    (f, 18, "NAMING", "Function Naming Error: FunctionBad"),
                    (f, 21, "NAMING", "Function Naming Error: functionStuff"),
                    (f, 24, "NAMING", "Variable Naming Error: BobStruct")]
        self.assertItemsEqual(errors, expected)

if __name__ == "__main__":
    unittest.main()
