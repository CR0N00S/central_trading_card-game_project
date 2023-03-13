
from django import forms
from .models import CardWhoWantToSale,transaction_table,card_infomation ,Rating

class subMit_form (forms.ModelForm):
    class Meta:
        model = CardWhoWantToSale
        # fields = "__all__"
        fields = ['sale_price','cardPhotoWhoWantSale']
        labels = {'cardPhotoWhoWantSale':'รูปการ์ด','sale_price':'ราคาที่ต้องการขาย'}
        
    def __init__(self,*args,**kwargs):
        super(subMit_form ,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})


    

    # def __init__(self , *args , **kwargs):
    #     super().__init__(*args , **kwargs)
    #     self.fields['card_code'].queryset = CardWhoWantToSale.objects.none()

class subMit_update_form (forms.ModelForm):
    class Meta:
        model = CardWhoWantToSale
        # fields = "__all__"
        fields = ['sale_price']
        labels = {'sale_price':'ราคาที่ต้องการจะตั้ง'}
    def __init__(self,*args,**kwargs):
        super(subMit_update_form ,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})



class transaction_submit (forms.ModelForm):
    class Meta:
        model = transaction_table
        fields = "__all__"
        # fields = ['fromSalerUser','toBuyerUser','buyerAddr','buyerPhone','card_code']




class change_price_adv (forms.ModelForm):
    class Meta:
        model = card_infomation
        fields = ['price_average']



class rate_this (forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rate','rateTxt']



class transactionGoTrue (forms.ModelForm):
    class Meta:
        model = transaction_table
        fields = ['is_rate']