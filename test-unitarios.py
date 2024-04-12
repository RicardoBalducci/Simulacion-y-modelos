import unittest
from Euler.Euler import euler

class EulerTest(unittest.TestCase):
    def test_euler(self):
        def f(x, y):
            return 2 * x
        
        x0 = 0
        y0 = 1
        h = 0.1
        n = 10
        
        x_values, y_values = euler(f, x0, y0, h, n)
        
        # Realiza las aserciones para verificar los resultados esperados
        self.assertEqual(len(x_values), n+1)
        self.assertEqual(len(y_values), n+1)
        self.assertAlmostEqual(x_values[0], x0)
        self.assertAlmostEqual(y_values[0], y0)
        # Añade más aserciones según sea necesario
        
if __name__ == '__main__':
    unittest.main()