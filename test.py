import unittest
first=1.345
second=1.346
decimal=2
message="First and Second inputs are not equal."
delta=0.01

class DemoTest(unittest.TestCase):
    def test_almost_equal1(self):
        self.assertAlmostEqual(first, second,None,message,delta)

if __name__ == '__main__':
    unittest.main()