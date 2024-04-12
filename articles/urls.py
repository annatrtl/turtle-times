from django.urls import path
from . import views

app_name = 'articles'

#url conf
urlpatterns = [
    path('', views.display, name = "list"),
    path('create/', views.article_create, name = "create"),
    path('<slug:slug>/', views.article_detail, name = "detail"),
]