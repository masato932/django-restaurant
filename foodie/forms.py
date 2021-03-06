from django import forms
from .models import Category, Pref, Review # 追加


class ReviewForm(forms.ModelForm): # 追加
    class Meta:
        model = Review
        fields = ['score', 'comment']


class SearchForm(forms.Form):
    pref = forms.ModelChoiceField(
        label='都道府県',
        required=False,
        queryset=Pref.objects,
    )
    category = forms.ModelChoiceField(
        label='カテゴリ',
        required=False,
        queryset=Category.objects,
    )
    freeword = forms.CharField(
        label='フリーワード',
        required=False,
        min_length=2,
        max_length=100
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pref = self.fields['pref']
        category = self.fields['category']