from django import forms
from companies.models import Company, CompanyVacancy, CompanyDocuments, InitialTestAnswers

class CreateCompany(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-auth_au',
    }), required=True)
    
    class Meta:
        model = Company
        fields = ('name',)
          

class AdditionVacancy(forms.ModelForm):
    CHOICES = [
        ('Нужен', 'Нужен'),
        ('Не нужен', 'Не нужен'),
    ]
    vacancy = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-auth_au',
        'id': 'form-id',
    }), required=False)
    open_vacancies = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-auth_au',
        'id': 'form-id',
    }), required=False)
    experience = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={
        'class': 'forms-auth_au'}), choices=CHOICES, required=False)
    # experience = forms.ChoiceField(widget=forms.RadioSelect(attrs={
    #     'class': 'forms-auth_au'}), choices=CHOICES, required=False)
    
    class Meta:
        model = CompanyVacancy
        fields = ('vacancy', 'open_vacancies', 'experience')
        

class CompanyProfile(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-auth_au',
    }), required=False)
    doc_title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-auth_au'
    }), required=False)
    files = forms.FileField(widget=forms.FileInput(attrs={
        'class': 'form-auth_au',
        # 'allow_multiple_selected': True
    }), required=False)
    doc_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-auth_au'
    }), required=False)
    
    class Meta:
        model = CompanyDocuments
        fields = ('name', 'doc_title', 'files', 'doc_name')
        

class CompanyImage(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'form-auth_au',
    }), required= False)
    
    class Meta:
        model = Company
        fields = ('image',)
        

class CompanyInfo(forms.ModelForm):
    info = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-auth_au'
    }), required=False)
    
    class Meta:
        model = Company
        fields = ('info', )
        
        
class InitialTest(forms.ModelForm):
    question = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-auth_au'
    }), required=True)
    answer = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-auth_au'
    }), required=True)
    
    class Meta:
        model = InitialTestAnswers
        fields = ('question', 'answer')