from django import forms
from .models import Member,Activity,Inscription

# this is the member form to validate input
# data and customization
class MemberForm(forms.ModelForm):
    class Meta :
        model = Member
        fields = '__all__'

class ActivityForm(forms.ModelForm):
    class Meta :
        model = Activity
        fields = '__all__'


class InscriptionForm(forms.ModelForm):
    class Meta :
        model = Inscription
        fields = '__all__'