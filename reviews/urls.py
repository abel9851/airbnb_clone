from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path("create/<int:room>/", views.create_review, name="create"),
    path("update/<int:room>/<int:comment>", views.update_review, name="update"),
    path("delete/<int:room>/<int:comment>", views.delete_review, name="delete"),
]
