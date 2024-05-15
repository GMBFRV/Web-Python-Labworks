from fastapi import FastAPI, Depends, Body, File
from fastapi.responses import JSONResponse, FileResponse
from pymongo import MongoClient
from bson.objectid import ObjectId

app = FastAPI()

MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DB = 'web_python'


def get_db():
    client = MongoClient(MONGO_HOST, MONGO_PORT)
    db = client[MONGO_DB]
    try:
        yield db
    finally:
        client.close()


# ---------------------------------------------- Користувачі -----------------------------------------------------------

@app.get("/")
def main():
    return FileResponse("public/index.html")


@app.get("/users")
def main():
    return FileResponse("public/users.html")


@app.get("/admin/users")
def main():
    return FileResponse("public/users-admin.html")


@app.get("/api/users")
def get_users(db: MongoClient = Depends(get_db)):
    users = db.people.find()
    users_list = []
    for user in users:
        user['_id'] = str(user['_id'])
        users_list.append(user)
    return users_list


@app.get("/api/users/{id}")
def get_person(id: str, db=Depends(get_db)):
    person = db.people.find_one({"_id": ObjectId(id)})
    if person is None:
        return JSONResponse(status_code=404, content={"message": "User wasn't found!"})
    person['_id'] = str(person['_id'])
    return person


@app.post("/api/users")
def create_person(data: dict = Body(...), db=Depends(get_db)):
    result = db.people.insert_one(data)
    return {"id": str(result.inserted_id), **data}


@app.put("/admin/api/users/{id}")
def edit_person(id: str, data: dict = Body(...), db=Depends(get_db)):
    db.people.update_one({"_id": ObjectId(id)}, {"$set": data})
    return {"id": id, **data}


@app.delete("/admin/api/users/{id}")
def delete_person(id: str, db=Depends(get_db)):
    db.people.delete_one({"_id": ObjectId(id)})
    return {"message": "User deleted successfully"}


# ------------------------------------------------ Словники ------------------------------------------------------------

@app.get("/dictionaries")
def dictionaries_main():
    return FileResponse("public/dictionaries.html")


@app.get("/admin/dictionaries")
def admin_dictionaries():
    return FileResponse("public/dictionaries-admin.html")


@app.get("/api/dictionaries")
def get_dictionaries(db=Depends(get_db)):
    dictionaries = db.dictionary.find()
    dictionaries_list = []
    for dictionary in dictionaries:
        dictionary['_id'] = str(dictionary['_id'])
        dictionaries_list.append(dictionary)
    return dictionaries_list


@app.get("/api/dictionaries/{id}")
def get_dictionary(id: str, db=Depends(get_db)):
    dictionary = db.dictionary.find_one({"_id": ObjectId(id)})
    if dictionary is None:
        return JSONResponse(status_code=404, content={"message": "Dictionary wasn't found!"})
    dictionary['_id'] = str(dictionary['_id'])
    return dictionary


@app.post("/api/dictionaries")
def create_dictionary(data: dict = Body(...), db=Depends(get_db)):
    result = db.dictionary.insert_one(data)
    return {"id": str(result.inserted_id), **data}


@app.put("/admin/api/dictionaries/{id}")
def edit_dictionary(id: str, data: dict = Body(...), db=Depends(get_db)):
    db.dictionary.update_one({"_id": ObjectId(id)}, {"$set": data})
    return {"id": id, **data}


@app.delete("/admin/api/dictionaries/{id}")
def delete_dictionary(id: str, db=Depends(get_db)):
    db.dictionary.delete_one({"_id": ObjectId(id)})
    return {"message": "Dictionary deleted successfully"}


# ---------------------------------------------- Автори ------------------------------------------------------------

@app.get("/authors")
def authors_main():
    return FileResponse("public/authors.html")


@app.get("/admin/authors")
def authors_main():
    return FileResponse("public/authors-admin.html")


@app.get("/api/authors")
def get_authors(db=Depends(get_db)):
    authors = db.authors.find()
    authors_list = []
    for author in authors:
        author['_id'] = str(author['_id'])
        authors_list.append(author)
    return authors_list


@app.get("/api/authors/{id}")
def get_author(id: str, db=Depends(get_db)):
    author = db.authors.find_one({"_id": ObjectId(id)})
    if author is None:
        return JSONResponse(status_code=404, content={"message": "Author wasn't found!"})
    author['_id'] = str(author['_id'])
    return author


@app.post("/admin/api/authors")
def create_author(data: dict = Body(...), db=Depends(get_db)):
    result = db.authors.insert_one(data)
    return {"id": str(result.inserted_id), **data}


@app.put("/admin/api/authors/{id}")
def edit_author(id: str, data: dict = Body(...), db=Depends(get_db)):
    db.authors.update_one({"_id": ObjectId(id)}, {"$set": data})
    return {"id": id, **data}


@app.delete("/admin/api/authors/{id}")
def delete_author(id: str, db=Depends(get_db)):
    db.authors.delete_one({"_id": ObjectId(id)})
    return {"message": "Author deleted successfully"}
