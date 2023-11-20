from django.shortcuts import render

# Create your views here.


def conditional(request):
    d={'a':1000}
    return render(request,'conditional.html',d)
def ifelse(request):
    d={'p':10,'q':20,'r':30}
    return render(request,'ifelse.html',d)