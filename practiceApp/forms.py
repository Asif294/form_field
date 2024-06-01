from django import forms 
from django.forms.widgets import NumberInput
import datetime,time

CHOICES = ['1980', '1981', '1982']
class contactFrom(forms.Form):
    name = forms.CharField(initial='your name',label="Enter your Name:",max_length=10)
    email = forms.EmailField(label = "User Email")
    # comment = forms.CharField(widget=forms.Textarea)
    agree = forms.BooleanField()
    # Birthday = forms.DateField(widget=NumberInput(attrs={'type':'date'}))
   
    Birthday = forms.DateField(widget=forms.SelectDateWidget(years=CHOICES))
    value = forms.DecimalField()
    email_address=forms.EmailField(required=False)
    day = forms.DateField(initial=datetime.date.today)
    
    favolite_color=[
        ('blur','Blur'),
        ('green','Green'),
        ('black','Black')
    ]
    Favorite_color=forms.ChoiceField(choices=favolite_color, required=False)
    Favorite_color=forms.ChoiceField(widget=forms.RadioSelect, choices=favolite_color, required=False)
    Favorite_color=forms.MultipleChoiceField( choices=favolite_color, required=False)
    Favorite_color=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple ,choices=favolite_color, required=False)
    # Model=forms.ModelChoiceField(
    #     queryset=MyModel.object.all(),initial=0
    # )
    field_name = forms.Field()
    roll_number = forms.IntegerField(help_text="Enter 6 digit roll Number ")
    Time= forms.TimeField()
    



    
