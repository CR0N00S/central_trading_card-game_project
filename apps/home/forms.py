
from django import forms
from .models import nation_name ,card_infomation ,CardWhoWantToSale

class subMit_form (forms.ModelForm):
    class Meta:
        model = CardWhoWantToSale
        fields = [ 'cardFromNation' , 'cardSaleCode'  ,'sale_price', 'cardPhotoWhoWantSale']
        labels = {'cardFromNation': 'เนชั่นของการ์ด','cardSaleCode': 'รหัสการ์ด','cardPhotoWhoWantSale':'รูปการ์ด','sale_price':'ราคาที่ต้องการขาย'}

    def __init__(self , *args , **kwargs):
        super().__init__(*args , **kwargs)
        self.fields['cardPhotoWhoWantSale'].queryset = CardWhoWantToSale.objects.none()