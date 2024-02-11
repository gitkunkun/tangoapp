from django.urls import path

from . import views

app_name = "main"
urlpatterns = [
    path("home", views.HomeView.as_view(), name="home"),
    path("words_detail/<int:pk>", views.WordsDetailView.as_view(), name="words_detail"),
    path("word_upload", views.word_upload, name="word_upload"),
    path("words_list", views.WordsListView.as_view(), name="words_list"),
    path("product_like/<int:pk>", views.word_like, name="like"),
    path("product_unlike/<int:pk>", views.word_unlike, name="unlike"),
    path("quiz", views.quiz, name="quiz")
]