from django.shortcuts import render

# Create your views here.
def temp1(request):
    d={'name':'vassu', 'age':22}
    return render(request, 'temp1.html', context=d)
