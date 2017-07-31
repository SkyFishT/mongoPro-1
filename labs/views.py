# coding: utf-8
from django.shortcuts import render,redirect
from models import *
from forms import LoginForm
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.


def index(request):
    # tmp = PpInfor.objects()
    # return render(request, 'labs/index.html', {'tmp': tmp})
    # tmp = User.objects.get(name='admin')
    # return render(request, 'labs/test.html')
    return render(request, 'labs/index.html')


def show(request):
    all = PpInfor.objects().only('title', 'pub_time', 'pub_name', 'autor_name', 'URL')
    errors = []
    if 'year' in request.GET:
        year = request.GET['year']
        if not year:
            errors.append('Enter a search year.')
        elif len(year) == -1:
            return render(request, 'labs/about.html', {'tmp': all, 'error': errors})
        elif len(year) != 4:
            errors.append('Please input a right year number.')
        else:
            tmp = PpInfor.objects(pub_time=year)
            return render(request, 'labs/about.html', {'tmp': tmp, 'query': year})
    return render(request, 'labs/about.html', {'tmp': all, 'error': errors})


def sign(request):
    return render(request, 'labs/signin.html')


def login_action(request):
    if 'username' in request.POST:
        name = request.POST.get('username', 'username')
        pwd = request.POST.get('password', 'password')
        tmp = User.objects.get(name=name)
        if name == tmp.name and pwd == tmp.pwd:
            all = PpInfor.objects().only('index', 'title', 'pub_time').order_by('-pub_time')
            return render(request, 'labs/manage.html', {"tmp": all, "name": name})


def edit(request, index):
    if index == '0':
        return render(request, 'labs/edit.html')
    else:
        paper = PpInfor.objects.get(index=int(index))
        return render(request, 'labs/edit.html', {'paper': paper})


def edit_action(request):
    index = request.POST.get('index', '0')
    title =request.POST.get('title', '')
    last_name = request.POST.getlist('last_name', '')
    first_name = request.POST.getlist('first_name', '')
    pub_time = int(request.POST.get('pub_time', '0'))
    pub_name = request.POST.get('pub_name', '')
    category = request.POST.get('category', '')
    accessNum = request.POST.get('accessNum', '')
    publish = request.POST.get('publish', '')
    commu_name = request.POST.get('commu_name', '')
    DOI = request.POST.get('DOI', '')
    SCI = request.POST.get('SCI', '')
    JCR = request.POST.get('JCR', '')
    EI = request.POST.get('EI', '')
    tzozif = request.POST.get('tzozif', '')
    tzofif =request.POST.get('tzofif', '')
    zkymp = request.POST.get('zkymp', '')
    fiyf = request.POST.get('fiyf', '')
    native = request.POST.get('native', '')
    quoted = request.POST.get('quoted', '')
    quote = request.POST.get('quote', '')
    URL = request.POST.get('URL', '')
    notes = request.POST.get('notes', '')
    num = len(PpInfor.objects)+1
    nm = []
    for (last, first) in zip(last_name, first_name):
        print last
        print first
        if first and last:
            name = Name(last_name=last.capitalize(), first_name=first.capitalize())
            nm.append(name)
    if index == '0':
        new = PpInfor(index=num, title=title, autor_name=nm, pub_time=pub_time, pub_name=pub_name, category=category,
                      accessNum=accessNum, publish=publish, commu_name=commu_name, DOI=DOI, SCI=SCI, JCR=JCR, EI=EI,
                      tzozif=tzozif,
                      tzofif=tzofif, zkymp=zkymp, fiyf=fiyf, native=native, quoted=quoted, quote=quote, URL=URL,
                      notes=notes)
        new.save()
        all = PpInfor.objects.only('index', 'title', 'pub_time').order_by('-pub_time')
        return render(request, 'labs/manage.html', {'tmp': all, 'error': []})
    else:
        old = PpInfor.objects.get(index=index)
        old.update(title=title, autor_name=nm, pub_time=pub_time, category=category, accessNum=accessNum,
                   publish=publish, commu_name=commu_name, DOI=DOI, SCI=SCI, JCR=JCR, EI=EI, tzozif=tzozif,
                   tzofif=tzofif, zkymp=zkymp, fiyf=fiyf, native=native, quoted=quoted, quote=quote, URL=URL, notes=notes)
        all = PpInfor.objects.only('index', 'title', 'pub_time').order_by('-pub_time')
        return render(request, 'labs/manage.html', {'tmp': all, 'error': []})


def delete(request, index):
    delete = PpInfor.objects.get(index=int(index))
    delete.delete()
    all = PpInfor.objects.only('index', 'title', 'pub_time').order_by('-pub_time')
    return render(request, 'labs/manage.html', {'tmp': all, 'error': []})


def manage(request):
    all = PpInfor.objects().only('index', 'title', 'pub_time').order_by('-pub_time')
    errors = []
    if 'year' in request.GET:
        year = request.GET['year']
        if not year:
            errors.append('Enter a search year.')
        elif len(year) != 4:
            errors.append('Please input a right year number.')
        else:
            tmp = PpInfor.objects(pub_time=year)
            return render(request, 'labs/manage.html', {'tmp': tmp, 'query': year})
    return render(request, 'labs/manage.html', {'tmp': all, 'error': errors})


def query_action(request):
    all = PpInfor.objects().only('index', 'title', 'pub_time').order_by('-pub_time')
    errors = []
    if 'key' and 'year' in request.GET:
        year = request.GET['year']
        key = request.GET['key'].lower()
        print year
        # 年份不在请求中，直接算总的查询集
        if not year:
            yrst = PpInfor.objects().only('index', 'title', 'pub_time', 'autor_name').order_by('-pub_time')
        elif len(year) != 4:  # 年份长度不对，做出警告
            yrst = []
            errors.append('请输入一个正确的年份！')
        else:  # 获得相应年份的查询集,年份存在，并且长度正确
            yrst = PpInfor.objects(pub_time=year).order_by('-pub_time')
        # 关键字存在
        if key:
            print key
            result = []
            for item in yrst:
                title = item.title
                if key in title.lower():
                    result.append(item)
                    continue
                for name in item.autor_name:
                    first = name.first_name.lower()
                    last = name.last_name.lower()
                    if key in first or key in last:
                        result.append(item)
            if not result:
                errors.append('没有找到匹配的文档！')
        else:
            result = yrst
        return render(request, 'labs/manage.html', {'tmp': result, 'error': errors})
    return render(request, 'labs/manage.html', {'tmp': all, 'error': errors})