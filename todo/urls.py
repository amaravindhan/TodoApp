from django.urls import path

from . import views

app_name = "todo_app"

urlpatterns = [
    path('', views.home, name = "home"),
    path('<int:item_id>/delete/', views.delete, name = "delete")
]
