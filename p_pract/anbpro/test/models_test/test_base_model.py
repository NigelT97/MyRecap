import unittest
from models.base_model import BaseModel

class BaseModel_test(unittest.TestCase):

    def test_initialization(self):
        basemodel1 = BaseModel()
        basemodel2 = BaseModel()

        self.assertNotEqual(basemodel1.id, basemodel2.id)

if __name__ == "__main__":
    unittest.main()


