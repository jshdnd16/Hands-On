from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import StudentInformation, Education, Adress, FamilyBackground

class RegistrationForm(UserCreationForm):
    email =  forms.EmailField(required=True, help_text='Required. Enter a valid email address')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        }

    def clean_username(self):
        username = self.cleaned_data.get('username', '')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        return email.lower()

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentInformation
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address'}),
            'student_id': forms.TextInput(attrs={'placeholder': 'Student ID'}),
            'gender': forms.Select(attrs={'placeholder': 'Gender'}),
        }

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name', '')
        return first_name.title()

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name', '')
        return last_name.title()

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        return email.lower()

    def clean_student_id(self):
        student_id = self.cleaned_data.get('student_id', '')
        return student_id

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'
        exclude = ['student']
        widgets = {
            'elementary': forms.TextInput(attrs={'placeholder': 'Elementary School'}),
            'highschool': forms.TextInput(attrs={'placeholder': 'High School'}),
            'tertiary': forms.TextInput(attrs={'placeholder': 'Tertiary School'}),
            'achievements': forms.TextInput(attrs={'placeholder': 'Achievements'}),
            'year_graduated': forms.NumberInput(attrs={'placeholder': 'Year Graduated'}),
        }

    def clean_elementary(self):
        elementary = self.cleaned_data.get('elementary', '')
        return elementary.title()

    def clean_highschool(self):
        highschool = self.cleaned_data.get('highschool', '')
        return highschool.title()

    def clean_tertiary(self):
        tertiary = self.cleaned_data.get('tertiary', '')
        return tertiary.title()

    def clean_achievements(self):
        achievements = self.cleaned_data.get('achievements', '')
        return achievements.title()

class AddressForm(forms.ModelForm):
    class Meta:
        model = Adress
        fields = '__all__'
        exclude = ['student']
        widgets = {
            'street': forms.TextInput(attrs={'placeholder': 'Street'}),
            'barangay': forms.TextInput(attrs={'placeholder': 'Barangay'}),
            'city': forms.TextInput(attrs={'placeholder': 'City'}),
            'provice': forms.TextInput(attrs={'placeholder': 'Province'}),
            'zipcode': forms.NumberInput(attrs={'placeholder': 'Zip Code'}),
        }

    def clean_street(self):
        street = self.cleaned_data.get('street', '')
        return street.title()

    def clean_barangay(self):
        barangay = self.cleaned_data.get('barangay', '')
        return barangay.title()

    def clean_city(self):
        city = self.cleaned_data.get('city', '')
        return city.title()

    def clean_provice(self):
        provice = self.cleaned_data.get('provice', '')
        return provice.title()

class FamilyForm(forms.ModelForm):
    class Meta:
        model = FamilyBackground
        fields = '__all__'
        exclude = ['student']
        widgets = {
            'mothers_name': forms.TextInput(attrs={'placeholder': "Mother's Name"}),
            'mothers_contact': forms.TextInput(attrs={'placeholder': "Mother's Contact"}),
            'fathers_name': forms.TextInput(attrs={'placeholder': "Father's Name"}),
            'fathers_contact': forms.TextInput(attrs={'placeholder': "Father's Contact"}),
            'guardian': forms.TextInput(attrs={'placeholder': "Guardian's Name"}),
        }

    def clean_mothers_name(self):
        mothers_name = self.cleaned_data.get('mothers_name', '')
        return mothers_name.title()

    def clean_fathers_name(self):
        fathers_name = self.cleaned_data.get('fathers_name', '')
        return fathers_name.title()

    def clean_guardian(self):
        guardian = self.cleaned_data.get('guardian', '')
        return guardian.title()

    def clean_mothers_contact(self):
        mothers_contact = self.cleaned_data.get('mothers_contact', '')
        return mothers_contact

    def clean_fathers_contact(self):
        fathers_contact = self.cleaned_data.get('fathers_contact', '')
        return fathers_contact