from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from .forms import WordUploadForm, WordsSearchForm
from .models import Genre, Words, Misstake, Like
from django.db.models import Count, Exists, OuterRef
from django.shortcuts import render, redirect, get_object_or_404

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
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.select_related("questioner", "genre").annotate(
            likes_count=Count("likes_received"),
            is_liked=Exists(
                Like.objects.filter(user=self.request.user, word=OuterRef("pk"))
            ),
        )
        return queryset

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

def word_like(request, pk):
    word = get_object_or_404(Words, pk=pk)
    Like.objects.create(user=request.user, word=word)
    return redirect("main:words_detail", pk)

def word_unlike(request, pk):
    word = get_object_or_404(Words, pk=pk)
    Like.objects.filter(user=request.user, word=word).delete()
    return redirect("main:words_detail", pk)

class WordsListView(LoginRequiredMixin, ListView):
    template_name = "main/words_list.html"
    model = Words
    context_object_name = "words"

    def get_queryset(self):
        queryset = super().get_queryset()

        genre = self.request.GET.get("genre")
        if genre:
            queryset = queryset.filter(genre__name = genre)
        
        search_form = WordsSearchForm(self.request.GET)
        if search_form.is_valid():
            keyword = search_form.cleaned_data["keyword"]
            if keyword:
                keyword = keyword.split()
                for k in keyword:
                    queryset = queryset.filter(name__icontains=k)
        return queryset       
        