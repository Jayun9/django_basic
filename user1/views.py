from django.http import HttpResponse 
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import User1

# Create your views here.
def home(request):
    user_id = request.session.get('user')

    if user_id:
        user1 = User1.objects.get(pk=user_id)
        return HttpResponse(user1.username)
    return HttpResponse('Home!')

def login(request):
    if request.method == 'GET':
        return render(request, "login.html")
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        res_data = {}
        if not (username and password):
            res_data['error'] = '모든 값을 입력해야 합니다.'
        else:
            user1 = User1.objects.get(username=username)
            if check_password(password, user1.password):
                request.session['user']= user1.id
                return redirect('/')
            else:
                res_data['error']='비밀번호를 틀렸습니다.'
        return render(request, "login.html", res_data)
        

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password',None)
        re_password = request.POST.get('re-password',None)

        res_data = {}
        if not(username and password and re_password and useremail):
            res_data['error'] = "모든 값을 입력해야 합니다."
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            user1 = User1(
                username = username,
                password = make_password(password),
                useremail = useremail
            )
            user1.save()
        return render(request, 'register.html',res_data)