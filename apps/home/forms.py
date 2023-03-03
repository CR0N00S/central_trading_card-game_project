
from django import forms
from .models import nation_name ,card_infomation ,CardWhoWantToSale

class subMit_form (forms.ModelForm):
    class Meta:
        model = CardWhoWantToSale
        # fields = "__all__"
        fields = ['sale_price','cardPhotoWhoWantSale']
        labels = {'cardPhotoWhoWantSale':'รูปการ์ด','sale_price':'ราคาที่ต้องการขาย'}

    # def __init__(self , *args , **kwargs):
    #     super().__init__(*args , **kwargs)
    #     self.fields['card_code'].queryset = CardWhoWantToSale.objects.none()