import unittest
from assess import *

class TestCase(unittest.TestCase):
    
    def test_grade_ave(self):
        self.assertIsInstance(grade_average([1,2,3,4,5]), float, "Expected a float")
        self.assertEqual(grade_average([1,2,3,4,5]), 3, "Unexpected output")
        self.assertEqual(grade_average([46, 78, 32, -5, 6]), 40.5, "Incorrect output")
        self.assertEqual(grade_average([-56, 94, -3, 0]), 47, "Unexpected output")
        self.assertEqual(grade_average([-2, -45, -82]), 0, "Unexpected output")
        self.assertEqual(grade_average([]), -1, None)


    def test_primes(self):
        self.assertIsInstance(find_prime_factors(5), list, "Expected a list")
        self.assertEqual(find_prime_factors(3), [3], None)
        self.assertEqual(find_prime_factors(78), [2, 3, 13], "Unexpected output")    

    def test_interest(self):
        self.assertIsInstance(calculate_interest(1000, 0.05, 5), float, "Expected a float")
        self.assertEqual(calculate_interest(1000, 0.05, 5), 1276.2815625000003, "Unexpected output")
        self.assertEqual(calculate_interest(1000, 0.1, 5), 1610.5100000000004, "Unexpected output")


    def test_code_word(self):
            self.assertIsInstance(code_word([3,1,20]), str, "Expected a string")
            self.assertEqual(code_word([16,25,20,8,15,14]), "python", "Unexpected output")
            self.assertEqual(code_word([14,1,20,21,18,5]), "nature", None)
            self.assertEqual(code_word([9,0,3,1,14,0,4,15,0,9,20]), "i can do it", "Unexpected output")


    def test_triangles(self):
        self.assertIsInstance(triangles(5), str, "Expected a string")
        self.assertEqual(triangles(3), "*\n**\n***", "Unexpected output")
        self.assertEqual(triangles(6), "*\n**\n***\n****\n*****\n******", "Unexpected output")
        self.assertEqual(triangles(7), "*\n**\n***\n****\n*****\n******\n*******", "Unexpected output")
        

    def test_hollow_triangles(self):
            self.assertIsInstance(hollow_triangle(5), str, "Expected a string")
            self.assertEqual(hollow_triangle(3), "*\n**\n***", "Unexpected output")
            self.assertEqual(hollow_triangle(6), "*\n**\n* *\n*  *\n*   *\n******", "Unexpected output")
            self.assertEqual(hollow_triangle(7), "*\n**\n* *\n*  *\n*   *\n*    *\n*******", "Unexpected output")
