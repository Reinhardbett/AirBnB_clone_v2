import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
from models import storage
from models.base_model import BaseModel

class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        '''Set up test environment.'''
        self.console = HBNBCommand()

    def tearDown(self):
        '''Tear down test environment.'''
        storage.all().clear()

    def test_create_missing_class_name(self):
        '''Test output when no class name.'''
        with patch('sys.stdout', new=StringIO()) as cli:
            self.console.onecmd("create")
            self.assertEqual("** class name missing **\n", cli.getvalue())

    def test_create_nonexistent_class(self):
        '''Test when user gives nonexistent class'''
        with patch('sys.stdout', new=StringIO()) as cli:
            self.console.onecmd('create BaseModel name="My_little_house" height=5.9')
            output = cli.getvalue().strip()
            self.assertTrue(output) #Check that an ID was printed
            new_instance = storage.all()["BaseModel." + output]
            self.assertEqual(new_instance.name, "My little house")
            self.assertEqual(new_instance.height, 5.9)

    def test_create_invalid_parameters(self):
        '''Test creating an instance with some invalid parameters.'''
        with patch('sys.stdout', new=StringIO()) as cli:
            self.console.onecmd('create BaseModel name="Valid_name" invalid_param=some_value age=25')
            output = cli.getvalue().strip()
            self.assertTrue(output)
            new_instance = storage.all()["BaseModel." + output]
            self.assertEqual(new_instance.name, "Valid name")
            self.assertEqual(new_instance.age, 25)
            # Check if invalid parameter was skipped
            self.assertFalse(hasattr(new_instance, 'invalid_param'))

if __name__ == "__main__":
    unittest.main()
