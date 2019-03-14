from django.shortcuts import render, redirect

import random
from joke.names import random_name
from joke.models import Article, Person


def random_users(num):
    for i in range(num):
        name, sex = random_name()
        Person.objects.create(
            name=name,
            sex=sex,
            age=random.randrange(18, 40)
        )


def home(request):
    nav = ['动漫', '音乐', '军事']
    article = Article.objects.get(id=1)
    person = Person.objects.get(name='Lucy')

    context = {
        'nav': nav,
        'article': article,
        'person': person,
    }
    return render(request, 'article.html', context)


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        description = request.POST['description']
        sex = request.POST['sex']
        city = request.POST['city']
        age = int(request.POST['age'])

        person = Person.objects.create(
            username=username,
            password=password,
            city=city,
            sex=sex,
            age=age,
            description=description,
        )
        return redirect('/user/info/?uid=%s' % person.id)
    else:
        return render(request, 'register.html')


def user_info(request):
    uid = request.GET['uid']
    person = Person.objects.get(id=uid)
    return render(request, 'show.html', {'person': person})