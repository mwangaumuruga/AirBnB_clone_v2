import unittest
import MySQLdb
import os

class TestCreateState(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.conn = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST'),
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB')
        )
        cls.cursor = cls.conn.cursor()

    @classmethod
    def tearDownClass(cls):
        cls.cursor.close()
        cls.conn.close()

    def test_create_state(self):
        # Count records before
        self.cursor.execute("SELECT COUNT(*) FROM states")
        initial_count = self.cursor.fetchone()[0]

        # Execute the command to create a new state
        os.system('echo "create State name=\'California\'" | ./console.py')

        # Count records after
        self.cursor.execute("SELECT COUNT(*) FROM states")
        final_count = self.cursor.fetchone()[0]

        # Validate the change
        self.assertEqual(final_count, initial_count + 1)

if __name__ == '__main__':
    unittest.main()
