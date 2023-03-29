from django.shortcuts import render
import pandas as pd
# Create your views here.
from decimal import Decimal
from django.shortcuts import render

from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseNotFound

# Create your views here.
from myapp.models import Devices,EnergyMeter
data = pd.read_excel('data_day.xlsx')
# Extract the column data
inc_pow = data['INCOMER - kW Total']
reac_pow=data['INCOMER - kVAr Total']
# Use the extracted data
lst_pw=list(inc_pow.values)
lst_reac=list(reac_pow.values)
def admin_login(request):
    user = request.user
    if request.method == "POST":
        print(request.POST.get('email'))
        user_qs = User.objects.filter(email=request.POST.get('email'))
        print(user_qs.exists())
        try:
            if not user_qs.exists():
                raise User.DoesNotExist
            user = user_qs[0]
            user = authenticate(username=user.username,
                                password=request.POST.get('password'))
            if not user:
                raise User.DoesNotExist
            if user.is_superuser:
                print(user)
                login(request, user)
                return HttpResponseRedirect('/home/')
            elif user.is_staff:
                login(request, user)
                return HttpResponseRedirect('/home/')
            else:
                login(request, user)
                return HttpResponseRedirect('/home/')
        except User.DoesNotExist:
            return render(request, 'signin.html', {'error': 'Invalid Email or Password'})
    else:
        if user.is_authenticated:
            return HttpResponseRedirect('/home/')
        else:
            return render(request, 'signin.html', {'error': ''})


# Logout a user, then redirect to login page
@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')



@login_required
def admin_home(request):
    admin = request.user
    name = admin.first_name
    dlist = []
    data={}
    if admin.is_superuser:
        d1=Devices.objects.get(dev=1)
        d1s=d1.status
        d2=Devices.objects.get(dev=2)
        d2s=d2.status
        em=EnergyMeter.objects.last()
        sno = 0
        data['name']="Super Admin"
        data['state1']=d1s
        data['state2']=d2s
        data['volt']=em.volt
        data['crnt']=em.current
        data['enr']=em.energy
        latest=EnergyMeter.objects.all().order_by('-id')
        l=len(latest)
        if(l>10):
            l=10
        lbl=[]
        datas=[]
        for i in range(l):
            lbl.append(latest[i].id)
            datas.append(latest[i].energy)

        data['labels']=lbl
        data['data']=datas
        data['hi']="hello"
        return render(request, 'home.html', data)
    return render(request, '404.html', {'name': name})
@login_required
def eee(request):
    admin = request.user
    name = admin.first_name
    dlist = []
    data={}
    if admin.is_superuser:
        d1=Devices.objects.get(dev=1)
        d1s=d1.status
        d2=Devices.objects.get(dev=2)
        d2s=d2.status
        em=EnergyMeter.objects.last()


        sno = 0
        data['name']="Super Admin"
        data['state1']=d1s
        data['state2']=d2s
        data['volt']=em.volt
        data['crnt']=em.current
        data['enr']=em.energy
        latest=EnergyMeter.objects.all().order_by('-id')
        l=len(latest)
        if(l>10):
            l=10
        lbl=[12,1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4,5,6,7,8,9,10,11,12]
        datas=[10,20,30,40,50]
        for i in range(l):
            datas.append(latest[i].energy)

        data['labels']=[12,1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4,5,6,7,8,9,10,11,12]
        #data['labels1']=["sun","mon","tue","wed","thu","sat"]
        data['data']=datas
        data['hi']="hello"
        return render(request, 'eee.html', data)
    return render(request, '404.html', {'name': name})
def ece(request):
    admin = request.user
    name = admin.first_name
    dlist = []
    data={}
    if admin.is_superuser:
        d1=Devices.objects.get(dev=1)
        d1s=d1.status
        d2=Devices.objects.get(dev=2)
        d2s=d2.status
        em=EnergyMeter.objects.last()


        sno = 0
        data['name']="Super Admin"
        data['state1']=d1s
        data['state2']=d2s
        data['volt']=em.volt
        data['crnt']=em.current
        data['enr']=em.energy
        latest=EnergyMeter.objects.all().order_by('-id')
        l=len(latest)
        if(l>10):
            l=10
        lbl=[12,1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4,5,6,7,8,9,10,11,12]
        datas=[10,20,30,40,50]
        for i in range(l):
            datas.append(latest[i].energy)

        data['labels']=lbl
        data['data']=datas
        data['hi']="hello"
        return render(request, 'ece.html', data)
    return render(request, '404.html', {'name': name})
def cse(request):
    admin = request.user
    name = admin.first_name
    dlist = []
    data={}
    if admin.is_superuser:
        d1=Devices.objects.get(dev=1)
        d1s=d1.status
        d2=Devices.objects.get(dev=2)
        d2s=d2.status
        em=EnergyMeter.objects.last()


        sno = 0
        data['name']="Super Admin"
        data['state1']=d1s
        data['state2']=d2s
        data['volt']=em.volt
        data['crnt']=em.current
        data['enr']=em.energy
        latest=EnergyMeter.objects.all().order_by('-id')
        l=len(latest)
        if(l>10):
            l=10
        lbl=[12,1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4,5,6,7,8,9,10,11,12]
        datas=[10,20,30,40,50]
        for i in range(l):
            datas.append(latest[i].energy)

        data['labels']=lbl
        data['data']=datas
        data['hi']="hello"
        return render(request, 'cse.html', data)
    return render(request, '404.html', {'name': name})

def clg(request):
    admin = request.user
    name = admin.first_name
    dlist = []
    data={}
    if admin.is_superuser:
        d1=Devices.objects.get(dev=1)
        d1s=d1.status
        d2=Devices.objects.get(dev=2)
        d2s=d2.status
        em=EnergyMeter.objects.last()
        sno = 0
        data['name']="Super Admin"
        data['state1']=d1s
        data['state2']=d2s
        data['volt']=em.volt
        data['crnt']=em.current
        data['enr']=em.energy
        latest=EnergyMeter.objects.all().order_by('-id')
        l=len(latest)
        if(l>10):
            l=10
        lbl=[12,1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4,5,6,7,8,9,10,11,12]
        datas=[10,20,30,40,50]
        for i in range(l):
            datas.append(latest[i].energy)

        data['labels']=[12,1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4,5,6,7,8,9,10,11,12]
        data['labels1']=["sun","mon","tue","wed","thu","sat"]
        data['data']=datas
        data['hi']="hello"
        return render(request, 'college.html', data)
    return render(request, '404.html', {'name': name})

@login_required
def device_control(request):
    print(request.POST)
    id=request.POST.get('deviceid')
    dev=Devices.objects.filter(dev=id)
    contorl=request.POST.get('control')
    if(len(dev)>0):
        dev=dev[0]
        dev.status=contorl
        dev.save()
    else:
        dev=Devices(dev=id,status=contorl)
        dev.full_clean()
        dev.save()
    return HttpResponseRedirect('/eee/')

@csrf_exempt
def send_stat(request):
    print(request.GET)
    volt=request.GET.get('volt')
    crnt=request.GET.get('crnt')
    enr=request.GET.get('enr')
    em=EnergyMeter(volt=volt,current=crnt,energy=enr)
    em.full_clean()
    em.save()
    d=Devices.objects.all()
    d1=d[0].status
    d2=d[1].status
    s=["0","0"]
    if(d1=="on"):
        s[0]="1"
    if(d2=="on"):
        s[1]="1"
    data="".join(s)
    return HttpResponse(data,status=200)


@csrf_exempt
def get_stat(request):
    d=Devices.objects.all()
    d1=d[0].status
    d2=d[1].status
    s=["0","0"]
    if(d1=="on"):
        s[0]="1"
    if(d2=="on"):
        s[1]="1"
    data="".join(s)
    return HttpResponse(data)


