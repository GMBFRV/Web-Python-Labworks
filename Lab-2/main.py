import psycopg2
from fastapi import FastAPI, Depends, Body, File
from fastapi.responses import JSONResponse, FileResponse
from typing import List

app = FastAPI()

POSTGRES_USER = 'postgres'
POSTGRES_PASSWORD = 'postgres'
POSTGRES_DB = 'Web-Python'
POSTGRES_HOST = 'localhost'
POSTGRES_PORT = '5432'


def get_db():
    conn = psycopg2.connect(
        dbname=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        host=POSTGRES_HOST,
        port=POSTGRES_PORT
    )
    try:
        yield conn
    finally:
        conn.close()


# ---------------------------------------------- Користувачі -----------------------------------------------------------

# Вітальна коренева сторінка
@app.get("/")
def main():
    return FileResponse("public/index.html")


# Сторінка для перегляду списку користувачів
@app.get("/users")
def main():
    return FileResponse("public/users.html")


# Сторінка для перегляду списку користувачів (Адмін)
@app.get("/admin/users")
def main():
    return FileResponse("public/users-admin.html")


# Отримання списку користувачів
@app.get("/api/users")
def get_people(db: psycopg2.connect = Depends(get_db)):
    cur = db.cursor()
    cur.execute("SELECT * FROM people;")
    result = cur.fetchall()
    cur.close()
    return result


# Отримання інформації про конкретного користувача (id)
@app.get("/api/users/{id}")
def get_person(id: int, db: psycopg2.connect = Depends(get_db)):
    cur = db.cursor()
    cur.execute("SELECT * FROM people WHERE id = %s;", (id,))
    result = cur.fetchone()
    cur.close()
    if result is None:
        return JSONResponse(status_code=404, content={"message": "User wasn't found!"})
    return result


# Створення нового користувача
@app.post("/api/users")
def create_person(data: dict = Body(...), db: psycopg2.connect = Depends(get_db)):
    cur = db.cursor()
    cur.execute("INSERT INTO people (name, age) VALUES (%s, %s) RETURNING id;", (data["name"], data["age"]))
    new_id = cur.fetchone()[0]
    db.commit()
    cur.close()
    return {"id": new_id, **data}


# Зміна інформації про користувача
@app.put("/admin/api/users/{id}")
def edit_person(id: int, data: dict = Body(...), db: psycopg2.connect = Depends(get_db)):
    cur = db.cursor()
    cur.execute("UPDATE people SET name = %s, age = %s WHERE id = %s;", (data["name"], data["age"], id))
    db.commit()
    cur.close()
    return {"id": id, **data}


# Видалення користувача
@app.delete("/admin/api/users/{id}")
def delete_person(id: int, db: psycopg2.connect = Depends(get_db)):
    cur = db.cursor()
    cur.execute("DELETE FROM people WHERE id = %s;", (id,))
    db.commit()
    cur.close()
    return {"message": "User deleted successfully"}


# ------------------------------------------------ Словники ------------------------------------------------------------

@app.get("/dictionaries")
def dictionaries_main():
    return FileResponse("public/dictionaries.html")


@app.get("/admin/dictionaries")
def admin_dictionaries():
    return FileResponse("public/dictionaries-admin.html")


@app.get("/api/dictionaries")
def get_dictionaries(db: psycopg2.connect = Depends(get_db)):
    cur = db.cursor()
    cur.execute("SELECT * FROM dictionary;")
    result = cur.fetchall()
    cur.close()
    return result


@app.get("/api/dictionaries/{id}")
def get_dictionary(id: int, db: psycopg2.connect = Depends(get_db)):
    cur = db.cursor()
    cur.execute("SELECT * FROM dictionary WHERE id = %s;", (id,))
    result = cur.fetchone()
    cur.close()
    if result is None:
        return JSONResponse(status_code=404, content={"message": "Dictionary wasn't found!"})
    return result


@app.post("/admin/api/dictionaries")
def create_dictionary(data: dict = Body(...), db: psycopg2.connect = Depends(get_db)):
    cur = db.cursor()
    cur.execute("INSERT INTO dictionary (name, pages, author) VALUES (%s, %s, %s) RETURNING id;",
                (data["name"], data["pages"], data["author"]))
    new_id = cur.fetchone()[0]
    db.commit()
    cur.close()
    return {"id": new_id, **data}


@app.put("/admin/api/dictionaries/{id}")
def edit_dictionary(id: int, data: dict = Body(...), db: psycopg2.connect = Depends(get_db)):
    cur = db.cursor()
    cur.execute("UPDATE dictionary SET name = %s, pages = %s, author = %s WHERE id = %s;",
                (data["name"], data["pages"], data["author"], id))
    db.commit()
    cur.close()
    return {"id": id, **data}


@app.delete("/admin/api/dictionaries/{id}")
def delete_dictionary(id: int, db: psycopg2.connect = Depends(get_db)):
    cur = db.cursor()
    cur.execute("DELETE FROM dictionary WHERE id = %s;", (id,))
    db.commit()
    cur.close()
    return {"message": "Dictionary deleted successfully"}


# ---------------------------------------------- Автори ------------------------------------------------------------

@app.get("/authors")
def authors_main():
    return FileResponse("public/authors.html")


@app.get("/admin/authors")
def authors_main():
    return FileResponse("public/authors-admin.html")


@app.get("/api/authors")
def get_authors(db: psycopg2.connect = Depends(get_db)):
    cur = db.cursor()
    cur.execute("SELECT * FROM authors;")
    result = cur.fetchall()
    cur.close()
    return result


@app.get("/api/authors/{id}")
def get_author(id: int, db: psycopg2.connect = Depends(get_db)):
    cur = db.cursor()
    cur.execute("SELECT * FROM authors WHERE id = %s;", (id,))
    result = cur.fetchone()
    cur.close()
    if result is None:
        return JSONResponse(status_code=404, content={"message": "Author wasn't found!"})
    return result


@app.post("/admin/api/authors")
def create_author(data: dict = Body(...), db: psycopg2.connect = Depends(get_db)):
    cur = db.cursor()
    cur.execute("INSERT INTO authors (name, books, rating) VALUES (%s, %s, %s) RETURNING id;",
                (data["name"], data["books"], data["rating"]))
    new_id = cur.fetchone()[0]
    db.commit()
    cur.close()
    return {"id": new_id, **data}


@app.put("/admin/api/authors/{id}")
def edit_author(id: int, data: dict = Body(...), db: psycopg2.connect = Depends(get_db)):
    cur = db.cursor()
    cur.execute("UPDATE authors SET name = %s, books = %s, rating = %s WHERE id = %s;",
                (data["name"], data["books"], data["rating"], id))
    db.commit()
    cur.close()
    return {"id": id, **data}


@app.delete("/admin/api/authors/{id}")
def delete_author(id: int, db: psycopg2.connect = Depends(get_db)):
    cur = db.cursor()
    cur.execute("DELETE FROM authors WHERE id = %s;", (id,))
    db.commit()
    cur.close()
    return {"message": "Author deleted successfully"}
