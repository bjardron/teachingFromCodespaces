import unittest

class TestMath(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 2, 4)
        self.assertEqual(3 + 3, 6)

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database()
        
    def tearDown(self):
        self.db.disconnect()
        
    def test_connection(self):
        self.db.connect()
        self.assertTrue(self.db.is_connected())
