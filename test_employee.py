import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('setupclass')

    @classmethod
    def tearDownClass(cls) -> None:
        print('tear_down_class')

    def setUp(self):
        self.emp1 = Employee('Esther', 'Jacinta', 230000)
        self.emp2 = Employee('Esther', 'Joy', 200000)

    def tearDown(self) -> None:
        pass

    def test_email(self):
        self.assertEqual(self.emp1.email, 'Esther.Jacinta@email.com')
        self.assertEqual(self.emp2.email, 'Esther.Joy@email.com')

        self.emp1.first = 'Jay'
        self.emp2.first = 'J'

        self.assertEqual(self.emp1.email, 'Jay.Jacinta@email.com')
        self.assertEqual(self.emp2.email, 'J.Joy@email.com')

    def test_fullname(self):
        self.assertEqual(self.emp1.fullname, 'Esther Jacinta')
        self.assertEqual(self.emp2.fullname, 'Esther Joy')

        self.emp1.first = 'Jay'
        self.emp2.first = 'J'

        self.assertEqual(self.emp1.fullname, 'Jay Jacinta')
        self.assertEqual(self.emp2.fullname, 'J Joy')


if __name__ == '__main__':
    unittest.main()
