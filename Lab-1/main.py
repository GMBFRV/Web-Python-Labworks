from database import *
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, Body
from fastapi.responses import JSONResponse, FileResponse

# Створення таблиць
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Визначення залежностей
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------------------------------------- Користувачі -----------------------------------------------------------

# Вітальна коренева сторінка
@app.get("/")
def main():
    return FileResponse("public/index.html")

# Сторінка для перегляду списку користувачів
@app.get("/users")
def main():
    return FileResponse("public/users.html")

@app.get("/api/users")
def get_people(db: Session = Depends(get_db)):
    return db.query(Person).all()

@app.get("/admin/users")
def main():
    return FileResponse("public/users-admin.html")

@app.get("/api/users/{id}")
def get_person(id, db: Session = Depends(get_db)):
    person = db.query(Person).filter(Person.id == id).first()
    if person is None:
        return JSONResponse(status_code=404, content={"message": "User wasn't found!"})
    return person


@app.post("/api/users")
def create_person(data=Body(), db: Session = Depends(get_db)):
    person = Person(name=data["name"], age=data["age"])
    db.add(person)
    db.commit()
    db.refresh(person)
    return person


@app.put("/admin/api/users")
def edit_person(data=Body(), db: Session = Depends(get_db)):
    person = db.query(Person).filter(Person.id == data["id"]).first()
    if person is None:
        return JSONResponse(status_code=404, content={"message": "User wasn't found!"})
    person.age = data["age"]
    person.name = data["name"]
    db.commit()
    db.refresh(person)
    return person


@app.delete("/api/users/{id}")
def delete_person(id, db: Session = Depends(get_db)):
    person = db.query(Person).filter(Person.id == id).first()
    if person is None:
        return JSONResponse(status_code=404, content={"message": "User wasn't found!"})
    db.delete(person)
    db.commit()
    return person


# ------------------------------------------------ Словники ------------------------------------------------------------

@app.get("/dictionaries")
def dictionaries_main():
    return FileResponse("public/dictionaries.html")


@app.get("/admin/dictionaries")
def admin_dictionaries():
    return FileResponse("public/dictionaries-admin.html")


@app.get("/admin/api/dictionaries")
def get_dictionaries(db: Session = Depends(get_db)):
    return db.query(Dictionary).all()


@app.get("/api/dictionaries")
def get_dictionaries(db: Session = Depends(get_db)):
    return db.query(Dictionary).all()


@app.get("/api/dictionaries/{id}")
def get_dictionary(id, db: Session = Depends(get_db)):
    dictionary = db.query(Dictionary).filter(Dictionary.id == id).first()
    if dictionary is None:
        return JSONResponse(status_code=404, content={"message": "Dictionary wasn't found!"})
    return dictionary


@app.post("/admin/api/dictionaries")
def create_dictionary(data=Body(), db: Session = Depends(get_db)):
    dictionary = Dictionary(name=data["name"], pages=data["pages"], author=data["author"])
    db.add(dictionary)
    db.commit()
    db.refresh(dictionary)
    return dictionary


@app.put("/admin/api/dictionaries")
def edit_dictionary(data: dict = Body(...), db: Session = Depends(get_db)):
    dictionary = db.query(Dictionary).filter(Dictionary.id == data["id"]).first()
    if dictionary is None:
        return JSONResponse(status_code=404, content={"message": "Dictionary wasn't found!"})
    dictionary.author = data["author"]
    dictionary.name = data["name"]
    dictionary.pages = data["pages"]
    db.commit()
    db.refresh(dictionary)
    return dictionary


@app.delete("/admin/api/dictionaries/{id}")
def delete_dictionary(id, db: Session = Depends(get_db)):
    dictionary = db.query(Dictionary).filter(Dictionary.id == id).first()
    if dictionary is None:
        return JSONResponse(status_code=404, content={"message": "Dictionary wasn't found!"})
    db.delete(dictionary)
    db.commit()
    return dictionary


# -------------------------------------------------- Автори ------------------------------------------------------------

@app.get("/authors")
def authors_main():
    return FileResponse("public/authors.html")


@app.get("/api/authors")
def get_authors(db: Session = Depends(get_db)):
    return db.query(Authors).all()

@app.get("/api/authors/{id}")
def get_author(id, db: Session = Depends(get_db)):
    author = db.query(Authors).filter(Authors.id == id).first()
    if author is None:
        return JSONResponse(status_code=404, content={"message": "Author wasn't found!"})
    return author

# --------------------------------------------- Автори (Admin) ---------------------------------------------------------

@app.get("/admin/authors")
def authors_main():
    return FileResponse("public/authors-admin.html")


@app.get("/admin/api/authors")
def get_authors(db: Session = Depends(get_db)):
    return db.query(Authors).all()


@app.post("/admin/api/authors")
def post_author(data=Body(), db: Session = Depends(get_db)):
    author = Authors(name=data["name"], books=data["books"], rating=data["rating"])
    db.add(author)
    db.commit()
    db.refresh(author)
    return author


@app.put("/admin/api/authors")
def edit_author(data=Body(), db: Session = Depends(get_db)):
    author = db.query(Authors).filter(Authors.id == data["id"]).first()
    if author is None:
        return JSONResponse(status_code=404, content={"message": "Sorry, author not found!"})
    author.books = data["books"]
    author.name = data["name"]
    author.rating = data["rating"]
    db.commit()
    db.refresh(author)
    return author


@app.delete("/api/authors/{id}")
def delete_author(id, db: Session = Depends(get_db)):
    author = db.query(Authors).filter(Authors.id == id).first()
    if author is None:
        return JSONResponse(status_code=404, content={"message": "Sorry, author not found!"})
    db.delete(author)
    db.commit()
    return author
