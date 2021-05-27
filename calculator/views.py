from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'calculator/home.html')


def calculator(request):   
    if request.method =='GET':    
           return render(request, 'calculator/result.html')


    if request.method =='POST':       
        name = request.POST.get('name')
        age = request.POST.get('age')

        try:
            height = eval(request.POST.get('height'))
            weight = eval(request.POST.get('weight'))
            bmi = round(weight/(height/100)**2,2)        

        except Exception as e:
            print(e)

        return render(request, 'calculator/result.html', locals())

        