from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

users_data = [
    {"id": 1, "name": "John", "age": 25},
    {"id": 2, "name": "Alice", "age": 30},
    {"id": 3, "name": "Bob", "age": 28}
]

dictionaries_data = [
    {"id": 1, "name": "English", "pages": 300, "author": "John Smith"},
    {"id": 2, "name": "French", "pages": 250, "author": "Alice Brown"},
    {"id": 3, "name": "German", "pages": 200, "author": "Bob Green"}
]

authors_data = [
    {"id": 1, "name": "Stephen King", "books": 63, "rating": 4.3},
    {"id": 2, "name": "J.K. Rowling", "books": 14, "rating": 4.7},
    {"id": 3, "name": "George R.R. Martin", "books": 27, "rating": 4.5}
]

def main(request):
    return render(request, "public/index.html")

# ---------------------------------------------- Users -----------------------------------------------------------------

def users_main(request):
    return render(request, "public/users.html", {"users_data": users_data})


def admin_users_main(request):
    return render(request, "public/users-admin.html", {"users_data": users_data})


def get_users(request):
    return JsonResponse(users_data, safe=False)

# Отримання користувача за id
def get_user(request, id):
    user = next((user for user in users_data if user["id"] == id), None)
    if user:
        return JsonResponse(user)
    else:
        return JsonResponse({"message": "User wasn't found!"}, status=404)

# Створення користувача
def create_user(request):
    if request.method == "POST":
        data = request.POST
        new_id = max(user["id"] for user in users_data) + 1
        new_user = {"id": new_id, "name": data["name"], "age": data["age"]}
        users_data.append(new_user)
        return JsonResponse(new_user, status=201)
    else:
        return JsonResponse({"message": "Method not allowed"}, status=405)

# Редагування інформації для користувача
@csrf_exempt
def edit_user(request, id):
    if request.method == "PUT":
        data = json.loads(request.body)
        user = next((user for user in users_data if user["id"] == int(id)), None)
        if user:
            user["name"] = data.get("name", user["name"])
            user["age"] = data.get("age", user["age"])
            return JsonResponse(user)
        else:
            return JsonResponse({"message": "User wasn't found!"}, status=404)
    else:
        return JsonResponse({"message": "Method not allowed"}, status=405)

# Видалення користувача
@csrf_exempt
def delete_user(request, id):
    if request.method == "DELETE":
        global users_data
        users_data = [user for user in users_data if user["id"] != int(id)]
        return JsonResponse({"message": "User deleted successfully"})
    else:
        return JsonResponse({"message": "Method not allowed"}, status=405)


# ---------------------------------------------- Dictionaries ----------------------------------------------------------

def dictionaries_main(request):
    return render(request, "public/dictionaries.html", {"dictionaries_data": dictionaries_data})


def admin_dictionaries_main(request):
    return render(request, "public/dictionaries-admin.html", {"dictionaries_data": dictionaries_data})


def get_dictionaries(request):
    return JsonResponse(dictionaries_data, safe=False)

# Отримання словника за id
def get_dictionary(request, id):
    dictionary = next((dictionary for dictionary in dictionaries_data if dictionary["id"] == int(id)), None)
    if dictionary:
        return JsonResponse(dictionary)
    else:
        return JsonResponse({"message": "Dictionary wasn't found!"}, status=404)

# Створення словника
@csrf_exempt
def create_dictionary(request):
    if request.method == "POST":
        data = request.POST
        new_id = max(dictionary["id"] for dictionary in dictionaries_data) + 1
        new_dictionary = {"id": new_id, "name": data["name"], "pages": data["pages"], "author": data["author"]}
        dictionaries_data.append(new_dictionary)
        return JsonResponse(new_dictionary, status=201)
    else:
        return JsonResponse({"message": "Method not allowed"}, status=405)

# Редагування інформації про словник
@csrf_exempt
def edit_dictionary(request, id):
    if request.method == "PUT":
        data = json.loads(request.body)
        dictionary = next((dictionary for dictionary in dictionaries_data if dictionary["id"] == int(id)), None)
        if dictionary:
            dictionary["name"] = data.get("name", dictionary["name"])
            dictionary["pages"] = data.get("pages", dictionary["pages"])
            dictionary["author"] = data.get("author", dictionary["author"])
            return JsonResponse(dictionary)
        else:
            return JsonResponse({"message": "Dictionary wasn't found!"}, status=404)
    else:
        return JsonResponse({"message": "Method not allowed"}, status=405)

# Видалення словника
@csrf_exempt
def delete_dictionary(request, id):
    if request.method == "DELETE":
        global dictionaries_data
        dictionaries_data = [dictionary for dictionary in dictionaries_data if dictionary["id"] != int(id)]
        return JsonResponse({"message": "Dictionary deleted successfully"})
    else:
        return JsonResponse({"message": "Method not allowed"}, status=405)

# ------------------------------------------------- Authors ------------------------------------------------------------

def authors_main(request):
    return render(request, "public/authors.html", {"authors_data": authors_data})


def admin_authors_main(request):
    return render(request, "public/authors-admin.html", {"authors_data": authors_data})

def get_authors(request):
    return JsonResponse(authors_data, safe=False)

# Отримання автора за id
def get_author(request, id):
    author = next((author for author in authors_data if author["id"] == id), None)
    if author:
        return JsonResponse(author)
    else:
        return JsonResponse({"message": "Author wasn't found!"}, status=404)

# Реєстрація нового автора
@csrf_exempt
def create_author(request):
    if request.method == "POST":
        data = request.POST
        new_id = max(author["id"] for author in authors_data) + 1
        new_author = {"id": new_id, "name": data["name"], "books": data["books"], "rating": data["rating"]}
        authors_data.append(new_author)
        return JsonResponse(new_author, status=201)
    else:
        return JsonResponse({"message": "Method not allowed"}, status=405)

# Редагування інформації про автора
@csrf_exempt
def edit_author(request, id):
    if request.method == "PUT":
        data = json.loads(request.body)
        author = next((author for author in authors_data if author["id"] == int(id)), None)
        if author:
            author["name"] = data.get("name", author["name"])
            author["books"] = data.get("books", author["books"])
            author["rating"] = data.get("rating", author["rating"])
            return JsonResponse(author)
        else:
            return JsonResponse({"message": "Author wasn't found!"}, status=404)
    else:
        return JsonResponse({"message": "Method not allowed"}, status=405)

# Видалення автора
@csrf_exempt
def delete_author(request, id):
    if request.method == "DELETE":
        global authors_data
        authors_data = [author for author in authors_data if author["id"] != int(id)]
        return JsonResponse({"message": "Author deleted successfully"})
    else:
        return JsonResponse({"message": "Method not allowed"}, status=405)
