from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import User, Dictionary, Author
import json

def main(request):
    return render(request, "public/index.html")

# ---------------------------------------------- Users -----------------------------------------------------------------

def users_main(request):
    users_data = User.objects.all()
    return render(request, "public/users.html", {"users_data": users_data})


def admin_users_main(request):
    users_data = User.objects.all()
    return render(request, "public/users-admin.html", {"users_data": users_data})


def get_users(request):
    users_data = User.objects.all().values()
    return JsonResponse(list(users_data), safe=False)

# Отримання користувача за id
def get_user(request, id):
    try:
        user = User.objects.get(id=id)
        return JsonResponse(user.values())
    except User.DoesNotExist:
        return JsonResponse({"message": "User wasn't found!"}, status=404)

# Створення користувача
@csrf_exempt
def create_user(request):
    if request.method == "POST":
        data = request.POST
        new_user = User.objects.create(name=data["name"], age=data["age"])
        return JsonResponse(new_user.values(), status=201)
    else:
        return JsonResponse({"message": "Method not allowed"}, status=405)

# Редагування інформації для користувача
@csrf_exempt
def edit_user(request, id):
    if request.method == "PUT":
        data = json.loads(request.body)
        try:
            user = User.objects.get(id=id)
            user.name = data.get("name", user.name)
            user.age = data.get("age", user.age)
            user.save()
            return JsonResponse(user.values())
        except User.DoesNotExist:
            return JsonResponse({"message": "User wasn't found!"}, status=404)
    else:
        return JsonResponse({"message": "Method not allowed"}, status=405)

# Видалення користувача
@csrf_exempt
def delete_user(request, id):
    if request.method == "DELETE":
        try:
            user = User.objects.get(id=id)
            user.delete()
            return JsonResponse({"message": "User deleted successfully"})
        except User.DoesNotExist:
            return JsonResponse({"message": "User wasn't found!"}, status=404)
    else:
        return JsonResponse({"message": "Method not allowed"}, status=405)


# ---------------------------------------------- Dictionaries ----------------------------------------------------------

def dictionaries_main(request):
    dictionaries_data = Dictionary.objects.all()
    return render(request, "public/dictionaries.html", {"dictionaries_data": dictionaries_data})


def admin_dictionaries_main(request):
    dictionaries_data = Dictionary.objects.all()
    return render(request, "public/dictionaries-admin.html", {"dictionaries_data": dictionaries_data})


def get_dictionaries(request):
    dictionaries_data = Dictionary.objects.all().values()
    return JsonResponse(list(dictionaries_data), safe=False)

# Отримання словника за id
def get_dictionary(request, id):
    try:
        dictionary = Dictionary.objects.get(id=id)
        return JsonResponse(dictionary.values())
    except Dictionary.DoesNotExist:
        return JsonResponse({"message": "Dictionary wasn't found!"}, status=404)

# Створення словника
@csrf_exempt
def create_dictionary(request):
    if request.method == "POST":
        data = request.POST
        new_dictionary = Dictionary.objects.create(name=data["name"], pages=data["pages"], author=data["author"])
        created_dictionary = Dictionary.objects.filter(id=new_dictionary.id).values().first()
        return JsonResponse(created_dictionary, status=201)
    else:
        return JsonResponse({"message": "Method not allowed"}, status=405)

# Редагування інформації про словник
@csrf_exempt
def edit_dictionary(request, id):
    if request.method == "PUT":
        data = json.loads(request.body)
        try:
            dictionary = Dictionary.objects.get(id=id)
            dictionary.name = data.get("name", dictionary.name)
            dictionary.pages = data.get("pages", dictionary.pages)
            dictionary.author = data.get("author", dictionary.author)
            dictionary.save()
            return JsonResponse(dictionary.values())
        except Dictionary.DoesNotExist:
            return JsonResponse({"message": "Dictionary wasn't found!"}, status=404)
    else:
        return JsonResponse({"message": "Method not allowed"}, status=405)

# Видалення словника
@csrf_exempt
def delete_dictionary(request, id):
    if request.method == "DELETE":
        try:
            dictionary = Dictionary.objects.get(id=id)
            dictionary.delete()
            return JsonResponse({"message": "Dictionary deleted successfully"})
        except Dictionary.DoesNotExist:
            return JsonResponse({"message": "Dictionary wasn't found!"}, status=404)
    else:
        return JsonResponse({"message": "Method not allowed"}, status=405)

# ------------------------------------------------- Authors ------------------------------------------------------------

def authors_main(request):
    authors_data = Author.objects.all()
    return render(request, "public/authors.html", {"authors_data": authors_data})


def admin_authors_main(request):
    authors_data = Author.objects.all()
    return render(request, "public/authors-admin.html", {"authors_data": authors_data})

def get_authors(request):
    authors_data = Author.objects.all().values()
    return JsonResponse(list(authors_data), safe=False)

# Отримання автора за id
def get_author(request, id):
    try:
        author = Author.objects.get(id=id)
        return JsonResponse(author.values())
    except Author.DoesNotExist:
        return JsonResponse({"message": "Author wasn't found!"}, status=404)

# Реєстрація нового автора
@csrf_exempt
def create_author(request):
    if request.method == "POST":
        data = request.POST
        new_author = Author.objects.create(name=data["name"], books=data["books"], rating=data["rating"])
        return JsonResponse(new_author.values(), status=201)
    else:
        return JsonResponse({"message": "Method not allowed"}, status=405)

# Редагування інформації про автора
@csrf_exempt
def edit_author(request, id):
    if request.method == "PUT":
        data = json.loads(request.body)
        try:
            author = Author.objects.get(id=id)
            author.name = data.get("name", author.name)
            author.books = data.get("books", author.books)
            author.rating = data.get("rating", author.rating)
            author.save()
            return JsonResponse(author.values())
        except Author.DoesNotExist:
            return JsonResponse({"message": "Author wasn't found!"}, status=404)
    else:
        return JsonResponse({"message": "Method not allowed"}, status=405)

# Видалення автора
@csrf_exempt
def delete_author(request, id):
    if request.method == "DELETE":
        try:
            author = Author.objects.get(id=id)
            author.delete()
            return JsonResponse({"message": "Author deleted successfully"})
        except Author.DoesNotExist:
            return JsonResponse({"message": "Author wasn't found!"}, status=404)
    else:
        return JsonResponse({"message": "Method not allowed"}, status=405)
