from django.shortcuts import render

def my_lambda(request):
    return render(request, 'lambda/Lambda_function.html')

def login(request):
    return render(request, 'lambda/login.html')
def logged_out(request):
    return render(request, 'lambda/logged_out.html')
def index(request):
    return render(request, 'lambda/index.html')


