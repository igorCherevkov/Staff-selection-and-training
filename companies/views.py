from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from companies.forms import CreateCompany, AdditionVacancy, CompanyProfile, CompanyImage, CompanyInfo, InitialTest
from companies.models import Company, CompanyVacancy, CompanyDocuments, InitialTestAnswers, UsersTests, UsersVacancies
from users.models import User


def mainPage(request):
    try:
        owner = Company.objects.get(owner_id = request.user.username)
    except:
        owner = None
    try:
        staff = UsersTests.objects.get(username_id = request.user.username)
    except:
        staff = None
    vacancies = CompanyVacancy.objects.all()
    companies = Company.objects.all()
    if owner:
        context = {
            'title': 'SSaT',
            'owner': owner,
            'vacancies': vacancies,
            'companies': companies
        }
    elif staff:
        context = {
            'title': 'SSaT',
            'staff': staff,
            'vacancies': vacancies,
            'companies': companies
        }
    else:
        context = {
            'title': 'SSaT',
            'owner': False,
            'staff': False,
            'vacancies': vacancies,
            'companies': companies
        }
    return render(request, 'companies/mainPage.html', context)


@login_required
def companyRegistration(request):
    try:
        owner = Company.objects.get(owner_id = request.user.username)
    except:
        owner = None
    try:
        staff = UsersTests.objects.get(username_id = request.user.username)
    except:
        staff = None
    if request.method == 'POST':
        formCreate = CreateCompany(data = request.POST)
        formVacancy = AdditionVacancy(data = request.POST)
        if formCreate.is_valid() and formVacancy.is_valid():
            company = Company()
            company.name = request.POST['name']
            company.owner_id = request.user.username
            company.save()
            if request.POST.getlist('vacancy')[0] != '':
                for i in range(len(request.POST.getlist('vacancy'))):
                    vacancy = CompanyVacancy()
                    if request.POST.get('vacancy'): vacancy.vacancy = request.POST.getlist('vacancy')[i] 
                    if request.POST.get('open_vacancies'): vacancy.open_vacancies = request.POST.getlist('open_vacancies')[i]
                    if request.POST.get('experience'): vacancy.experience = request.POST['experience']
                    vacancy.name_id = request.POST['name']
                    vacancy.save()
            return HttpResponseRedirect(reverse('companies:companyProfile'))
    else:
        formCreate = CreateCompany()
        formVacancy = AdditionVacancy()
    if owner:
        context = {
        'title': 'Регистрация компании',
        'formCreate': formCreate,
        'formVacancy': formVacancy,
        'owner': owner
    }
    elif staff:
        context = {
        'title': 'Регистрация компании',
        'formCreate': formCreate,
        'formVacancy': formVacancy,
        'staff': staff
    }
    else:
        context = {
        'title': 'Регистрация компании',
        'formCreate': formCreate,
        'formVacancy': formVacancy,
        'owner': False,
        'staff': False
    }
    return render(request, 'companies/companyRegistration.html', context)


@login_required
def companyProfile(request):
    try:
        owner = Company.objects.get(owner_id = request.user.username)
    except:
        owner = None
    try:
        staff = UsersTests.objects.get(username_id = request.user.username)
        company = Company.objects.get(name = CompanyVacancy.objects.get(id = staff.test_id).name_id)
    except:
        staff = None
    if request.method == 'POST':
        form = CompanyProfile(instance=owner, data = request.POST, files=request.FILES)
        formVacancy = AdditionVacancy(instance=owner, data = request.POST)
        companyImage = CompanyImage(files = request.FILES)
        companyInfo = CompanyInfo(instance=owner, data=request.POST)
        if request.FILES.get('image'):
            company = Company.objects.get(name = owner)
            company.image = request.FILES.get('image')
            company.save()
            Company.objects.filter(owner_id = request.user.username).update(name = request.POST['name'])
        if companyInfo.is_valid() and request.POST.getlist('info'):
            company = Company.objects.get(name = owner)
            company.info = request.POST['info']
            company.save()
        if form.is_valid():
            if dict(request.POST).get('doc_title') and dict(request.FILES).get('files'):
                docs = CompanyDocuments()
                docs.name = owner
                if dict(request.POST).get('doc_title')[0] == '': docs.doc_title = 'Файлы без темы'
                else: docs.doc_title = request.POST['doc_title']
                docs.files = request.FILES.get('files')
                docs.doc_name = request.POST['doc_name']
                docs.save()
            elif dict(request.POST).get('doc_title'): 
                docs = CompanyDocuments()
                docs.name = owner
                docs.doc_title = request.POST['doc_title']
                docs.doc_name = request.POST['doc_name']
                docs.save()
        if formVacancy.is_valid():
            for i in range(len(request.POST.getlist('vacancy'))):
                vacancy = CompanyVacancy()
                vacancy.name_id = owner
                vacancy.vacancy = request.POST.getlist('vacancy')[i]
                if request.POST.get('open_vacancies'): vacancy.open_vacancies = request.POST.getlist('open_vacancies')[i]
                if request.POST.get('experience'): vacancy.experience = request.POST['experience']
                vacancy.save()
        return HttpResponseRedirect(reverse('companies:companyProfile'))
    else:
        form = CompanyProfile(instance=owner)
        formVacancy = AdditionVacancy(instance=owner)
        companyImage = CompanyImage()
        companyInfo = CompanyInfo(instance=owner)
    if owner:
        files = CompanyDocuments.objects.filter(name_id = owner)
    else:
        files = CompanyDocuments.objects.filter(name_id = CompanyVacancy.objects.get(id = staff.test_id).name_id)
    files_title = []
    for i in range(len(list(files))):
        if files[i].doc_title not in files_title: files_title.append(files[i].doc_title)
    if owner:
        context = {
        'title': 'Профиль компании',
        'form': form,
        'formVacancy': formVacancy,
        'companyImage': companyImage,
        'companyInfo': companyInfo,
        'owner': owner,
        'files': files,
        'files_title': files_title,
        'companyName': owner,
        'vacancies': CompanyVacancy.objects.filter(name_id = owner).values()
    }
    elif staff:
        context = {
        'title': 'Профиль компании',
        'form': form,
        'formVacancy': formVacancy,
        'companyImage': companyImage,
        'companyInfo': companyInfo,
        'staff': staff,
        'files': files,
        'files_title': files_title,
        'companyName': company,
        'vacancies': CompanyVacancy.objects.filter(name_id = company.name).values()
    }
    else:
        context = {
        'title': 'Профиль компании',
        'form': form,
        'formVacancy': formVacancy,
        'companyImage': companyImage,
        'companyInfo': companyInfo,
        'owner': False,
        'staff': False,
        'files': files,
        'files_title': files_title,
        'companyName': owner,
        'vacancies': CompanyVacancy.objects.filter(name_id = owner).values()
    }
    return render(request, 'companies/companyProfile.html', context)


@login_required
def vacancyInfo(request, id):
    try:
        owner = Company.objects.get(owner_id = request.user.username)
    except:
        owner = None
    try:
        staff = UsersTests.objects.get(username_id = request.user.username)
    except:
        staff = None
    vacancyInfo = CompanyVacancy.objects.get(id = id)
    companyInfo = Company.objects.get(name = vacancyInfo.name_id)
    print(vacancyInfo.info)
    if companyInfo.info == None:
        companyInfo.info = 'Информации пока нет'
        companyInfo.save()
    if owner:
        context = {
        'title': 'Информация о вакансии',
        'vacancyInfo': vacancyInfo,
        'companyInfo': companyInfo,
        'owner': owner,
        }
    elif staff:
        context = {
        'title': 'Информация о вакансии',
        'vacancyInfo': vacancyInfo,
        'companyInfo': companyInfo,
        'staff': staff,
        }
    else:
        context = {
        'title': 'Информация о вакансии',
        'vacancyInfo': vacancyInfo,
        'companyInfo': companyInfo,
        'owner': False,
        'staff': False
        }
    return render(request, 'companies/vacancyInfo.html', context)


@login_required
def addInitialTest(request, id):
    try:
        owner = Company.objects.get(owner_id = request.user.username)
    except:
        owner = None
    try:
        staff = UsersTests.objects.get(username_id = request.user.username)
    except:
        staff = None
    vacancy = CompanyVacancy.objects.get(id = id)
    candidates = UsersTests.objects.filter(test_id = id, status = 'Не оценён')
    if request.method == 'POST':
        form = InitialTest(data = request.POST)
        if request.POST.getlist('testStatus'):
            for testStatus, candidate in zip(range(len(request.POST.getlist('testStatus'))), range(len(candidates))):
                UsersTests.objects.filter(username_id = candidates[candidate].username_id).update(status = request.POST.getlist('testStatus')[testStatus])
                if request.POST.getlist('testStatus')[testStatus] == 'Пройден':
                    vac = UsersVacancies()
                    vac.username_id = candidates[candidate].username_id
                    vac.vacancy_id = id
                    vac.save()
            return HttpResponseRedirect(reverse('companies:companyProfile'))
        if form.is_valid():
            for question, answer in zip(request.POST.getlist('question'), request.POST.getlist('answer')):
                newQuestion = InitialTestAnswers()
                newQuestion.question = question
                newQuestion.answer = answer
                newQuestion.test_id = id
                newQuestion.save()
            return HttpResponseRedirect(reverse('companies:companyProfile'))
    else:
        form = InitialTest()
    if owner:
        context = {
            'title': 'Добавление входного тестирования',
            'companyOwner': True,
            'form': form,
            'id': id,
            'vacancy': vacancy,
            'candidates': candidates,
            'owner': owner
        }
    elif staff:
        context = {
            'title': 'Добавление входного тестирования',
            'staff': staff,
            'form': form,
            'id': id,
            'vacancy': vacancy,
            'candidates': candidates
        }
    else:
        context = {
            'title': 'Добавление входного тестирования',
            'owner': False,
            'staff': False,
            'form': form,
            'id': id,
            'vacancy': vacancy,
            'candidates': candidates
        }
    return render(request, 'companies/addInitialTest.html', context)


@login_required
def initialTest(request, id):
    try:
        owner = Company.objects.get(owner_id = request.user.username)
    except:
        owner = None
    try:
        staff = UsersTests.objects.get(username_id = request.user.username)
    except:
        staff = None
    try: 
        questions = InitialTestAnswers.objects.filter(test_id = id)
        questions[0]
    except:
        questions = False
    if request.method == 'POST':
        score = 0
        for answer, answerBD in zip(request.POST.getlist('test_answer') ,range(len(questions))):
                if answer == questions[answerBD].answer: score += 1
        if UsersTests(username_id = request.user.username).check() != []:
            UsersTests.objects.filter(username_id = request.user.username).update(score = score, status = 'Не оценён', test_id = id)
        else:
            test = UsersTests()
            test.score = score
            test.username_id = request.user.username
            test.test_id = id
            test.save()
        return HttpResponseRedirect(reverse('mainPage'))
    else:
        pass
    if owner:
        context = {
            'title': 'Входное тестирование',
            'owner': owner,
            'id': id,
            'questions': questions
        }
    elif staff:
        context = {
            'title': 'Входное тестирование',
            'staff': staff,
            'id': id,
            'questions': questions
        }
    else:
        context = {
            'title': 'Входное тестирование',
            'owner': False,
            'staff': False,
            'id': id,
            'questions': questions
        }
    return render(request, 'companies/initialTest.html', context)