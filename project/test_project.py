import unittest
import sqlite3
import os

from project import register, login, add_task, delete_task, display_tasks


class TestTodoFunctions(unittest.TestCase):
    def setUp(self):
        # Connect to an in-memory SQLite database
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()

        # Create tables
        self.cursor.execute('''
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT NOT NULL,
                user_id INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        ''')
        self.conn.commit()

    def tearDown(self):
        # Close the database connection
        self.conn.close()

    def test_register(self):
        # Test registration with a new username and password
        self.assertEqual(register("test_user", "test_password"), "Registration successful.")

        # Test registration with an existing username
        self.assertEqual(register("test_user", "test_password"),
                         "Username already exists. Please choose a different username.")

    def test_login(self):
        # Test login with correct username and password
        self.assertIsNotNone(login("test_user", "test_password"))

        # Test login with incorrect password
        self.assertIsNone(login("test_user", "wrong_password"))

    def test_add_task(self):
        user_id = login("test_user", "test_password")
        self.assertIsNotNone(user_id)

        # Test adding a task
        self.assertTrue(add_task("Test task", user_id))

    def test_delete_task(self):
        user_id = login("test_user", "test_password")
        self.assertIsNotNone(user_id)

        # Check if any tasks exist for the user
        self.cursor.execute('SELECT id FROM tasks WHERE user_id=?', (user_id,))
        task_row = self.cursor.fetchone()
        if task_row is None:
            # Add a task if none are found
            add_task("Test task", user_id)
            self.cursor.execute('SELECT id FROM tasks WHERE user_id=?', (user_id,))
            task_row = self.cursor.fetchone()
            if task_row is None:
                self.fail("Failed to add a task for the user.")
                return

        task_id = task_row[0]

        # Test deleting the task
        self.assertEqual(delete_task(task_id, user_id), "Task deleted successfully.")



    def test_display_tasks(self):
        user_id = login("test_user", "test_password")
        self.assertIsNotNone(user_id)

        # Test displaying tasks
        self.assertIsNone(display_tasks(user_id))


if __name__ == '__main__':
    unittest.main()
