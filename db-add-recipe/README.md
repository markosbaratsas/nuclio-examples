# Nuclio Examples: Add recipe to database

## Description
This example demonstrates how to connect and add data to a database, using nuclio functions. In this example, when the function is invoked, it inserts a new recipe in the database.

## How to implement:
1. First of all, database credentials along with the database schema are required to get this project up and running. In the `db/schema.sql` file, the database schema is provided. It contains only one table that holds the recipe data. After creating such a table in a PostgreSQL database, we can move onto the next step.
2. Execute the following command:
```
sudo nuctl deploy \
    --path PATH_TO_NUCLIO_EXAMPLES/nuclio-examples/db-add-recipe \
    --registry $(minikube ip):5000 \
    --run-registry localhost:5000 \
    --env db_host=DB_HOST \
    --env db_port=DB_PORT \
    --env db_user=DB_USER \
    --env db_password=DB_PASSWORD \
    --env db_database=DB_DATABASE_NAME
```
Fill in the information that are provided with capital letters(PATH_TO_NUCLIO_EXAMPLES, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_DATABASE_NAME).
3. Test the function, using port provided from the command executed in step 2. Using Postman, create a request towards `http://localhost:PORT_FROM_COMMAND`. Under body->raw->JSON provide the title and the instructions of the recipe. Those should look something like this:
```
{
    "title": "Sample Title for recipe 1",
    "instructions": "Sample instructions for recipe 1"
}
```
If everything is working as expected the response should look like this:
```
Inserted successfully.
```


## Next steps:
In order to retrieve the data inserted in the database, and actually check if the example is indeed performing as expected, the *db-list-recipes* example was created. It serves as extra validation that this example is working as expected.
