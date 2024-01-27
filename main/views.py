from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

from .models import Genre, Words, Misstake

class HomeView(LoginRequiredMixin, ListView):
    template_name = "main/home.html"
    model = Words
    context_object_name = "words"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = (
            queryset
            .order_by("-uploaded_at")[:4]
        )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["genres"] = Genre.objects.all()
        return context

class WordsDetailView(LoginRequiredMixin, DetailView):
    model = Words
    template_name = "main/words_detail.html"
    context_object_name = "words_detail"

    def get_context_data(self, **kwargs):
        queryset = Words.objects.get()
        return queryset