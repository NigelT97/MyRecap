import unittest
from base_model import BaseModel
from datetime import datetime

class BaseModel_test(unittest.TestCase):

    def test_initialization(self):
        basemodel1 = BaseModel()
        basemodel2 = BaseModel()

        self.assertNotEqual(basemodel1.id, basemodel2.id)
        self.assertIsInstance(basemodel1.id, str)
        self.assertIsInstance(basemodel2.created_at, datetime)
        self.assertIsInstance(basemodel2.updated_at, datetime)

if __name__ == "__main__":
    unittest.main()