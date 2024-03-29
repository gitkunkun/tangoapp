from django import forms
from .models import Words

class WordsSearchForm(forms.Form):
    keyword = forms.CharField(
        label="検索",
        required=False,
        widget=forms.TextInput(attrs={"placeholder":"単語を検索"})
    )

class WordUploadForm(forms.ModelForm):
    class Meta:
        model = Words
        fields = (
            "genre",
            "name",
            "yaku",
            "ex_1",
            "ex_1_yaku",
        )
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "単語",
                }
            ),
            "yaku": forms.TextInput(
                attrs={
                    "placeholder": "単語の訳",
                }
            ),
            "explanation": forms.Textarea(
                attrs={
                    "placeholder": "商品の説明",
                }
            ),
            "ex_1": forms.Textarea(
                attrs={"placeholder": "例文-英語"}
            ),
            "ex_1_yaku": forms.Textarea(
                attrs={"placeholder": "例文-和訳"}
            ),
        }

class QuizAnswerForm(forms.Form):
    answer = forms.CharField(
        label="",
        required=True,
        widget=forms.TextInput(attrs={"placeholder":"回答を入力"})
    )