from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from . models import details,team
def home(request):
    obj = details.objects.all()
    obj2 = team.objects.all()
    return render(request,'index.html', {'result':obj,'team':obj2})

# def about(request):
#     return HttpResponse('Hai am About Man')
# def contact(request):
#     return render(request,'contactt.html')
# def details(req):
#     return render(req,'details.html')
# def thanks(req):
#     return HttpResponse('Thanks to come')
# def result(request):
#     a = int(request.GET['firstvalue'])
#     b = int(request.GET['secondvalue'])
#     add = a + b
#     sub = a - b
#     mult = a * b
#     div = a/b
#     return render(request,'result.html',{'addition': add,'subs':sub,'multi':mult,'divi':div})