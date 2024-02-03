from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from .forms import WordUploadForm
from .models import Genre, Words, Misstake
from django.shortcuts import render, redirect

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
    template_name = "main/word_detail.html"
    context_object_name = "words"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(pk=self.kwargs['pk']) # pkを指定してデータを絞り込む
        return context

def word_upload(request):
    if request.method == "GET":
        word_upload_form = WordUploadForm()
    elif request.method == "POST":
        word_upload_form = WordUploadForm(request.POST)
        if word_upload_form.is_valid():
            new_word = word_upload_form.save(commit=False)
            new_word.questioner = request.user
            new_word.save()
            return redirect("main:home")
    context = {
        "text_form": word_upload_form,
    }
    return render(request, "main/word_upload.html", context)