import mysql.connector as mc
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        conn = mc.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return conn

def execute_query(conn, query,data = ()):
    cursor = conn.cursor()
    try:
        cursor.execute(query,data)
        conn.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def execute_read_query(conn, query):
    cursor = conn.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

# # Replace with your MySQL server details
# conn = create_connection("your_host", "your_username", "your_password", "your_database")

# # Example queries
# create_table_query = """
# CREATE TABLE IF NOT EXISTS users (
#     id INT AUTO_INCREMENT, 
#     name TEXT NOT NULL, 
#     age INT, 
#     gender TEXT, 
#     nationality TEXT, 
#     PRIMARY KEY (id)
# ) ENGINE = InnoDB;
# """

# execute_query(conn, create_table_query)

# # Insert data
# insert_users_query = """
# INSERT INTO users (name, age, gender, nationality) VALUES 
# ('James', 25, 'male', 'USA'), 
# ('Leila', 32, 'female', 'France'), 
# ('Brigitte', 35, 'female', 'UK');
# """

# execute_query(conn, insert_users_query)

# # Retrieve data
# select_users_query = "SELECT * from users"
# users = execute_read_query(conn, select_users_query)

# for user in users:
#     print(user)