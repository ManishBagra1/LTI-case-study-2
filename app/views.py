from django.shortcuts import render
from django.http import HttpResponse
from .forms import djangoform, contactform

# Create your views here.


def index(request):
    context = {
        'title': 'Homepage'
    }
    return render(request, 'index.html', context)


def searchstudent(request):
    form = djangoform(request.GET or None)
    context = {
        'form': form,
        'title': 'Search Student'
    }
    if form.is_valid():
        data = form.cleaned_data.get('sid')
        print('data is', data)
        file = open('app/Data/students.csv', mode='r')
        for line in file:
            if line.startswith(str(data)):
                temp = line.strip().split(',')
                break
        file.close()

        context = {
            'title': 'search result',
            'data': {
                'sid': temp[0],
                'name': temp[1],
                'gender': temp[2],
                'dob': temp[3],
                'city': temp[4],
                'state': temp[5],
                'email': temp[6],
                'qualification': temp[7],
                'stream': temp[8],
            }
        }
        return render(request, 'searchresult.html', context)

    return render(request, 'searchstudent.html', context)



def displayall(request):
    file = open('app/Data/students.csv', mode='r')
    data = []
    for line in file:
        x = line.strip().split(',')
        data.append({'sid': x[0], 'name': x[1], 'gender': x[2], 'dob': x[3], 'city': x[4],
                     'state': x[5], 'mail': x[6], 'qualification': x[7], 'stream': x[8]})
    file.close()
    data.remove(data[0])
    context = {
        'title':'All Students',
        'data' : data
        }
    return render(request,'allstudent.html',context)


def addstudent(request):
    form = contactform(request.POST or None)
    context = {
        'form': form,
        'title': 'Student Registraion'
    }

    if form.is_valid():
        sid = form.cleaned_data['sid']
        name = form.cleaned_data['name']
        gender = form.cleaned_data['gender']
        dob = form.cleaned_data['dob']
        city = form.cleaned_data['city']
        state = form.cleaned_data['state']
        email = form.cleaned_data['email']
        qualification = form.cleaned_data['qualification']
        stream = form.cleaned_data['stream']

        file = open('app/Data/students.csv', mode='a')
        dob = str(dob).strip().split('-')
        dob.reverse()
        dob = '-'.join(dob)
        data = f"{sid},{name},{gender},{dob},{city},{state},{email},{qualification},{stream}"
        file.write("\n"+data)
        file.close()

        return render(request,'index.html',{'title':'Homepage'})




    return render(request,'addstudent.html',context)