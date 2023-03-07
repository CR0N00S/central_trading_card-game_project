
from django import forms
from .models import CardWhoWantToSale,transaction_table,card_infomation

class subMit_form (forms.ModelForm):
    class Meta:
        model = CardWhoWantToSale
        # fields = "__all__"
        fields = ['sale_price','cardPhotoWhoWantSale']
        labels = {'cardPhotoWhoWantSale':'รูปการ์ด','sale_price':'ราคาที่ต้องการขาย'}

    # def __init__(self , *args , **kwargs):
    #     super().__init__(*args , **kwargs)
    #     self.fields['card_code'].queryset = CardWhoWantToSale.objects.none()

class subMit_update_form (forms.ModelForm):
    class Meta:
        model = CardWhoWantToSale
        # fields = "__all__"
        fields = ['sale_price']
        labels = {'sale_price':'ราคาที่ต้องการจะตั้ง'}


class transaction_submit (forms.ModelForm):
    class Meta:
        model = transaction_table
        fields = "__all__"
        # fields = ['fromSalerUser','toBuyerUser','buyerAddr','buyerPhone','card_code']

class change_price_adv (forms.ModelForm):
    class Meta:
        model = card_infomation
        fields = ['price_average']


