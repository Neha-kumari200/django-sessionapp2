from django.shortcuts import render

# Create your views here.


def setsession(request):
    request.session['name'] = 'Neha'
    request.session['lname'] = 'Singh'
    return render(request, 'testapp/setsession.html')


def getsession(request):
    name = request.session.get('name', default="None")
    #lname = request.session.get('lname', default="None")
    keys = request.session.keys()
    items = request.session.items()
    #age = request.session.setdefault('age', '24')

    #name = request.session('name')
    return render(request, 'testapp/getsession.html', {'name': name, 'keys': keys, 'items': items})


def delsession(request):
    request.session.flush()
    return render(request, 'testapp/delsession.html')



