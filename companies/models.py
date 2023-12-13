from django.db import models
from users.models import User

class Company(models.Model):
    name = models.CharField(max_length=30, primary_key=True, blank=False, null=False, unique=True)
    image = models.ImageField(upload_to='company_images', blank=True, null=True)
    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    info = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name
    
    
class CompanyVacancy(models.Model):
    name = models.ForeignKey(Company, on_delete=models.CASCADE)
    # username = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    vacancy = models.CharField(max_length=50, blank=False, null=False)
    open_vacancies = models.IntegerField(blank=True, null=True, default=None)
    experience = models.CharField(blank=True, null=True, default='Не нужен')
    info = models.TextField(blank=True, null=True)
    initial_test = models.CharField(blank=True, null=True, default='Теста нет')
    
    def __str__(self) -> str:
        return self.vacancy
        

class CompanyDocuments(models.Model):
    name = models.ForeignKey(Company, on_delete=models.CASCADE)
    doc_title = models.CharField(max_length=50, blank=False, null=False)
    files = models.FileField(upload_to='companies_files', blank=True, null=True)
    doc_name = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.doc_title


class InitialTestAnswers(models.Model):
    test = models.ForeignKey(CompanyVacancy, on_delete=models.CASCADE)
    question = models.TextField(blank=False, null=False)
    answer = models.TextField(blank=False, null=False)
    
    def __str__(self) -> str:
        return self.question
    
    
class UsersTests(models.Model):
    test = models.ForeignKey(CompanyVacancy, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    status = models.CharField(max_length=50, default='Не оценён')
    
    class Meta:
        unique_together = (('test'), ('username'))
        
        
class UsersVacancies(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    vacancy = models.ForeignKey(CompanyVacancy, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = (('username'), ('vacancy'))