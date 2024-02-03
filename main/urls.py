from django.urls import path

from . import views

app_name = "main"
urlpatterns = [
    path("home", views.HomeView.as_view(), name="home"),
    path("words_detail/<int:pk>", views.WordsDetailView.as_view(), name="words_detail"),
    path("word_upload", views.word_upload, name="word_upload"),
]