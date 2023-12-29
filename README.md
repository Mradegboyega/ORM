# SQLAlchemy ORM Learning Project

This project serves as a hands-on learning experience for SQLAlchemy ORM (Object-Relational Mapping). The goal is to understand how to interact with a relational database using Python classes and objects.

## Project Structure

The project is organized as follows:

- **models.py**: Contains the SQLAlchemy models (`User` and `Comment`) that define the structure of the database tables and their relationships.

- **main.py**: Initializes the SQLAlchemy session and provides a centralized place for interacting with the database.

- **selec_join.py**: Demonstrates a SELECT query with a JOIN operation to retrieve specific data from the database.

- **persist.py**: Illustrates the usage of SQLAlchemy to insert, update, and delete records in the database.

## Running the Project

1. Ensure you have the necessary dependencies installed:

pip install -r requirements.txt

markdown


2. Run the project files:

python3 main.py
python3 selec_join.py
python3 persist.py

markdown


## Learning Objectives

- Define SQLAlchemy models to represent database tables.
- Establish relationships between tables using foreign keys and relationships.
- Perform CRUD operations (Create, Read, Update, Delete) using SQLAlchemy.
- Use SQLAlchemy queries to retrieve and manipulate data.

## Notes

- The project uses SQLite as the database engine for simplicity. You can modify the `create_engine` statement in `main.py` to connect to a different database.

- Feel free to explore and modify the code to deepen your understanding of SQLAlchemy ORM.

Happy learning!