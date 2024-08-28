import sqlite3
import bcrypt
import getpass

# Connect to SQLite database
conn = sqlite3.connect('todo.db')
cursor = conn.cursor()

# Create users and tasks tables if they don't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
''')
conn.commit()


def register(username, password):
    try:
        # Check if the username already exists
        cursor.execute('SELECT id FROM users WHERE username=?', (username,))
        existing_user = cursor.fetchone()
        if existing_user:
            return "Username already exists. Please choose a different username."

        # If username doesn't exist, proceed with registration
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)',
                       (username, hashed_password))
        conn.commit()
        return "Registration successful."
    except sqlite3.Error as e:
        conn.rollback()
        print(f"Database error: {e}")
        return "Database error. Please try again later."
    except Exception as e:
        print(f"Error during registration: {e}")
        return "An error occurred during registration."


def login(username, password):
    try:
        cursor.execute('SELECT id, password FROM users WHERE username=?', (username,))
        user = cursor.fetchone()
        if user:
            user_id, hashed_password = user
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                return user_id
        return None
    except sqlite3.Error as e:
        return f"Database error: {e}"
    except Exception as e:
        return f"Error during login: {e}"


def add_task(task, user_id):
    try:
        cursor.execute('INSERT INTO tasks (task, user_id) VALUES (?, ?)', (task, user_id))
        conn.commit()
        return True  # Return True if the task is added successfully
    except sqlite3.Error as e:
        conn.rollback()
        print(f"Database error: {e}")
        return False  # Return False if an error occurs
    except Exception as e:
        print(f"Error adding task: {e}")
        return False  # Return False if an error occurs


def delete_task(task_id, user_id):
    try:
        cursor.execute('DELETE FROM tasks WHERE id=? AND user_id=?', (task_id, user_id))
        conn.commit()
        return "Task deleted successfully."
    except sqlite3.Error as e:
        conn.rollback()
        return f"Database error: {e}"
    except Exception as e:
        return f"Error deleting task: {e}"


def display_tasks(user_id):
    try:
        cursor.execute('SELECT * FROM tasks WHERE user_id=?', (user_id,))
        tasks = cursor.fetchall()
        if tasks:
            print("Your tasks:")
            for task_id, task, _ in tasks:
                print(f"{task_id}. {task}")
        else:
            print("No tasks.")
    except sqlite3.Error as e:
        return f"Database error: {e}"
    except Exception as e:
        return f"Error displaying tasks: {e}"


def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            register(username, password)
        elif choice == '2':
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            user_id = login(username, password)
            if user_id:
                print("Login successful.")
                while True:
                    print("\n1. Add Task")
                    print("2. Delete Task")
                    print("3. View Tasks")
                    print("4. Logout")
                    sub_choice = input("Enter your choice: ")

                    if sub_choice == '1':
                        task = input("Enter task: ")
                        add_task(task, user_id)
                    elif sub_choice == '2':
                        task_id = input("Enter task ID to delete: ")
                        delete_task(task_id, user_id)
                    elif sub_choice == '3':
                        display_tasks(user_id)
                    elif sub_choice == '4':
                        print("Logged out.")
                        break
                    else:
                        print("Invalid choice.")
            else:
                print("Invalid username or password.")
        elif choice == '3':
            print("Exiting.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
