
from django import forms
from .models import nation_name ,card_infomation ,CardWhoWantToSale

class subMit_form (forms.ModelForm):
    class Meta:
        model = CardWhoWantToSale
        fields = "__all__"

    def __init__(self , *args , **kwargs):
        super().__init__(*args , **kwargs)
        self.fields['cardSaleCode'].queryset = CardWhoWantToSale.objects.none()