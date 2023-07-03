from django.urls import path
from . import views

urlpatterns = [
    path("add_post/", views.add_post, name="add_post"),
    path("edit/<uuid:post_id>/", views.edit_post, name="edit_post"),
    path("delete/<uuid:post_id>/", views.delete, name="delete"),
]
