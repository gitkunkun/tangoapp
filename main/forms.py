from django import forms
from .models import Words

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