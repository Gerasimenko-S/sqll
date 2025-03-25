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

insert_movies_query = """
INSERT INTO movies (title, release_year, genre, collection_in_mil)
VALUES
    ("Forrest Gump", 1994, "Drama", 330.2),
    ("3 Idiots", 2009, "Drama", 2.4),
    ("Eternal Sunshine of the Spotless Mind", 2004, "Drama", 34.5),
    ("Good Will Hunting", 1997, "Drama", 138.1),
    ("Skyfall", 2012, "Action", 304.6),
    ("Gladiator", 2000, "Action", 188.7),
    ("Black", 2005, "Drama", 3.0),
    ("Titanic", 1997, "Romance", 659.2),
    ("The Shawshank Redemption", 1994, "Drama", 28.4),
    ("Udaan", 2010, "Drama", 1.5),
    ("Home Alone", 1990, "Comedy", 286.9)
"""

with connection.cursor() as cursor:
    cursor.execute(insert_movies_query)
    connection.commit()


select_movies_query = "SELECT * FROM movies LIMIT 5"
with connection.cursor() as cursor:
    cursor.execute(select_movies_query)
    result = cursor.fetchall()
    for row in result:
        print(row)

update_query = """  
UPDATE  
    reviewers  
SET  
    last_name = "Cooper"  
WHERE  
    first_name = "Amy"  
"""
with connection.cursor() as cursor:
    cursor.execute(update_query)
    connection.commit()


delete_query = "DELETE FROM ratings WHERE reviewer_id = 2"
with connection.cursor() as cursor:
    cursor.execute(delete_query)
    connection.commit()

