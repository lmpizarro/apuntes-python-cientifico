import unittest

def f1 (n1, n2):
    return n1 + n2

def f2 (n1, n2):
    return n1 > n2

def f3 (n1):
    return 2*n1

class TestStringMethods(unittest.TestCase):

  def test_upper(self):
      self.assertEqual('foo'.upper(), 'FOO')

  def test_isupper(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())

  def test_split(self):
      s = 'hello world'
      self.assertEqual(s.split(), ['hello', 'world'])
      # check that s.split fails when the separator is not a string
      with self.assertRaises(TypeError):
          s.split(2)

  def test_f2a (self):
      self.assertTrue(f2(4,2), 4)

  def test_f2b (self):
      self.assertFalse(f2(2,4), 4)


  def test_f1 (self):
      self.assertEqual(f1(2,2), 4)

  def test_f3 (self):
      self.assertEqual(f3(2), 6)


if __name__ == '__main__':
    unittest.main()
