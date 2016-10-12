from django import forms
from .models import Citizen

class SignupForm(forms.ModelForm):
    #firts_name = forms.CharField()
    #last_name = forms.CharField()

    class Meta:
        model = Citizen
        exclude = ['slug', 'password', 'last_login', 'groups', 'user_permissions', 'is_staff', 'is_superuser', 'is_active', 'date_joined']

    def save_user(self,  request, user, form, commit=False):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.country = self.cleaned_data['country']
        user.city = self.cleaned_data['city']
        user.age = self.cleaned_data['age']

        if commit:
            user.save()
        return user
        # profile, created = Citizen.objects.get_or_create(username=self.cleaned_data['username'], first_name=user.first_name, last_name=user.last_name, defaults={
        #     'country': self.cleaned_data['country'],
        #     'city': self.cleaned_data['city'],
        #     'age': self.cleaned_data['age']
        # })

        # if created:
        #     profile.save()

