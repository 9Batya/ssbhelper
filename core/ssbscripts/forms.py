from django import forms

class NameForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

class share_smart_house(forms.Form):
    contract_nubmer = forms.CharField(label='Номер договора', empty_value=True)
    house_id = forms.CharField(label='House id', empty_value=True)

    field_order = ["contract_nubmer", "house_id"]


