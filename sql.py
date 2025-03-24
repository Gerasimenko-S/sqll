import mysql.connector
from getpass import getpass
from mysql.connector import Error, connect


#def connect_to():
try:
    with connect(
            host="localhost",
            user=input("Имя пользователя: "),
            password=getpass("Пароль: "),
    ) as connection:
        print(connection)
except Error as e:
    print(e)


#def make_a_database():
try:
    with connect(
            host="localhost",
            user=input("Имя пользователя: "),
            password=getpass("Пароль: "),
    ) as connection:
        create_db_query = "CREATE DATABASE online_movie_rating"
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)

except Error as e:\
    print(e)


#def connect_to_database():
try:
    with connect(
            host="localhost",
            user=input("Имя пользователя: "),
            password=getpass("Пароль: "),
            database="online_movie_rating",
    )as connection:
        print(connection)

except Error as e:
        print(e)


#def make_a_movie_table():
create_movies_table_query = """
CREATE TABLE  movies(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    release_year YEAR(4),
    genre VARCHAR(100),
    collection_in_mil INT
)
"""
with connection.cursor() as cursor:
    cursor.execute(create_movies_table_query)
    connection.commit()


#def make_a_reviewers_table():
create_reviewers_table_query = """
CREATE TABLE  reviewers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100),
    second_name VARCHAR(100)
)
"""
with connection.cursor() as cursor:
    cursor.execute(create_reviewers_table_query)
    connection.commit()


#def make_a_ratings_table():
create_ratings_table_query = """
CREATE TABLE  ratings (
    movie_id INT,
    reviewer_id INT,
    rating DECIMAL(2,1),
    FOREIGN KEY(movie_id) REFERENCES movies(id),
    FOREIGN KEY(reviewer_id) REFERENCES reviewers(id),
    PRIMARY KEY(movie_id, reviewers_id)
)
"""
with connection.cursor() as cursor:
    cursor.execute(create_ratings_table_query)
    connection.commit()

