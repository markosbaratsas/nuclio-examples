import json
import psycopg2
import os

def connect():
    try:
        connection = psycopg2.connect(host=os.environ['db_host'],
                                database=os.environ['db_database'],
                                user=os.environ['db_user'],
                                port=os.environ['db_port'],
                                password=os.environ['db_password'])
        return connection    
    except Error as e:
        return None
    

def handler(context, event):
    data = event.body

    if 'title' not in data or 'instructions' not in data:
        return "Please send a recipe request with title and instructions."

    title = data['title']
    instructions = data['instructions']
    if (str(type(title)) != "<class 'str'>"
            or str(type(instructions)) != "<class 'str'>"):
        return "Title and instructions should be str type."

    connection = connect()
    if connection == None:
        return "Error: Could not connect to database."

    try:
        insert_query = f"""INSERT INTO recipes(Title, Instructions)
                            VALUES ('{title}', '{instructions}') """

        cursor = connection.cursor()
        cursor.execute(insert_query)
        connection.commit()
        ret = f"Recipe added successfully."
        cursor.close()
    except:
        ret = f"Failed to insert recipe, because of database error."
    finally:
        cursor.close()
        connection.close()

    return ret


def init_context(context):
    connection = connect()
    if connection == None:
        return

    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS recipes (
            recipeID int NOT NULL AUTO_INCREMENT,
            Title varchar(255),
            Instructions varchar(1023),
            PRIMARY KEY (recipeID)
            );""")
        connection.commit()
        ret = f"Inserted successfully. Total recipes: {cursor.rowcount}"
        cursor.close()
    except:
        ret = f"Failed to insert record into Laptop table"
    finally:
        cursor.close()
        connection.close()
