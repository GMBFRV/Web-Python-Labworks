from django.urls import path
from lab4 import views

urlpatterns = [
    path('', views.main, name='main'),
    # Маршрути для користувачів
    path('users/', views.users_main, name='users_main'),
    path('admin/users/', views.admin_users_main, name='admin_users_main'),
    path('api/users/', views.get_users, name='get_users'),
    path('api/users/<int:id>/', views.get_user, name='get_user'),
    path('admin/api/users/', views.create_user, name='create_user'),
    path('edit_user/<id>/', views.edit_user, name='edit_user'),
    path('delete_user/<id>/', views.delete_user, name='delete_user'),
    # Маршрути для словників
    path('dictionaries/', views.dictionaries_main, name='dictionaries_main'),
    path('admin/dictionaries/', views.admin_dictionaries_main, name='admin_dictionaries_main'),
    path('api/dictionaries/', views.get_dictionaries, name='get_dictionaries'),
    path('api/dictionaries/<int:id>/', views.get_dictionary, name='get_dictionary'),
    path('admin/api/dictionaries/', views.create_dictionary, name='create_dictionary'),
    path('edit_dictionary/<id>/', views.edit_dictionary, name='edit_dictionary'),
    path('delete_dictionary/<id>/', views.delete_dictionary, name='delete_dictionary'),
    # Маршрути для авторів
    path('authors/', views.authors_main, name='authors_main'),
    path('admin/authors/', views.admin_authors_main, name='admin_authors_main'),
    path('api/authors/', views.get_authors, name='get_authors'),
    path('api/authors/<int:id>/', views.get_author, name='get_author'),
    path('admin/api/authors/', views.create_author, name='create_author'),
    path('edit_author/<id>/', views.edit_author, name='edit_author'),
    path('delete_author/<id>/', views.delete_author, name='delete_author'),
]
