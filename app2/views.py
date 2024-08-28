from django.shortcuts import render

# Create your views here.
def temp2(request):
    d={'veg':'Tomato', 'veg1':'Capsicum', 'veg2':'Chillies'}
    return render(request, 'temp2.html', context=d)
