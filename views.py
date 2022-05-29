from django.shortcuts import render
from django.http import HttpResponse
from django import template
# Create your views here.

def base(request):
    return render(request, 'base.html')
def signup(request):
    return render(request, 'signup.html')
def welcm(request):
    return render(request, 'welcm.html')
def dash(request):
    return render(request, 'dash.html')
def home(request):
    errors=""
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')

        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            if(user.is_superuser):
                return redirect('welcm')
            try:
                if(Education.objects.get(user=user)):
                    return redirect('')
            except Education.DoesNotExist:
                errors="User name or password is wrong"          
    context={'errors':errors}
    return render(request,'home.html',context) 
    def register(request):
        form = CreateUserForm
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.save()
                s=Education.objects.create(user=user,username=form.cleaned_data.get('username'),fname=form.cleaned_data.get('first_name'),lname=form.cleaned_data.get('last_name'),sid=request.POST.get('sid'),email=form.cleaned_data.get('email'),phn=request.POST.get('num'))
                s.save()
                messages.success(request,"Account has been successfully created")
                return redirect('loginpage')
            context={'form':form}
            return render(request,'nbasystem/register.html',context)
